import requests
import json
from unittest import mock
import logging

url = 'http://httpbin.org/post'
data = {
    "data": [{
        'userid': 'admin',
        'pwd': '123456',
        'date': '20200515'
    }]
}


def send_post(url, data):
    res = requests.post(url=url, data=data).json()
    return json.dumps(res, indent=2, sort_keys=True)


print(send_post(url, data))

logging.debug('this is a debug日志')
logging.info('this is a  info')
logging.warning('this is a warning')
logging.error('this is a error')
logging.critical('this is a critical message')
