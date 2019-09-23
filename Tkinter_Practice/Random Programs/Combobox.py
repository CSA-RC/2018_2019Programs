from tkinter import *
from tkinter import ttk
root = Tk()

class App:

    def __init__(self, master):
        masterframe = Frame(master, width=300, height=100)
        masterframe.pack()

        labeltop = Label(masterframe, text="Choice")
        labeltop.grid(row=0, column=0)

        self.labelchoice = Label(masterframe, text='')
        self.labelchoice.grid(column=0, row=3)

        self.choices = ["Blue", "Red", "Green", "Purple", "Yellow"]

        self.choicebox = ttk.Combobox(masterframe, state='readonly', value=self.choices)
        self.choicebox.grid(column=0, row=1)
        self.choicebox.bind('<<ComboboxSelected>>', self.labelupdate)

    def labelupdate(self, x):
        self.labelchoice.config(text=(self.choicebox.get()))




app = App(root)
root.geometry('300x100')
root.mainloop()
