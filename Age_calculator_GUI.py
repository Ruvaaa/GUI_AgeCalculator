import tkinter as tk
from tkinter import ttk
import datetime 
from dateutil import relativedelta

#Main window
root = tk.Tk()
root.title("AgeCalculator")
root.geometry("350x280")

#First label
label1 = tk.Label(root, text = "Age Calculator", font = ("Arial",26))
label1.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

#Year of Birth data
YearLabel = tk.Label(root, text="Year of birth: ", font = ("Arial",13))
YearLabel.grid(row = 1, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = 'w')

YearEntry = tk.Entry(root, font = ("Arial", 13))
YearEntry.grid(row = 1, column = 1, columnspan = 1, padx = 10, pady = 5, sticky = 'e')

#Month of Birth data
MonthLabel = tk.Label(root, text = "Month of birth: ", font = ("Arial",13))
MonthLabel.grid(row = 2, column = 0, columnspan = 1, padx = 1, pady = 5, sticky = 'w')

MonthEntry = tk.Entry(root, font = ("Arial",13))
MonthEntry.grid(row = 2, column = 1, columnspan = 1, padx = 10, pady= 5, sticky = 'e')

#Day of Birth data
DayLabel = tk.Label(root, text = "Day of birth: ", font = ("Arial", 13))
DayLabel.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 5, sticky = 'w')

DayEntry = tk.Entry(root, font = ("Arial",13))
DayEntry.grid(row = 3, column = 1, columnspan = 1, padx = 10, pady = 5, sticky = 'e')

#Age display
age = tk.Text(root, height = 1, width = 30, font = ("Arial", 13))
age.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 5)

#Function to calculate age

def calculate_age():
    try:
        year = int(YearEntry.get())
        month = int(MonthEntry.get())
        day = int(DayEntry.get())

        today = datetime.date.today()
        birth_date = datetime.date(year, month, day)

        years = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1

        #Months and days before last birthday
        try:
            last_birthday = datetime.date(today.year, birth_date.month, birth_date.day)
        except ValueError:
            # Fix for Feb 29
            last_birthday = datetime.date(today.year, birth_date.month, birth_date.day - 1)

        if last_birthday > today:
            last_birthday = datetime.date(today.year - 1, birth_date.month, birth_date.day)

        delta = today - last_birthday
        months = delta.days //30
        days = delta.days % 30
        
        age_of_birth = (f"{years} years, {months} months and {days} days")

        age.delete(1.0, tk.END)
        age.insert(tk.END, str(age_of_birth))
    except ValueError:
        age.delete(1.0, tk.END)
        age.insert(tk.END, "Invalid input")

#Caluclate age button
calculate_button = ttk.Button(root, text = "Calculate Age", command = calculate_age)
calculate_button.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = 'w')

#Exit button
exit = ttk.Button(root, text = "Exit", command = root.quit)
exit.grid(row = 5, column = 1, padx = 10, pady = 5, sticky = 'e')

#Run the application
root.mainloop() 