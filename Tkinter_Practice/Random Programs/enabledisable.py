from tkinter import *

root = Tk()


class App:
    def __init__(self, master):

        buttframe = Frame(master, width=100, height=200)
        buttframe.pack_propagate(0)
        buttframe.pack()

        self.ok = Button(buttframe, text="OK", state='normal', command=self.okd)
        self.ok.pack(fill=BOTH, expand=1)

        self.notok = Button(buttframe, text="NOT OK", state='disabled', command=self.notokd)
        self.notok.pack(fill=BOTH, expand=1)

    def notokd(self):
        self.notok.config(state='disabled')
        self.ok.config(state='normal')

    def okd(self):
        self.ok.config(state='disabled')
        self.notok.config(state='normal')

app = App(root)

root.mainloop()