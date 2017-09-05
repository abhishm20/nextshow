import logging
import time

from imdbpie import Imdb
from process import run
from util.decorator import timeit

concurrent = 2
imdb = Imdb(anonymize=True)  # to proxy requests

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
    while count < 4000000:
        start_time = time.time()
        for title in get_titles(["tt" + str(index).zfill(7) for index in range(count, count + 9999)]):
            run(title.__dict__)
        count += 9999
        logging.getLogger('debug').debug("--- %s seconds ---" % str(time.time() - start_time))
        logging.getLogger('debug').debug("--- %s counts ---" % str(count))
