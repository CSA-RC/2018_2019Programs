from tkinter import *
root = Tk()

mframe = Frame(width=200, height=200)
mframe.pack()
name = StringVar()
name.set("")

nl = Label(mframe, text="Name:")
nl.grid(column=0, row=0, sticky='nsew')

ne = Entry(mframe, width=15, textvar=name)
ne.grid(column=1, row=0, columnspan=2, sticky="nsew")
ne.columnconfigure(0, weight=1)

submitbutton = Button(mframe, text="SUBMIT")
submitbutton.grid(column=1, row=1, sticky="nsew")
submitbutton.columnconfigure(0, weight=1)

clearbutton = Button(mframe, text="CLEAR")
clearbutton.grid(column=0, row=1, stick="nsew")
clearbutton.columnconfigure(0, weight=1)

cancelbutton = Button(mframe, text="CANCEL")
cancelbutton.grid(column=2, row=1, stick="nsew")
cancelbutton.columnconfigure(0, weight=1)

root.rowconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.mainloop()