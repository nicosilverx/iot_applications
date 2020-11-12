from MyMQTT import *
import json, random, time, numpy

class myPublisher():
    def __init__(self, clientID, topic, broker, port):
        self.client = MyMQTT(clientID, broker, port, self)
        self.topic = topic
        self.status = None
        self.__message = {"bn" : "sensor1",
                          "e" : [
                              {
                                  "n" : "heartrate",
                                  "u" : "bpm",
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

    myPubl = myPublisher("myPublisher", "IoT/nico/exercise_2", broker, port)    
    myPubl.start()

    sensor_values = numpy.random.normal(118, 62, 24)
    for i in range(24):
        myPubl.publish(sensor_values[i])
        time.sleep(5)
    myPubl.stop()