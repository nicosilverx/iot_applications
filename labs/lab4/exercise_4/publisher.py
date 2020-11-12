from MyMQTT import *
import json, random, time

class myPublisher():
    def __init__(self, clientID, topic, broker, port):
        self.client = MyMQTT(clientID, broker, port, self)
        self.topic = topic
        self.status = None
        self.__message = {"bn" : "sensor1",
                          "e" : [
                              {
                                  "n" : "temperature",
                                  "u" : "Cel",
                                  "t" : "",
                                  "v" : 0
                              }
                          ]}

    def start(self):
        self.client.start()

    def stop(self):
        self.client.stop()

    def publish(self, value):
        message = self.__message
        message["e"][0]["v"] = value
        message["e"][0]["t"] = str(time.time())
        self.client.myPublish(self.topic, message)
    
if __name__ == "__main__":
    conf = json.load(open("settings.json"))
    broker = conf["broker"]
    port = conf["port"]

    myPubl = myPublisher("myPublisher", "IoT/nico/exercise_4", broker, port)    
    myPubl.start()

    #[-25, 40] Nominal
    #[41, 70] Warning
    #[71, 100] Danger

    print("What range do you want to send?")
    print("n - Nominal [-25 ; 40]")
    print("w - Warning [41 ; 70]")
    print("d - Danger [71 ; 100]\n")
    cmd = input()
    if cmd == "n":
        a = -25
        b = 40
    elif cmd == "w":
        a = 41
        b = 70
    elif cmd == "d":
        a = 71
        b = 100
    else:
        a = -25
        b = 100

    for i in range(24):
        myPubl.publish(random.randint(a, b))
        time.sleep(5)
    myPubl.stop()