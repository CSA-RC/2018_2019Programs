"""
    readit version 1.0.0 allows users to read text files
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

root = Tk()

class App:

    def __init__(self, master):
        self.rtest = True
        self.mframe = Frame(master, width=130, height=200)
        self.mframe.pack()
        self.rbutton = Button(self.mframe, text="Read It", command=self.readit)
        self.rbutton.pack()

    def readit(self):
        if self.rtest == True:
            self.txt = open("test_text.txt", "r")
            self.text = self.txt.read()
            self.msg = Message(self.mframe, text=self.text)
            self.msg.pack()
            self.rtest = False
        else:
            pass


app = App(root)
root.geometry('200x200')
root.mainloop()