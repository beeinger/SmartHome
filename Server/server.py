from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json


items = []
readings = []

class GETer(RequestHandler):
    def get(self):
        self.write({"items": items, "readings": readings})


class POSTer(RequestHandler):
    def post(self):
        items.append(json.loads(self.request.body.decode('ascii'))) 
        self.write({'message': json.loads(self.request.body)})

class Readings(RequestHandler):
    def post(self):
        readings.append(json.loads(self.request.body.decode('ascii')))
        self.write('Message sent: ')
        self.write(json.loads(self.request.body.decode('ascii')))

class Remove(RequestHandler):
    def post(self):
        items.pop()
        self.write({'message': items} )

def make_app():
    urls = [
        ("/", GETer),
        ("/api/item/", POSTer),
        ("/api/item/remove/", Remove),
        ("/api/reading/", Readings)
    ]
    return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()