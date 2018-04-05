from requests import get

URL = 'http://google.com'

google = get(URL)

print('Status code : {0} '.format(google.status_code))

print('Headers : {0}'.format(google.headers))

print('Cookies : {0}'.format(google.cookies))

print('Text : {0}'.format(google.text))

print(google.encoding)

google.close()
