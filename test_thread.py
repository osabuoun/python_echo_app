from threading import Thread
import sys, time, os

value = set()
def thread1(value):
	print("Thread 1 - started")
	for x in range(1,10):
		time.sleep(1)
		print("thread 1 " + str(x) + " - value : " + str(value))
		value.add("th1-" + str(x)) 
	print("Thread 1 - Finished")

def thread2(value):
	print("Thread 2 - started")
	for x in range(1,5):
		time.sleep(1)
		print("thread 2 " + str(x) + " - value : " + str(value))
		value.add("th2-" + str(x)) 

	print("Thread 1 - Finished")
	sys.exit(0)
	for x in range(1,5):
		time.sleep(1)
		print("thread 2 - Phase 2 : " + str(x))

if __name__ == '__main__':
    thread1_thread = Thread(target = thread1, args = (value,))
    thread1_thread.start()
    thread2_thread = Thread(target = thread2, args = (value,))
    thread2_thread.start()
