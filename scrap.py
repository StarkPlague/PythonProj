import requests

url = "https://courses.wscubetech.com/"
req = requests.get(url)


print(req.status_code)
