import requests

#url = "http://10.69.41.156:9123/openapi/api-auth/"
url = "http://10.69.41.156:9123/openapi/api-token-auth/"
payload = {
    'username': 'admin',
    'password': 'admin@888'
}
response = requests.request("POST", url, data = payload)
print(response.text.encode('utf8'))

