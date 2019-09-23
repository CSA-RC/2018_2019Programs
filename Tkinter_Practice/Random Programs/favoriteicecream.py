from tkinter import *

root = Tk()

class App:

    def __init__(self, master):

        master.config(width=245, height=180)
        master.propagate(0)
        master.title("Checkbuttons!")

        labelframe = Frame(master, width=130, height=20)
        labelframe.pack_propagate(0)
        labelframe.pack()

        buttframe = Frame(master, width=100, height=120)
        buttframe.pack_propagate(0)
        buttframe.pack()

        doneframe = Frame(master, width=100, height=25)
        doneframe.pack_propagate(0)
        doneframe.pack()

        label = Label(labelframe, text="Favorite Ice Cream")
        label.pack(fill=BOTH, expand=1)

        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()

        self.state = 'disabled'

        self.vanilla = 0
        self.strawberry = 0
        self.chocolate = 0
        self.mintchip =  0
        self.rockyroad = 0

        self.b1 = Checkbutton(buttframe, text="Vanilla", variable=self.var1, command=self.submitcheck)
        self.b1.pack()
        self.b2 = Checkbutton(buttframe, text="Strawberry", variable=self.var2, command=self.submitcheck)
        self.b2.pack()
        self.b3 = Checkbutton(buttframe, text="Chocolate", variable=self.var3, command=self.submitcheck)
        self.b3.pack()
        self.b4 = Checkbutton(buttframe, text="Mint Chip", variable=self.var4, command=self.submitcheck)
        self.b4.pack()
        self.b5 = Checkbutton(buttframe, text="Rocky Road", variable=self.var5, command=self.submitcheck)
        self.b5.pack()

        self.submitbutton = Button(doneframe, text="SUBMIT", state=self.state, command=self.submit)
        self.submitbutton.pack(fill='both', expand=1, side='left')

        self.clearbutton = Button(doneframe, text="CLEAR", command=self.clear)
        self.clearbutton.pack(fill='both', expand=1, side='right')

    def submitcheck(self):
            self.submitbutton.config(state="normal")

    def submit(self):
        self.submitbutton.config(state='disabled')

        if self.var1.get() == 1:
            self.vanilla+=1

        if self.var2.get() == 1:
            self.strawberry+=1

        if self.var3.get() == 1:
            self.chocolate+=1

        if self.var4.get() == 1:
            self.mintchip+=1

        if self.var5.get() == 1:
            self.rockyroad+=1

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.store()

    def clear(self):
        self.submitbutton.config(state='disabled')
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)

    def store(self):
        try:
            favorite_ice_cream_txt = open("favorite_ice_cream.txt", "w")
            favorite_ice_cream_txt.write("Vanilla \n %s \n\n Strawberry \n %s \n\n Chocolate \n %s \n\n Mint Chip \n %s \n\n Rocky Road \n %s \n\n " % (str(self.vanilla), str(self.strawberry), str(self.chocolate), str(self.mintchip), str(self.rockyroad)))
            favorite_ice_cream_txt.close()
        except FileNotFoundError:
            favorite_ice_cream_txt = open("favorite_ice_cream.txt", "w")
            favorite_ice_cream_txt.write("Vanilla \n %s \n\n Strawberry \n %s \n\n Chocolate \n %s \n\n Mint Chip \n %s \n\n Rocky Road \n %s \n\n " % (str(self.vanilla), str(self.strawberry), str(self.chocolate), str(self.mintchip), str(self.rockyroad)))
            favorite_ice_cream_txt.close()


app = App(root)
root.mainloop()