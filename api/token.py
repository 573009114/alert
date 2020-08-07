import requests


url = "http://10.18.41.156:9123/openapi/api-token-auth/"
payload = {
    'username': 'admin',
    'password': 'admin@888'
}
response = requests.request("POST", url, data = payload)
print(response.text.encode('utf8'))

