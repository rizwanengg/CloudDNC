import threading
from Launch import MainScreen
import time
class myThread (threading.Thread,MainScreen):

   def __init__(self, fname,ser, fileptr):
      threading.Thread.__init__(self)
      self.tname = fname
      self.ser = ser
      self.fileptr = fileptr

   def run(self):
      print ("Starting " + self.tname)
      # Get lock to synchronize threads


      threadLock.acquire()
      self.sendFile1(self.ser, self.fileptr)
      # Free lock to release next thread
      threadLock.release()


def runMyThread(fname,ser, fileptr):

    threads = []
    # Create new threads & Start new Threads
    x = "temp.txt"
    y = myThread(fname,ser, fileptr)
    y.start()
    # Add threads to thread list
    threads.append(y)
    # Wait for all threads to complete
    y.join()
    print("Exiting Main Thread")

threadLock = threading.Lock()
runMyThread("fname","ser", "fileptr")
