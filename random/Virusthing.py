from tkinter import *
import time

root = Tk()

def ah():
    for x in range(0, 100):
        t = Toplevel()
        m = Message(t, text="You have a virus")
        m.pack()
        time.sleep(1)

b = Button(text="DO NOT PRESS", command=ah)
b.pack()

root.mainloop()