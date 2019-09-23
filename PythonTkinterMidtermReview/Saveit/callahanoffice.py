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
from tkinter import filedialog

root = Tk()

class App:

    def __init__(self, master):
        root.title("WordPad Deluxe")
        self.filename = StringVar()
        self.filename.set("")
        self.rtest = True
        self.wtest = True
        self.input = ''

        self.mframe = Frame(master, width=280, height=280)
        self.mframe.pack()

        self.write = Text(self.mframe, width=1080, height=960, wrap='word')
        self.write.pack()

        """self.wbutton = Button(self.mframe, text="Save", command=self.writeit)
        self.wbutton.pack()

        self.rbutton = Button(self.mframe, text="Open", command=self.readit)
        self.rbutton.pack()"""

        self.menubar = Menu(root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.readit)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_command(label="Save As", command=self.saveas)
        self.filemenu.add_command(label="Exit", command=exit)
        self.filemenu.add_command(label="Clear", command=self.clear)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.helpmenu.add_command(label="Licensing", command=self.license)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        root.config(menu=self.menubar)

    def writeit(self):
        for x in range(0, 5):
            self.i = self.write.get(1.0, END)
            self.input = (self.i)
            self.wtxt = open((self.filename.get() + '.txt'), "w")
            self.wtxt.write(self.input)

    def readit(self):
        self.filename.set(filedialog.askopenfilename())
        try:
            self.write.delete(1.0, END)
            self.txt = open((self.filename.get()), "r")
            self.text = self.txt.read()
            self.write.insert(END, self.text)
        except FileNotFoundError:
            pass

    def clear(self):
        self.write.delete(1.0, END)

    def save(self):
        if self.filename.get() == "":
            self.saveas()
        else:
            self.save2 = Toplevel()
            self.save2.geometry('180x150')
            self.save2.title("Save")
            savemsg = Message(self.save2, text=("Save File As " + self.filename.get() + '.txt'))
            savemsg.pack()
            saveb = Button(self.save2, text="Save", command=self.s2)
            saveb.pack()
            close = Button(self.save2, text="Close", command=self.save2.destroy)
            close.pack()

    def s2(self):
        self.writeit()
        self.save2.destroy()

    def saveas(self):
        self.save = Toplevel()
        self.save.geometry('180x150')
        self.save.title("Save As")
        savemsg = Message(self.save, text="Save File As: ")
        savemsg.pack()
        self.name = Entry(self.save, textvariable=self.filename)
        self.name.pack()
        saveb = Button(self.save, text="Save", command=self.s)
        saveb.pack()
        close = Button(self.save, text="Close", command=self.save.destroy)
        close.pack()

    def s(self):
        self.filename.set(self.name.get())
        self.writeit()
        self.save.destroy()

    """def openas(self):
        self.filename.set(filedialog.askopenfilename())
        self.open = Toplevel()
        self.open.geometry('180x150')
        self.open.title("Open")
        openmsg = Message(self.open, text="Open File: ")
        openmsg.pack()
        self.oname = Entry(self.open, textvariable=self.filename)
        self.oname.pack()
        saveb = Button(self.open, text="Open", command=self.o)
        saveb.pack()
        close = Button(self.open, text="Close", command=self.open.destroy)
        close.pack()

    def o(self):
        self.filename.set(self.oname.get())
        self.readit()
        self.open.destroy()"""

    def about(self):
        abt = Toplevel()
        abt.geometry('180x150')
        abt.title("About")
        abtmsg = Message(abt,
                         text="Made by Ryan Callahan\n\n"
                              "This is a word processing program"
                              " used to input words and save them to a file"
                              ", then display them for the user. "
                              "\n\nVersion 1.0.0")
        abtmsg.pack()
        close = Button(abt, text="Close", command=abt.destroy)
        close.pack()

    def license(self):
        lic = Toplevel()
        lic.geometry('480x300')
        lic.title("Licensing")
        licmsg = Message(lic,
                         text="This program is free software:"
                              " you can redistribute it and/or "
                              "modify it under the terms of the "
                              "GNU General Public License as "
                              "published by the Free Software Foundation,"
                              " either version 3 of the License, "
                              "or (at your option) any later version."
                              "\n\nThis program is distributed in the"
                              " hope that it will be useful, but WITHOUT"
                              " ANY WARRANTY; without even the implied "
                              "warranty of MERCHANTABILITY or FITNESS FOR"
                              " A PARTICULAR PURPOSE. See the GNU General "
                              "Public License for more details.\n\nYou "
                              "should have received a copy of the GNU General "
                              "Public License along with this program. "
                              "If not, see <http://www.gnu.org/licenses/>."
                              "\n#####\nRyan I Callahan\ncallahanoffice.py")
        licmsg.pack()
        close = Button(lic, text="Close", command=lic.destroy)
        close.pack()


app = App(root)
root.geometry('600x400')
root.mainloop()