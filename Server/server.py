from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json


lights = {
        "kitchen": 0,
        "livingroom": 0        
    }
sensors = {
        "temperature": {
            "kitchen": 0,
            "livingroom": 0
        },
        "humidity": {
            "kitchen": 0,
            "livingroom": 0
        }
    }

class GET(RequestHandler):
    def get(self):
        self.write({"lights": lights, "sensors": sensors})


class LightStatus(RequestHandler):
    def post(self):
        lights.update(json.loads(self.request.body.decode('ascii'))) 
        self.write({'message': json.loads(self.request.body)})

class SensorReadings(RequestHandler):
    def post(self):
        sensors.update(json.loads(self.request.body.decode('ascii')))
        self.write({'message': json.loads(self.request.body)})

class RemoveLight(RequestHandler):
    def post(self):
        lights.pop()
        self.write({'message': lights} )

class RemoveSensor(RequestHandler):
    def post(self):
        sensors.pop()
        self.write({'message': sensors} )

def make_app():
    urls = [
        ("/", GET),
        ("/push/lights/", LightStatus),
        ("/push/sensors/", SensorReadings),
        ("/push/lights/remove/", RemoveLight),
        ("/push/sensors/remove/", RemoveSensor)
    ]
    return Application(urls, debug=True)
  
if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()