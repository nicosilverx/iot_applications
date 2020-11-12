from MyMQTT import *
import json, time

class Led():
    def __init__(self, clientID, topic, broker, port):
        self.client = MyMQTT(clientID, broker, port, self)
        self.topic = topic
        self.status = None

    def start(self):
        self.client.start()
        self.client.mySubscribe(self.topic)

    def stop(self):
        self.client.stop()

    def notify(self, topic, payload):
        payload = json.loads(payload)
        new_status = payload["value"]
        self.status = new_status
        pubID = payload["clientID"]
        timestamp = payload["timestamp"]
        print(f"The led has been set to {new_status} at {timestamp} by {pubID}")
        json.dump(payload, open("temp_log.json", "a"))

if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    broker = conf["broker"]
    port = conf["port"]
    myLed = Led("myLed", "IoT/nico/led", broker, port)

    myLed.start()
    
    while(1):
        time.sleep(1)
    myLed.stop()