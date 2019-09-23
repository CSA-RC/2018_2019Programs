"""
    writeit version 1.0.0 allows users to write text files
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
        self.input = ''
        self.mframe = Frame(master, width=130, height=200)
        self.mframe.pack()
        self.write = Text(self.mframe, width=20, height=10, wrap='word')
        self.write.pack()
        self.wbutton = Button(self.mframe, text="Write It", command=self.writeit)
        self.wbutton.pack()

    def writeit(self):
        self.input = self.write.get(1.0, END)
        self.txt = open("user_input.txt", "a")
        self.txt.write('\n-------NEW ENTRY-------\n'+self.input+'\n')
        self.write.delete(1.0, END)

app = App(root)
root.geometry('200x200')
root.mainloop()