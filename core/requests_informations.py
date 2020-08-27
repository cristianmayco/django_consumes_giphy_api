from enum import Enum
import requests


class RequestsConfigurations(Enum):
    URL_BASE = 'https://api.giphy.com/v1/gifs/'
    SEARCH_FORM = 'trending'
    API_KEY = 'zPfJHNJ2bGCpUJr7jyvcW0RcctC2QOUN'
    LIMIT = 10
    RATING = 'g'


