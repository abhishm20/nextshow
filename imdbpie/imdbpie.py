from __future__ import absolute_import, unicode_literals

import datetime
import json
import logging
import random
import time
import warnings

import grequests
import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache
from six.moves.urllib.parse import urlencode, quote

from imdbpie.constants import (
    BASE_URI, SHA1_KEY, USER_AGENTS, DEFAULT_PROXY_URI
)
from imdbpie.objects import Title

logger = logging.getLogger(__name__)


class Imdb(object):
    def __init__(self, api_key=None, locale=None, anonymize=False,
                 exclude_episodes=False, user_agent=None, cache=None,
                 proxy_uri=None, verify_ssl=True):
        self.api_key = api_key or SHA1_KEY
        self.timestamp = time.mktime(datetime.date.today().timetuple())
        self.user_agent = user_agent or random.choice(USER_AGENTS)
        self.locale = locale or 'en_US'
        self.exclude_episodes = exclude_episodes
        self.caching_enabled = True if cache is True else False
        self.proxy_uri = proxy_uri or DEFAULT_PROXY_URI
        self.anonymize = anonymize
        self.verify_ssl = verify_ssl
        self.session = requests

        if self.caching_enabled:
            warnings.warn('caching will be removed in version 5.0.0 '
                          'due to not being thread safe')
            self.session = CacheControl(
                requests.Session(), cache=FileCache('.imdbpie_cache')
            )

    def get_title_by_ids(self, imdb_ids):
        response = []
        main_urls = [self._build_url('/title/maindetails', {'tconst': imdb_id}) for imdb_id in imdb_ids]

        titles = self._get(main_urls)
        for title in titles:
            try:
                title = json.loads(title.content.decode('utf-8'))
            except Exception:
                logging.getLogger('error').error("Error %s" % str(title))
                continue

            if title.get('error') or title is None or self._is_redirection_result(title):
                titles.append(None)
                continue

            title = Title(data=title['data'])
            response.append(title)
        return response

    def _get(self, urls):
        rs = (grequests.get(url,
                            headers={'User-Agent': self.user_agent},
                            verify=self.verify_ssl) for url in urls)
        return grequests.map(rs)

    def _build_url(self, path, params):
        default_params = {
            'api': 'v1',
            'appid': 'iphone1_1',
            'apiPolicy': 'app1_1',
            'apiKey': self.api_key,
            'locale': self.locale,
            'timestamp': self.timestamp
        }

        query_params = dict(
            list(default_params.items()) + list(params.items())
        )
        query_params = urlencode(query_params)
        url = '{base}{path}?{params}'.format(base=BASE_URI,
                                             path=path, params=query_params)

        if self.anonymize is True:
            return self.proxy_uri.format(quote(url))
        return url

    @staticmethod
    def _is_redirection_result(response):
        """
        Return True if response is that of a redirection else False
        Redirection results have no information of use.
        """
        imdb_id = response['data'].get('tconst')
        if (
            imdb_id and
            imdb_id != response['data'].get('news', {}).get('channel')
        ):
            return True
        return False
