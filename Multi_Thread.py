#Multi Thread = Multithreading refers to concurrently executing multiple threads by rapidly switching the control of the CPU between threads.

from time import sleep
from threading import *

class Hello(Thread):
	def run(self):
		for i in range(50):
			print("hello")
			sleep(1)

class Hi(Thread):
	def run(self):
		for i in range(50):
			print("Hi")
			sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()