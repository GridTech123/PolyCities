from Tkinter import *
import os
import pickle

def start():
    v_str = v.get()
    v2_str = v2.get()
    if v2_str == 1:
        pickle_out = open('devMode.pcr', 'w')
        pickle.dump('safeMode', pickle_out)
        pickle_out.close()
        os.startfile('Poly_Cities.py')
    else:
        if v_str == 0:
            pickle_out = open('devMode.pcr', 'w')
            pickle.dump(False, pickle_out)
            pickle_out.close()
            os.startfile('Poly_Cities.py')
        if v_str == 1:
            pickle_out = open('devMode.pcr', 'w')
            pickle.dump(True, pickle_out)
            pickle_out.close()
            os.startfile('Poly_Cities.py')

app = Tk()
app.title('Poly Cities Launcher')
app.geometry('500x100')

logbutton = Button(app, text = 'Play', width = 60, command = start)
logbutton.pack()

v = IntVar()
check = Checkbutton(app, text = 'DevMode', variable=v).pack()

v2 = IntVar()
check = Checkbutton(app, text = 'SafeMode', variable=v2).pack()

app.mainloop()
