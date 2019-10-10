from tkinter import *
root=Tk()
root.geometry("500x500")
root.title('Сложение двух чисел')

def Summ_find():
    a = EntryA.get()
    a = float(a)
    b = EntryB.get()
    b = float(b)
    result = str(a + b)
    EntryC.delete(0, END)
    EntryC.insert(0, result)

Label(root,text='Первое число').pack()
EntryA=Entry(root,width=10,font='Arial 16')
EntryA.pack()

Label(root,text='Второе число').pack()
EntryB=Entry(root,width=10,font='Arial 16')
EntryB.pack()

EntryC=Entry(root,width=20,font='Arial 16')
EntryC.pack()

but=Button(root,text='Сумма')
but = Button(root, text='Сумма', command=Summ_find)
but.pack()

root.mainloop()
