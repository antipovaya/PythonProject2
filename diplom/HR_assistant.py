import calculations
from tkinter import *
from tkinter.ttk import Combobox


# def clicked():
    # res = "Привет {}".format(txt.get())
    # lbl.configure(text=res)

window = Tk()
window.title("Добро пожаловать в приложение HR Assistant")
window.geometry('500x250')


date_user = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
month_user = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12]
year_user = [i for i  in range(1950, 2024)]


combobox_date = Combobox(window, values=date_user)
combobox_date.pack(anchor=NW, padx=6, pady=6)
combobox_month = Combobox(window, values=month_user)
combobox_date.pack(anchor=NW, padx=12, pady=12)

# lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
#
# combo = Combobox(window)
# combo['values'] = (1, 2, 3, 4, 5, "Текст")
# combo.current(1)  # установите вариант по умолчанию
# combo.grid(column=0, row=0)
# txt = Entry(combo,width=10)
# txt.grid(column=1, row=0)
# btn = Button(window, text="Клик!", command=clicked)
# btn.grid(column=2, row=0)







window.mainloop()