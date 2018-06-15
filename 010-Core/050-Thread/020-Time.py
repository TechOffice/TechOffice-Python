import _thread
import time

def test():
	count = 0;
	while count < 5:
		count=count + 1
		print(1)
		time.sleep(5)

_thread.start_new_thread(test, ())