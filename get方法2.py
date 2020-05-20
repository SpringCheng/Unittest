import requests

url = "https://www.baidu.com"
params = {
    "id": "1001,1002",
    "city":"shanghai"
}

r = requests.get(url, params=params)
print(r.url)
