from Tkinter import *
import os
import pickle

def start():
    v_str = v.get()
    v2_str = v2.get()
    v3_str = v3.get()
    if v2_str == 1:
        pickle_out = open('devMode.pcr', 'w')
        pickle.dump('safeMode', pickle_out)
        pickle_out.close()
    else:
        if v_str == 0:
            pickle_out = open('devMode.pcr', 'w')
            pickle.dump(False, pickle_out)
            pickle_out.close()
        if v_str == 1:
            pickle_out = open('devMode.pcr', 'w')
            pickle.dump(True, pickle_out)
            pickle_out.close()
    if v3_str == 1:
        pickle_out = open('visualizations.pcr', 'w')
        pickle.dump(True, pickle_out)
        pickle_out.close()
        os.startfile('Poly_Cities.py')
    else:
        pickle_out = open('visualizations.pcr', 'w')
        pickle.dump(False, pickle_out)
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

v3 = IntVar()
check = Checkbutton(app, text = 'Use R2 with rendering visualizations', variable=v3).pack()

app.mainloop()
