import tkinter
from tkinter import Tk, Button
from tkinter.scrolledtext import ScrolledText

FILE = 'log.txt'

def logfile():
    f = open(FILE, "r")
    text = f.read()
    tex.delete('1.0', tkinter.END)
    tex.insert(tkinter.INSERT,text)
    tex.see(tkinter.END)
    f.close()
    root.after(1000,logfile)

master = Tk()
root = tkinter.Tk()
root.attributes("-topmost",True)
master.withdraw()
root.lift()

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 1.1    
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 20
root.geometry("+%d+%d" % (x, y))
tex = ScrolledText(root)
tex.pack(side="bottom", fill="both", expand=True)
o = Button(root, text="Start monitoring Log file", command = logfile)
o.pack()


tkinter.mainloop()