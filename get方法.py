import requests

url = "https://www.baidu.com"
r = requests.get(url)
print("状态码", r.status_code)
print("响应文本:", r.text)
