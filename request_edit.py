import requests
from dotenv import load_dotenv
import os
import datetime

import pyshorteners
load_dotenv()


class NewsRequest():
    def __init__(self):
        self._API_NEWS_KEY = str(os.getenv("API_KEY"))
        self._request_url = f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={self._API_NEWS_KEY}'
        self.last_news_string = {'date':0}
    def take_actual_news(self):
        result_string = []
        if self.last_news_string is None or self.last_news_string['date'] != datetime.date.today():
            request = requests.get(self._request_url).json()
            for articl in request['articles'] :
                result_string.append(f'Дата публикации:{articl['publishedAt'][11:16]}\nСсылка:{(articl['url'])}\n\n')
            self.last_news_string = {'date':datetime.date.today(),
                                     'data':result_string}
            return result_string
        return self.last_news_string['data']


n = NewsRequest()
print(n.take_actual_news())
