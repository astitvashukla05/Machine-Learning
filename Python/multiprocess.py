import multiprocessing
import time
def printNum():
    for i in range(1,10):
        time.sleep(2)
        print(i)

def printSq():
    for i in range(1,10):
        time.sleep(3)
        print(i*i)

if __name__=='__main__':
 t1=time.time()

 p1=multiprocessing.Process(target=printNum)
 p2=multiprocessing.Process(target=printSq)

 p1.start()
 p2.start()

 p1.join()
 p1.join()

 time_diff=time.time()-t1
 print(time_diff)