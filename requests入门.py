from selenium import webdriver
import requests
import json

url = 'http://httpbin.org/get'
# hearder = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
#                          ' Chrome/65.0.3325.181 Safari/537.36'}
data = {
    'name': 'admin',
    'age': 20
}


# 定义函数 ，封装get请求
def send_get(url, data):
    res = requests.get(url=url, params=data).json()
    return json.dumps(res, indent=2, sort_keys=True)


print(send_get(url, data))
