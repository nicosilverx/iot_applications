import threading, numpy, time
    
N_CUSTOMERS=30
N_DESKS=5
CASH_DESK=[i for i in range(N_DESKS) ]
CUSTOMERS=[numpy.random.poisson(5) for i in range(N_CUSTOMERS)]

SERVED=dict([[i,0] for i in range(N_DESKS) ])
BUSY=dict([[i,0] for i in range(N_DESKS) ])

TOTAL_SERVING_TIME=0

class Customer(threading.Thread):
    def __init__(self, customerID, servingTime, semaphore):
        threading.Thread.__init__(self)
        self.servingTime = servingTime
        self.customerID = customerID
        self.semaphore = semaphore

    def run(self):
        self.semaphore.acquire()

        servedBy = CASH_DESK.pop()
        SERVED[servedBy] += 1
        BUSY[servedBy] += self.servingTime

        time.sleep(self.servingTime)
        CASH_DESK.append(servedBy)
        self.semaphore.release()

if __name__ == "__main__":
    customers_list = []        
    semaphore = threading.Semaphore(N_DESKS)

    for i in range(N_CUSTOMERS):
        customers_list.append(Customer(i, CUSTOMERS[i], semaphore))

    start = time.time()

    for c in customers_list:
        c.start()
    for c in customers_list:
        c.join()        

    stop = time.time()        
    TOTAL_SERVING_TIME = stop-start
    print(f"Total serving time: {TOTAL_SERVING_TIME} s")
    print(SERVED)
    AVG_TIME=(BUSY[i]/SERVED[i] for i in range(N_DESKS))
    print(AVG_TIME)