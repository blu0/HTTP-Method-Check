import http.client

print('Enter a URL beginning with http or https:')
URL = input()

protocol, domain = URL.split("://")

options = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'OPTIONS', 'HEAD', 'ARBITRARY']

def test_options():
    conn.request(opt, '/')
    response = conn.getresponse()
    print(opt, response.status, response.reason)

for opt in options:
    if protocol.lower() == "http":
        conn = http.client.HTTPConnection(domain)
        test_options()
    elif protocol.lower() == "https":
        conn = http.client.HTTPSConnection(domain)
        test_options()
    else:
        print ('Invalid value...')
        exit()
