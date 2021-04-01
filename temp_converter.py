# coding: utf-8
import tkinter as tk
from tkinter import ttk
import math


def convert_it(*args):
    numb = float(feet.get())
    result_F.set(float((numb * 1.8) + 32))
    result_K.set(float(numb + 273.15))
    result_Re.set(float(numb * 0.8))
    result_Ro.set(float((numb * 0.525) + 7.5))
    result_Ra.set(float((numb * 1.8) + 491.67))
    result_D.set(float((100 - numb) * 1.5))
    result_H.set(float((numb * 12) / 5))
    result_Da.set(float(((math.log10((float(numb + 273.15)))
                          - math.log10(273.15)) / (math.log10(373.15) - math.log10(273.15))) * 100))
    result_N.set(float((numb * 33) / 100))
    result_L.set(float(numb + 253))
    result_Pl.set(float((1.416784 * (10 ** 32)) + 273.15))


root = tk.Tk()
root.title(f"Конвертер температур")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, font=('Helvetica', 10), width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky='we')

result_F = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_F).grid(column=2, row=2, sticky='we')
result_K = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_K).grid(column=2, row=3, sticky='we')
result_Re = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_Re).grid(column=2, row=4, sticky='we')
result_Ro = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_Ro).grid(column=2, row=5, sticky='we')
result_Ra = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_Ra).grid(column=2, row=6, sticky='we')
result_D = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_D).grid(column=2, row=7, sticky='we')
result_H = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_H).grid(column=2, row=8, sticky='we')
result_Da = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_Da).grid(column=2, row=9, sticky='we')
result_N = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_N).grid(column=2, row=10, sticky='we')
result_L = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_L).grid(column=2, row=11, sticky='we')
result_Pl = tk.StringVar()
ttk.Label(mainframe, font=('Helvetica', 10), textvariable=result_Pl).grid(column=2, row=12, sticky='we')

ttk.Button(mainframe, text=f"Расчёт", command=convert_it).grid(column=1, row=1, sticky='w')

ttk.Label(mainframe, font=('Helvetica', 10), text=f"Цельсий").grid(column=3, row=1, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Эквивалентно:").grid(column=1, row=2, sticky='e')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Фаренгейт").grid(column=3, row=2, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Кельвин").grid(column=3, row=3, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Реомюр").grid(column=3, row=4, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Рёмер").grid(column=3, row=5, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Ранкин").grid(column=3, row=6, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Делиль").grid(column=3, row=7, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Гук").grid(column=3, row=8, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Дальтон").grid(column=3, row=9, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Ньютон").grid(column=3, row=10, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Лейденский градус").grid(column=3, row=11, sticky='w')
ttk.Label(mainframe, font=('Helvetica', 10), text=f"Планк").grid(column=3, row=12, sticky='w')

for i in mainframe.winfo_children():
    i.grid_configure(padx=2, pady=2)

feet_entry.focus()
root.bind("<Return>", convert_it)

root.mainloop()
