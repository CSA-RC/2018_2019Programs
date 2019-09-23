"""
    QuickLunch version 1.0.0 allows users to order food from a menu
    and write the order to a text file
    Copyright (C) 2018  Ryan I Callahan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from tkinter import *
from tkinter import ttk

root = Tk()

class App:

    def __init__(self):
        # Variable List
        self.drink = IntVar()
        self.foodlist = ["Sandwich", "Pizza", "Chicken Nuggets", "Chicken", "Tofu",
                         "Gluten/Soy/Shellfish Free Clam Chowder"]
        self.payment = ["Credit", "Check", "Cash"]
        self.price = DoubleVar()
        self.price.set(0.00)
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.id = StringVar()
        self.progress = IntVar()
        self.progress.set(0)
        self.dcount = 1
        self.fcount = 1
        self.pcount = 1
        self.ecount = 1
        self.wcount = 1


        # Progress Bar
        self.p = ttk.Progressbar(root, orient=VERTICAL, length=200, mode='determinate', value=self.progress.get())
        self.p.grid(column=4, row=2)


        # Menu Initialization
        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.helpmenu.add_command(label="Instructions", command=self.instructions)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        root.config(menu=self.menubar)


        # Drink Menu
        self.dframe = Frame(root)
        self.dframe.grid(column=3, row=2)

        drinks = Label(self.dframe, text="Drinks:")
        drinks.grid(row=0, sticky='w')

        self.soda = Radiobutton(self.dframe, text="Soda", var=self.drink, value=1)
        self.soda.grid(row=1, sticky="w")

        self.tea = Radiobutton(self.dframe, text="Tea", var=self.drink, value=2)
        self.tea.grid(row=2, sticky="w")

        self.milk = Radiobutton(self.dframe, text="Milk", var=self.drink, value=3)
        self.milk.grid(row=3, sticky="w")

        self.juice = Radiobutton(self.dframe, text="Juice", var=self.drink, value=4)
        self.juice.grid(row=4, sticky="w")

        self.water = Radiobutton(self.dframe, text="Bottled Water", var=self.drink, value=5)
        self.water.grid(row=5, sticky="w")

        self.none = Radiobutton(self.dframe, text="None", var=self.drink, value=6)
        self.none.grid(row=6, sticky="w")

        self.soda.bind('<ButtonRelease-1>', self.dprog)
        self.tea.bind('<ButtonRelease-1>', self.dprog)
        self.milk.bind('<ButtonRelease-1>', self.dprog)
        self.juice.bind('<ButtonRelease-1>', self.dprog)
        self.water.bind('<ButtonRelease-1>', self.dprog)
        self.none.bind('<ButtonRelease-1>', self.dprog)


        # Food Menu
        self.fframe = Frame(root)
        self.fframe.grid(column=1, row=2, columnspan=2)

        entrees = Label(self.fframe, text="Entrees:")
        entrees.grid(row=0, sticky='w')

        self.foodbox = Listbox(self.fframe, height=6, width=36, listvariable=self.foodlist, selectmode=SINGLE)
        for item in self.foodlist:
            self.foodbox.insert('end', '%s' % item)
        self.foodbox.grid(row=1)
        self.foodbox.bind('<FocusIn>', self.fprog)

        # make pretty
        spaceframe = Frame(root)
        spaceframe.grid(row=3, column=1)
        space=Label(spaceframe, text="   ")
        space.pack()

        # Checkout Menu
        self.cframe = Frame(root)
        self.cframe.grid(column=1, row=3, columnspan=3)

        self.paybox = ttk.Combobox(self.cframe, width=13, state='readonly', value=self.payment)
        self.paybox.grid(row=2, column=0, sticky='w')
        self.paybox.bind('<<ComboboxSelected>>', self.paymentmethod)

        spacer = Label(self.cframe, text="Payment Method:")
        spacer.grid(row=1, column=0)

        self.day = Spinbox(self.cframe, state='readonly', wrap=True, width=11, values=self.days)
        self.day.grid(row=0, sticky='w')
        self.day.bind('<Leave>', self.wprog)

        elabel = Label(self.cframe, text="  Employee ID:")
        elabel.grid(row=2, column=1, sticky='e')

        self.employeeid = Entry(self.cframe, width=13, textvar=self.id)
        self.employeeid.grid(row=2, column=2, sticky='w')
        self.employeeid.bind('<FocusIn>', self.eprog)

        self.calc = Button(self.cframe, text="Calculate", command=self.calculate)
        self.calc.grid(row=3, column=0, sticky='e')

        self.check = Button(self.cframe, text="Check Out", state='disabled', command=self.checkout)
        self.check.grid(row=3, column=1)

        self.pricelabel = Label(self.cframe, text=("Price: $%s" % self.price.get()))
        self.pricelabel.grid(column=2, row=3)

    def paymentmethod(self, x):
        self.method = self.paybox.get()
        self.pprog(x)

    def calculate(self):
        self.price.set(0.00)
        food = self.foodbox.curselection()
        if self.drink.get() == 1:
            self.price.set(self.price.get() + 1.00)
        if self.drink.get() == 2:
            self.price.set(self.price.get() + 1.00)
        if self.drink.get() == 3:
            self.price.set(self.price.get() + .75)
        if self.drink.get() == 4:
            self.price.set(self.price.get() + 1.25)
        if self.drink.get() == 5:
            self.price.set(self.price.get() + 1.00)

        if food == (0,):
            self.price.set(self.price.get() + 3.00)
        if food == (1,):
            self.price.set(self.price.get() + 4.00)
        if food == (2,):
            self.price.set(self.price.get() + 3.75)
        if food == (3,):
            self.price.set(self.price.get() + 4.00)
        if food == (4,):
            self.price.set(self.price.get() + 15.00)
        if food == (5,):
            self.price.set(self.price.get() + 20.00)

        self.price.set(round((self.price.get()*.0825), 2)+self.price.get())

        self.pricelabel.config(text=("Price: $%s" % self.price.get()))

    def checkout(self):
        self.calculate()
        bill = open("purchasehistory.txt", "a")
        bill.write("\n\n\nNew Purchase\n\nEmployee ID: %s\nPrice Total: %s" % (self.employeeid.get(), self.price.get()))
        bill.close()

    def about(self):
        abt = Toplevel()
        abt.geometry('180x150')
        abt.title("About")
        abtmsg = Message(abt,
                         text="Made by Ryan Callahan\n\n"
                              "This is a food menu program used to "
                              "determine the price of an order from a restaurant"
                              "\n\nVersion 1.0.0")
        abtmsg.pack()
        close = Button(abt, text="Close", command=abt.destroy)
        close.pack()

    def instructions(self):
        ins = Toplevel()
        ins.geometry('480x300')
        ins.title("Instructions")
        insmsg = Message(ins,
                         text="Fill out all parameters and hit calculate to see total price (with tax) or hit check out to finish the order.")
        insmsg.pack()
        close = Button(ins, text="Close", command=ins.destroy)
        close.pack()



    def dprog(self, x):
        if self.dcount==1:
            self.progress.set(self.progress.get() + 20)
            self.p.config(value = self.progress.get())
            self.dcount=0
            if self.progress.get() == 100:
                self.check.config(state='normal')
        else:
            pass

    def fprog(self, x):
        if self.fcount==1:
            self.progress.set(self.progress.get() + 20)
            self.p.config(value = self.progress.get())
            self.fcount=0
            if self.progress.get() == 100:
                self.check.config(state='normal')
        else:
            pass

    def pprog(self, x):
        if self.pcount==1:
            self.progress.set(self.progress.get() + 20)
            self.p.config(value = self.progress.get())
            self.pcount=0
            if self.progress.get() == 100:
                self.check.config(state='normal')
        else:
            pass

    def eprog(self, x):
        if self.ecount==1:
            self.progress.set(self.progress.get() + 20)
            self.p.config(value = self.progress.get())
            self.ecount=0
            if self.progress.get() == 100:
                self.check.config(state='normal')
        else:
            pass

    def wprog(self, x):
        if self.wcount==1:
            self.progress.set(self.progress.get() + 20)
            self.p.config(value = self.progress.get())
            self.wcount=0
            if self.progress.get() == 100:
                self.check.config(state='normal')
        else:
            pass





app = App()
root.mainloop()