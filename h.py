from tkinter import*
import random
otvet=['Да', 'Нет', 'Может быть']
root=Tk()
root.title('Шар предсказаний')
root.geometry('500x400')
b=Button(root, text='встряхнуть', bg='white', command=click).place(relx=0.7, rely=0,7)
b.pack
a=Label(root, text=(random.randit(otvet)), width=15, bg='black', fg='cyan', font=consolas).place(relx=0.5, rely=0.5)
a.pack
root.mainloop()
