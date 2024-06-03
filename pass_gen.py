from tkinter import *
import pyperclip
import random, string

root = Tk()
root.title('Random Password Generator')
root.geometry('400x400')


heading = Label(root,text = 'Random Password Generator',font = 'arial 15 bold').pack()

pass_label = Label(root,text = 'Password Length',font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_=8,to_=32,textvariable = pass_len).pack()


pass_str = StringVar()
def Generator():
    Password = ''
    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range (pass_len.get()-4):
        Password = Password+ random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    pass_str.set(Password)


Button(root , text = 'Generate' , command=Generator).pack()
Entry(root, textvariable=pass_str).pack()

def copy_pass():
    pyperclip.copy(pass_str.get())
Button(root, text = 'Copy', command=copy_pass).pack()
root.mainloop()