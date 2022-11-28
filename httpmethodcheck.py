import http.client

print('Enter a URL:')
URL = input()

protocol, domain = URL.split("://")

options = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'OPTIONS', 'HEAD', 'ARBITRARY']

def test_options():
        conn.request(opt, '/')
        response = conn.getresponse()
        print(opt, response.status, response.reason)

for opt in options:
    if protocol == "http":
        conn = http.client.HTTPConnection(domain)
        test_options()
    elif protocol == "https":
        conn = http.client.HTTPSConnection(domain)
        test_options()
    else:
        print ('Invalid value...')
        exit()
