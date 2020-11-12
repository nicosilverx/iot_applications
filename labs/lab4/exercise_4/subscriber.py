from MyMQTT import *
import json, time, os

class mySubscriber():
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
        new_status = payload["e"][0]["v"]
        self.status = new_status
        pubID = payload["bn"]
        timestamp = payload["e"][0]["t"]

        if new_status < 41:
            status = "Nominal"
        elif new_status < 71:
            status = "Warning"
        else:
            status = "Danger!!"
        print(f"The led has been set to {new_status} at {timestamp} by {pubID} - Status: {status}")


if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    broker = conf["broker"]
    port = conf["port"]
    mySub = mySubscriber("mySubscriber", "IoT/nico/exercise_4", broker, port)

    mySub.start()
    
    while(1):
        time.sleep(1)
    mySub.stop()