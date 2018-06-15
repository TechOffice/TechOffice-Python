import wx
import threading
import atexit

def disable_asserts():
    import wx
    wx.DisableAsserts()

atexit.register(disable_asserts)

class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		import wx 
		app = wx.App(False) 
		frame = wx.Frame(None,wx.ID_ANY,"Hello") 
		frame.Show(True) 
		app.MainLoop()
		
		
t = myThread();
t.start();

# exec(open('020-HelloWorldCommand.py').read());