# import threading
# import time
# def print_n():
    # for i in range(1,10):
        # time.sleep(3)
        # print(i)
# 
# 
# def print_l():
    # for i in 'abcde':
        # time.sleep(3)
        # print(i)
        # 
#t1=threading.Thread(target=print_n)
#t2=threading.Thread(target=print_l)
# 
# time_now=time.time()
# print_l()
# print_n()
#t1.start()
#t2.start()
#t1.join()
#t2.join()
# time_diff=time.time()-time_now
# print(time_diff)

## THREAD POOL EXECTUOR

from concurrent.futures import ThreadPoolExecutor
import time
numbers=[1,2,3,4,5,67,8,9,10,11,2,34,5,76]

def printI(numbers):
    
    for i in numbers:
        time.sleep(2)
        print(i)

with ThreadPoolExecutor(max_workers=4) as executor:
    results=executor.map(printI,numbers)

for i in results:
    print(i)
