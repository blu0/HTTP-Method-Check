import http.client

print('Enter a URL:')
URL = input()

protocol, domain = URL.split("://")

if protocol == "http":
    print(protocol, domain)
    
    options = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'OPTIONS', 'HEAD', 'ARBITRARY']

    for opt in options:
        conn = http.client.HTTPConnection(domain)
        conn.request(opt, '/')
        response = conn.getresponse()
        print(opt, response.status, response.reason)

elif protocol == "https":
    print(protocol, domain)

    options = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'TRACE', 'OPTIONS', 'HEAD', 'ARBITRARY']

    for opt in options:
        conn = http.client.HTTPSConnection(domain)
        conn.request(opt, '/')
        response = conn.getresponse()
        print(opt, response.status, response.reason)

else:
    print ('Invalid value...')
    exit()
