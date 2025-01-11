import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    print(f"sleepnig for {seconds} sec")
    time.sleep(seconds)
    return seconds
t1=threading.Thread(target=func(1))
t2=threading.Thread(target=func(2))
t3=threading.Thread(target=func(4))
time1=time.perf_counter()
t3.start()
t1.start()
t2.start()
time1=time.perf_counter()
#func(1)
#func(5)
#func(2)
time2=time.perf_counter()
print(time2 - time1)


def poolingdemo():
    with ThreadPoolExecutor() as executor:
     future = executor.submit(func(3))
     future = executor.submit(func(2))
     future = executor.submit(func(1))
    print(future.result)

poolingdemo()

l=[3,5,1,2]
with ThreadPoolExecutor() as executor:
  result=executor.map(func,l)
  print(result)