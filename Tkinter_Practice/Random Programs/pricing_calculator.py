from tkinter import *
from tkinter import ttk
import random as rand
root = Tk()

class App:

    def __init__(self, master):
        mframe = Frame(master, width=500, height=500)
        mframe.pack()

        master.title("Pricing")
        self.bcount = 1
        self.ccount = 1
        self.lcount = 1
        self.price = DoubleVar()
        self.price.set(0.00)
        self.pricet = StringVar(value=("Price: $%d" % self.price.get()))
        self.progress = IntVar()
        self.shipping = ["UPS", "Express", "Ground"]
        self.itemlist = ["Chicken", "Spaghetti", "Marinara", "Water", "Book", "CD", "Car", "Andrew", "Soda", "Computer", "Math", "Dry Erase Marker", "Glue", "Pencil", "Peach"]
        self.itempricelist = dict()
        self.shippricelist = {"UPS": 10.00, "Express": 15.00, "Ground": 5.00}
        for item in self.itemlist:
            self.itempricelist[item] = rand.randint(1, 50)

        self.choicebox = ttk.Combobox(mframe, width=12, state='readonly', value=self.shipping)
        self.choicebox.grid(column=1, row=1, sticky='w')
        self.choicebox.bind('<<ComboboxSelected>>', self.cbox)


        self.itembox = Listbox(mframe, height=10, listvariable=self.itemlist, selectmode=MULTIPLE)
        for item in self.itemlist:
            self.itembox.insert('end', '%s' % item)
        self.itembox.grid(column=1, row=2, sticky='w')
        self.itembox.bind('<FocusIn>', self.pbar2)


        self.notebox = Text(mframe, width=10, height=5, wrap='word')
        self.notebox.grid(column=2, row=2)


        self.l = Label(mframe, text=self.pricet.get())
        self.l.grid(column=1, row=3)


        self.s = ttk.Scrollbar(mframe, orient=VERTICAL, command=self.itembox.yview)
        self.s.grid(column=0, row=2, sticky='nse')
        self.itembox.configure(yscrollcommand=self.s.set)


        self.p = ttk.Progressbar(mframe, orient=VERTICAL, length=200, mode='determinate', value=self.progress.get())
        self.p.grid(column=3, row=2)


        self.calculate = Button(mframe, text="SUBMIT", command=self.calc)
        self.calculate.grid(column=2, row=3)


        self.clearb = Button(mframe, text="CLEAR", command=self.clear)
        self.clearb.grid(column=3, row=3)

    def cbox(self, x):
        self.pbar()
        self.price.set(self.cbox)

    def lbox(self):
        self.pbar2()

    def bbox(self):
        self.pbar3()

    def pbar(self):
        if self.ccount==1:
            self.progress.set(self.progress.get() + 33)
            self.p.config(value = self.progress.get())
            self.ccount=0
        else:
            pass

    def pbar2(self, x):
        if self.lcount==1:
            self.progress.set(self.progress.get() + 33)
            self.p.config(value = self.progress.get())
            self.lcount=0
        else:
            pass

    def pbar3(self):
        if self.bcount==1:
            self.progress.set(self.progress.get() + 33)
            self.p.config(value = self.progress.get())
            self.bcount=0
        else:
            pass


    def calc(self):
        self.pbar3()

    def clear(self):
        self.bcount=0
        self.lcount=0
        self.ccount=0
        self.progress.set(0)
        self.p.config(value=self.progress.get())
        self.choicebox.set("")
        self.itembox.selection_clear(0, END)
        self.notebox.delete(1.0, END)






app = App(root)
root.mainloop()