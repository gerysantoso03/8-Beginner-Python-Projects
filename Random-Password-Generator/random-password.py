import random 
from tkinter import *
import string
from tkinter.font import Font

def random_password():
    password = []
    for i in range(2):
        aplha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        number = random.choice(string.digits)
        password.append(aplha)
        password.append(symbol)
        password.append(number)
    rand_pass = "".join(str(x) for x in password)
    lbl.config(text = rand_pass)

# Make our GUI 
root = Tk()
root.geometry('350x300')
btn = Button(root, text="Generate your password", command = random_password)
btn.place(relx = 0.5, rely = 0.2, anchor=N)
guiFont = Font(family="TImes New Roman", size=14)
lbl = Label(root, font = guiFont)
lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()