import threading, time, requests

website_list= ["http://yahoo.com", "http://google.com","http://amazon.com","http://ibm.com", "http://apple.com","https://www.microsoft.com","https://www.youtube.com/" ,"https://www.polito.it/" ,"http://www.wikipedia.org","https://www.reddit.com/","https://www.adobe.com/","https://wordpress.org/","https://github.com/","https://www.google.com/maps/"]

class MyThread(threading.Thread):
    def __init__(self, threadID, website):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.website = website
    def run(self):
        resp = requests.get(self.website)
        print(resp)
            

if __name__ == "__main__":
    thread_list = []
    threadID = 1
    start = time.time()

    for website in website_list:
        thread = MyThread(threadID, website)
        thread_list.append(thread)
        thread.start()
    
    for thread in thread_list:
        thread.join()

    stop = time.time()
    execution_time = stop - start
    
    print(f"Execution time: {execution_time}")