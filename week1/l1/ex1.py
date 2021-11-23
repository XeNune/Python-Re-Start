import tkinter
from tkinter import *
frame = tkinter.Tk()
frame.title('Список покупочек чееек')
frame.geometry("1080x720")
#задания для самостоятельного выполнения
name = 'задания для самостоятельного выполнения'
print(name)
testo = 50
rice = 100
wishproduct = input('Что хотите купить?')
buylist = 'Макароны ' + str(testo+rice) + 'гр.'
print(buylist, wishproduct, sep='и ', end='')

text1 = Label(frame, text='huy', font=('Times New Roman', 50))
text1.grid()
frame.mainloop()
