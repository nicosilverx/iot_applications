from MyMQTT import *
import json, time

class LedManager():
    def __init__(self, clientID, topic, broker, port):
        self.client = MyMQTT(clientID, broker, port, self)
        self.topic = topic
        self.status = None
        self.__message = {"clientID" : clientID,
                          "n" : "switch",
                          "value" : None,
                          "timestamp" : "",
                          "unit" : "bool"}

    def start(self):
        self.client.start()

    def stop(self):
        self.client.stop()

    def publish(self, value):
        message = self.__message
        message["value"] = value
        message["timestamp"] = str(time.time())
        self.client.myPublish(self.topic, message)

if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    broker = conf["broker"]
    port = conf["port"]
    myLedManager = LedManager("myLedManager", "IoT/nico/led", broker, port)
    myLedManager.start()

    while(1):
        print("Welcome to the client to switch on/off the lamp\n")
        print("Type:\n'on' to set the light on")
        print("'off' to set it off")
        print("'q' to quit")

        cmd = input()

        if cmd == "on":
            myLedManager.publish("on")
        elif cmd == "off":
            myLedManager.publish("off")
        elif cmd == "q":
            break

    myLedManager.stop()        



    