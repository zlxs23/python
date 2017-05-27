from wsgiref.simple_server import make_server
from browser import application

# create a Sever IP address = None, Port = 8000, handlerFun = application
httpd = make_server('', 8000, application)
print('Servering...')
httpd.serve_forever()