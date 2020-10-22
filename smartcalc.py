from tkinter import *

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multip(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def floordiv(a,b):
    return a//b

def toThePower(a,b):
    return a**b

def extract_numbers(text):
    l=[]
    for elem in text.split(' '):
        try:
            l.append(float(elem))
        except ValueError:
            pass
    return l



def execute_operation():
    text=textbox.get()
    for word in text.split(' '):
        if word.upper() in operatorDict.keys():
            try:
                l=extract_numbers(text)
                r=operatorDict[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Ops! Something went wrong!')
            finally:
                break
        elif word.upper() not in operatorDict.keys():
                 list.delete(0,END)
                 list.insert(END,'Ops! Something went wrong again!')


operatorDict={'ADD':add,'ADDITION':add,'SUM':add,'SUMMATION':add,'PLUS':add,
              'SUB':subtract,'SUBRACT':subtract,'MINUS':subtract,
              'SQUARE':toThePower,'TO THE POWER':toThePower,'MODULUS':mod,'MOD':mod,'FLOOR':floordiv,
              'DIVISION':div,'DIV':div, 'DIVIDE':div}



win=Tk()
win.geometry('500x300')
win.title('Smart Calc ')
win.configure(bg='pink')


l1=Label(win, text="My name is Pinky ^_^",width=50,padx=2)
l1.place(x=40,y=20)

l1=Label(win, text="What can I do for you?",padx=2)
l1.place(x=160,y=80)

textbox=StringVar()
e1=Entry(win,width=30, textvariable= textbox)
e1.place(x=120,y=160)

b1=Button(win, text='Process',command=execute_operation)
b1.place(x=200,y=190)

list=Listbox(win,width=20,height=3)
list.place(x=160,y=230)


win.mainloop()