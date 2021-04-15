import requests

print('hello world!')

try:
    request = requests.get('http://www.goo gle.com')
    print(request.status_code)
    if request.status_code == 200:
        print(request.text)
except Exception as ex:
    print('Ada Error', ex)