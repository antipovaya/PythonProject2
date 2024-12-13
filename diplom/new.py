from tkinter import *
from tkinter import messagebox
import calculations


class Window:
    def __init__(self, master):
        self.master = master

        self.Main = Frame(self.master)

        self.L1 = Label(self.Main, text="Введите дату рождения кандидата:")
        self.L1.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

        # date_user
        self.L2 = Label(self.Main, text="День: ")
        self.L2.grid(row=1, column=0, padx=5, pady=5)

        self.E1 = Entry(self.Main, width=30)
        self.E1.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

        # month_user
        self.L3 = Label(self.Main, text="Месяц: ")
        self.L3.grid(row=2, column=0, padx=5, pady=5)

        self.E2 = Entry(self.Main, width=30)
        self.E2.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

        # year_user
        self.L4 = Label(self.Main, text="Год: ")
        self.L4.grid(row=3, column=0, padx=5, pady=5)

        self.E3 = Entry(self.Main, width=30)
        self.E3.grid(row=3, column=1, padx=5, pady=5, columnspan=3)

        # Buttons
        self.B1 = Button(self.Main, text="Рассчитать", command=self.astro_calculation)
        self.B1.grid(row=4, column=2, padx=5, pady=5, sticky="e")

        # self.B2 = Button(self.Main, text="Clear", command=self.clear)
        # self.B2.grid(row=4, column=3, padx=5, pady=5)

        self.Main.pack(padx=5, pady=5)

    def clear(self):
        self.E1.delete(0, 'end')
        self.E2.delete(0, 'end')

    def verify(self):
        user = self.E1.get()
        password = self.E2.get()



    def astro_calculation(self):
        date_user = self.E1.get()
        month_user = self.E2.get()
        year_user = self.E3.get()
        user = {}
        user['date'] = str(year_user) + '-' + str(month_user) + '-' + str(date_user)
        calculations.sun_user(user)
        calculations.mercury_user(user)
        calculations.jupiter_user(user)
        calculations.saturn_user(user)
        print(user)




        # file = open("Accounts.txt", "r")
        #
        # for line in file:
        #     temp = line.strip("\n").split(",")
        #
        #     if user == temp[0] and password == temp[1]:
        #         print("Your Login Credentials have been Verified")
        #         return 1
        #
        # prompt = messagebox.showerror(title="Error!", message="Incorrect Login Details")
        # return 0


root = Tk()
window = Window(root)
root.title("Добро пожаловать в приложение HR Assistant")
root.geometry('480x180')
root.mainloop()