import requests

responce = requests.get('https://www.walissonsilva.com')

print('Status code: ', responce.status_code)
print('Header: ')
print(responce.headers)

print('\n Content: ')
print(responce.content)