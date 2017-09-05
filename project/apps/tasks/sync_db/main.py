import logging
import time

from imdbpie import Imdb
from process import run
from util.decorator import timeit

imdb = Imdb(anonymize=True)  # to proxy requests


@timeit
def get_title(imdb_id):
    try:
        title = imdb.get_title_by_id(imdb_id)
        return title
    except Exception as e:
        logging.getLogger('error').error(str(imdb_id) + str(e), exc_info=True)
        return None


def sync():
    count = 1
    while count < 9999999:
        start_time = time.time()
        title = get_title("tt" + str(count).zfill(7))
        try:
            if title:
                run(title.__dict__)
        except Exception as e:
            logging.getLogger('error').error(str(e))
            continue
        count += 1
        logging.getLogger('debug').debug("--- %s seconds ---" % str(time.time() - start_time))
        logging.getLogger('debug').debug("--- %s counts ---" % str(count))
