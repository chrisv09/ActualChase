# Test timer
#test
import time
from tkinter import *

root = Tk()

second = StringVar()
timer = Label(textvariable = second, font = ('Times New Roman', 40))
second.set("60")

timer.pack()

for i in range(1, 5):
    second.set("Starting in" + str(5 - i))
    root.update()
    time.sleep(1)

for i in range(0,10):
    # Temporary timer (will use tkinter to display)
    second.set(str(10 - i))
    root.update()
    time.sleep(1)

second.set("0")