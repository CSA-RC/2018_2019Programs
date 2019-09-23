"""
    employeelog version 1.0.0 allows users to log their name
    and time for their employer to see
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
import time

root = Tk()

class App:

    def __init__(self):
        self.timein = StringVar()
        self.bigmonths = ["January", "March", "May", "July", "August", "October", "December"]
        self.daylist = []
        self.name = StringVar()
        self.nameb = Entry(root, width=15, textvar=self.name)
        self.nameb.grid(column=2, row=0)

        self.months = Spinbox(root, state='readonly', wrap=True, width=7, values=(
        "January", "February", "March", "April", "May",
        "June", "July", "August", "September", "October", "November",
        "December"))
        self.months.grid(column=1, row=1)

        for x in range(1, 31):
            self.daylist.append(x)
        self.days = Spinbox(root, state='readonly', wrap=True, width=5, values=self.daylist)
        self.days.grid(column=2, row=1)

        self.yearlist = []
        for x in range(0, 31):
            self.yearlist.append((str(2000+x)))
        self.years = Spinbox(root, state='readonly', wrap=True, width=5, values=self.yearlist)
        self.years.grid(column=3, row=1)

        self.clockinb = Button(root, text="Clock In", command=self.clockin)
        self.clockinb.grid(column=1, row=2)

        self.clockoutb = Button(root, text="Clock Out", command=self.clockout)
        self.clockoutb.grid(column=2, row=2)

        self.clock = Message(root, text=time.asctime())
        self.clock.grid(columnspan=3, column=6, row=6)

        root.after(1, self.clockloop)

        self.months.bind("<Leave>", self.daychange)

    def clockloop(self):
        if self.clock.cget("text") != time.asctime():
            self.clock.config(text=time.asctime())
        root.after(1, self.clockloop)

    def daychange(self, event):
        if self.months.get() in self.bigmonths:
            self.days.config(values=list(range(1, 32)))
        if self.months.get() == "February":
            self.days.config(values=list(range(1, 29)))
        else:
            self.days.config(values=list(range(1, 31)))

    def clockin(self):
        self.timein.set((self.days.get() + self.months.get() + self.years.get()))
        print(self.timein.get())

    def clockout(self):
        pass

app = App()
root.geometry('500x500')
root.mainloop()