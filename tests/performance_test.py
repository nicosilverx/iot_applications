import time

if __name__=="__main__":
    start = time.time()
    #print(start)
    a = 0
    for i in range(10000):
        a += i
    stop = time.time()
    #print(stop)
    delta = stop - start
    print(f"{delta}")