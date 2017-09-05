import logging
import time

from imdbpie import Imdb
from process import run
from util.decorator import timeit

concurrent = 2
imdb = Imdb()  # to proxy requests


@timeit
def get_titles(imdb_ids):
    try:
        titles = imdb.get_title_by_ids(imdb_ids)
        return titles
    except Exception as e:
        logging.getLogger('error').error(str(imdb_ids) + str(e), exc_info=True)
        return None


def sync():
    count = 1
    period = 999
    while count < 4000000:
        start_time = time.time()
        for title in get_titles(["tt" + str(index).zfill(7) for index in range(count, count + period)]):
            try:
                if title:
                    run(title.__dict__)
            except Exception as e:
                logging.getLogger('error').error(str(e))
                continue
        count += period
        logging.getLogger('debug').debug("--- %s seconds ---" % str(time.time() - start_time))
        logging.getLogger('debug').debug("--- %s counts ---" % str(count))
