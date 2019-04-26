from tkinter import *

root = Tk()
root.geometry('300x300')

l = Label(root, text="CMfind")
l.pack(side=TOP)

mb = Menubutton(root, text="Import Text")
mb.menu = Menu(mb)
mb["menu"] = mb.menu

mb.menu.add_command(label="Select File 1", command=lambda: print("This is option 1"))
mb.menu.add_command(label="Select File 2", command=lambda: print("This is option 2"))

mb.pack()

#c = Canvas(root, height=250, width=300, bg="blue")

#l = c.create_line(5,5,200,200, width=10)

#o = c.create_oval(20,20,100,100, fill="red")

#arc = c.create_arc(10,50,240,210, extent=150, fill="red")

#r = c.create_rectangle(20,20,100,100, fill="blue")

#c.pack()

def buttonFunction():
    print("Welcome to CMfind")

b = Button(root, text="Import Text!", command=buttonFunction)
b.pack(side=LEFT)

b2 = Button(root, text="Find all the Metaphors!", command=buttonFunction)
b2.pack(side=RIGHT)

root.mainloop()
