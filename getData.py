import pprint
import time
from requests import request, session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=volume_24h'
parameters = {
    'start': '1',
    'limit': '10'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '80832223-74db-401b-8268-948b9d767a8b'
}

session = session()
session.headers.update(headers)

try:
    start_time = int(round(time.time() * 1000))
    response = session.get(url, params=parameters)
    current_time = int(round(time.time() * 1000))
    time_resp = current_time - start_time  # время ответа от ресурса
    size = len(response.text)  # размер полученного пакета данных
    data = json.loads(response.text)['data'][0:10]
    date = data[0]['last_updated']
    date = date.split()
    date = date[0][0:10]  # дата обновления тикеров
    # pprint.pprint(data) # вывод на экран полученных данных
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
