import os
import tkinter as tk

root= tk.Tk()
root.title("Zzz..")
canvas1 = tk.Canvas(root, width = 125, height = 215, bg = 'grey20', relief = 'groove')
canvas1.pack()
def sleep1 ():
    os.system('cmd /c "shutdown -s -t 1800"')
def sleep2 ():
    os.system('cmd /c "shutdown -s -t 2700"')
def sleep3 ():
    os.system('cmd /c "shutdown -s -t 3600"')
def sleep4 ():
    os.system('cmd /c "shutdown -s -t 7200"')
def cancel ():
    os.system('cmd /c "shutdown -a"')
button1 = tk.Button(text='30 Minutos', command=sleep1, bg='black', fg='white', font=('helvetica', 12, 'bold'))
button2 = tk.Button(text='45 Minutos', command=sleep2, bg='black', fg='white', font=('helvetica', 12, 'bold'))
button3 = tk.Button(text='1 hora', command=sleep3, bg='black', fg='white', font=('helvetica', 12, 'bold'))
button4 = tk.Button(text='2 horas', command=sleep4, bg='black', fg='white', font=('helvetica', 12, 'bold'))
button5 = tk.Button(text='Cancelar', command=cancel, bg='black', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(65, 30, window=button1)
canvas1.create_window(65, 70, window=button2)
canvas1.create_window(65, 110, window=button3)
canvas1.create_window(65, 150, window=button4)
canvas1.create_window(65, 190, window=button5)
root.mainloop()