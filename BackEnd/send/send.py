import requests

with open('img.png', 'rb') as f:
    r = requests.post('http://10.1.248.11:80/image', files={'img.png': f})