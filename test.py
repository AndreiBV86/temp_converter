# coding: utf-8
from tkinter import *
import math

# main_window = Tk()
# main_window.geometry('750x500')
# main_window.title('Main screen')
main_label = Label(main_window, text='Hello, Python!', font=('Helvetica', 20), fg='SpringGreen3', bg='gray17',
                   relief='groove')
# main_label.pack()
# version_label = Label(main_window, text='Version 1.0', font=('Helvetica', 12), fg='SpringGreen3', bg='gray17',
#                       relief='groove')
# version_label.place(anchor='nw')
# go_button = Button(main_window, text='Бдыщь!', font=('Helvetica', 20), fg='red2', bg='gray17',
#                    relief='groove')
# go_button.place(relx=0.5, rely=0.5, width=130, height=40)
# main_window.mainloop()


result_K = 66
a = math.log10((float(numb + 273.15))
                          - math.log10(273.15)) / (math.log10(373.15) - math.log10(273.15))) * 100
print(a)