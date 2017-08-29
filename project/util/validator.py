import logging
import re
import smtplib
import socket

from dns import resolver
from twilio.rest import Client

import error_msg
from conf import ADMIN_EMAIL, VALIDATION
from conf import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


def validate_mobile(mobile, country_code="+91"):
    if not VALIDATION:
        return True, ""

    match = re.match('^[789]\d{9}$', mobile)
    if not match:
        return False, error_msg.INVALID % "Mobile Number"
    else:
        return True, ""

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        logging.getLogger('custom').info("Validation Mobile: %s-%s ..." % (str(country_code),str(mobile)))
        number = client.lookups.phone_numbers("%s%s" % (country_code, mobile)).fetch(type="carrier")
        if number.carrier['type'] == 'mobile':
            return True, ""
        else:
            return False, error_msg.NO_LANDLINE_MOBILE_NUMBER
    except Exception as e:
        logging.getLogger('custom').exception("Validating mobile number")
        return True, ""


def validate_email(email):
    if not VALIDATION:
        return True, ""
    email_address = email
    logging.getLogger('custom').info("Validation Email: %s ..." % (str(email)))
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address)
    if not match:
        return False, error_msg.INVALID % "Email"
    else:
        return True, ""

    try:
        # Pull domain name from email address
        domain_name = email_address.split('@')[1]

        # get the MX record for the domain
        records = resolver.query(domain_name, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)

        # check if the email address exists

        # Get local server hostname
        host = socket.gethostname()

        # SMTP lib setup (use debug level for full output)
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail(ADMIN_EMAIL)
        code, message = server.rcpt(str(email_address))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            return True, ""
        else:
            return False, error_msg.INVALID % "Email"
    except:
        logging.getLogger('custom').exception("Validating email")
        return True, ""
