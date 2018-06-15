import _thread

def test():
	print(1)
	print(2)

_thread.start_new_thread(test, ())