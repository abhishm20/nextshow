import uuid
from datetime import datetime
from datetime import timedelta

from hashids import Hashids

hashids = Hashids(alphabet='0123456789ADUXYM', min_length=5)


def unique_id():
    return str(uuid.uuid1())


def from_seconds(seconds):
    seconds = int(float(seconds))
    return datetime.fromtimestamp(seconds)


def to_seconds(dt):
    return int(float(dt.strftime("%s")))


def delta_time(tm, ch_dict):
    if tm is None:
        tm = datetime.now()
    return tm + timedelta(**ch_dict)


def current_time():
    timestamp = datetime.now()
    return timestamp


def start_of_day(dt=None):
    if dt is None:
        dt = datetime.now()
    return from_seconds(to_seconds(dt)).replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(dt=None):
    if dt is None:
        dt = datetime.now()
    return from_seconds(to_seconds(dt)).replace(hour=23, minute=59, second=59, microsecond=999)


def start_of_week(dt=None):
    if dt is None:
        dt = datetime.now()
    return start_of_day(from_seconds(to_seconds(dt))) - timedelta(days=dt.weekday())


def end_of_week(dt=None):
    if dt is None:
        dt = datetime.now()
    return end_of_day(delta_time(start_of_week(dt), {'days': 6}))


def start_of_fortnight(dt=None):
    if dt is None:
        dt = datetime.now()
    if dt.day > 15:
        return delta_time(start_of_month(), {'days': 15})
    else:
        return start_of_month()


def end_of_fortnight(dt=None):
    if dt is None:
        dt = datetime.now()
    if dt.day > 15:
        return end_of_month()
    else:
        return end_of_day(delta_time(delta_time(start_of_month(), {'days': 15}), {'seconds': -1}))


def start_of_month(dt=None):
    if dt is None:
        dt = datetime.now()
    return start_of_day(from_seconds(to_seconds(dt)).replace(day=1))


def end_of_month(dt=None):
    if dt is None:
        dt = datetime.now()
    return delta_time(start_of_month(delta_time(start_of_month(dt), {'days': 32})), {'seconds': -1})


def add_time(delta, tm=None):
    if not tm:
        tm = get_current_time()
    return tm + timedelta(seconds=delta)


def format_date(object):
    return object.strftime("%a, %d %b %Y")


def format_date_time(object):
    return object.strftime("%I:%M %p  %d %b %Y")


def format_time_to(object, format_str):
    return object.strftime(format_str)
