# importing only those functions which
# are needed
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button

# time function used to calculate time
from time import time

# creating tkinter window
root = Tk()

button = Button(root, text = 'Geeks')
button.pack(side = TOP, pady = 5)

logging.info('Running...')
# Calculating starting time
start = time()

# in after method 5000 milliseconds
# is passed i.e after 5 seconds
# main window i.e root window will
# get destroyed
root.after(5000, root.destroy)

mainloop()

# calculating end time
end = time()
logging.info('Destroyed after % d seconds' % (end-start))

def doit():
    logging.info("5000 msec passed")

    root.after(5000, doit)