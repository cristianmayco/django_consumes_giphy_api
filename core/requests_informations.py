from enum import Enum
import requests


class RequestsConfigurations(Enum):
    URL_BASE = 'https://api.giphy.com/v1/gifs/'
    TRENDING = 'trending'
    SEARCH_FORM = 'search'
    API_KEY = 'zPfJHNJ2bGCpUJr7jyvcW0RcctC2QOUN'
    LIMIT = 10
    RATING = 'g'
    ICON = 'https://developers.giphy.com/static/img/dev-logo-lg.7404c00322a8.gif'
    LANGUAGE = 'en'
    OFFSET = 1
