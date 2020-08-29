import requests
from .requests_informations import RequestsConfigurations as conf


class RequestsFactory:

    def indexPage(self, search):
        url = f'{conf.URL_BASE.value}'

        if search is None or search == '':
            url = f"{url}{conf.TRENDING.value}?api_key={conf.API_KEY.value}" \
                  f"&limit={conf.LIMIT.value}&rating={conf.RATING.value}"
        else:
            url = f"{url}{conf.SEARCH_FORM.value}?api_key={conf.API_KEY.value}" \
                  f"&q={search}&limit={conf.LIMIT.value}&offset={conf.OFFSET.value}" \
                  f"&rating={conf.RATING.value}&lang={conf.LANGUAGE.value}"

        data = requests.get(url).json()
        return data['data']
