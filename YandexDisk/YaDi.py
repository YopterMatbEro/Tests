import requests
import configparser
import json


config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config.get('YandexDisk', 'TOKEN')

url = 'https://disk.yandex.ru/client/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + TOKEN}
data = {'path': '/Загрузки/Adobe Photoshop CS6.zip'}

response = requests.get(url, headers=headers)

if response.status_code == 201:
    print('Папка успешно создана')
else:
    print('Ошибка {}: {}'.format(response.status_code, response.text))