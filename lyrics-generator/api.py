import requests

length = 20
text = 'Привет!'
url = 'https://127.0.0.1:8000/predict'   #'https://127.0.0.1:8000/predict'

resp = requests.get(url, params={'text': text, 'length': length})
print(resp.status_code)
print(resp.content.decode('utf-8'))