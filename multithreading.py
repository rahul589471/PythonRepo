from threading import *;
import time;


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            #time.sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            #time.sleep(1)


h1 = Hello();
h2=Hi();

#h1.run();
#h2.run();

h1.start();
time.sleep(0.2)
h2.start();

# So that main thread will wait for all other threads to finish
h1.join()
h2.join()

print(time.perf_counter());
print("Bye")
