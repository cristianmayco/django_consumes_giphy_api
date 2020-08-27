import requests
from .requests_informations import RequestsConfigurations as conf


class RequestsFactory:

    def indexPage(self):
        url = f"{conf.URL_BASE.value}{conf.SEARCH_FORM.value}?api_key={conf.API_KEY.value}" \
              f"&limit={conf.LIMIT.value}&rating={conf.RATING.value}"

        data = requests.get(url).json()
        return data['data']
