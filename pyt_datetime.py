from datetime import datetime
import time


print(datetime)
print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().hour)

print(datetime.now().strftime('%H:%M:%S'))

time.sleep(1)
print(time)
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))