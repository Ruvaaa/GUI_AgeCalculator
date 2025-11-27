import tkinter as tk
from tkinter import ttk

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
    current_year = 2025
    current_month = 11
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    current_day = 27
    try:
        year_of_birth = int(YearEntry.get())
        month_of_birth = str(MonthEntry.get())
        month_index = (month.index(month_of_birth)) + 1
        day_of_birth = int(DayEntry.get())

        years = current_year - year_of_birth
        months = current_month - month_index
        days = current_day - day_of_birth

        days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

        if days < 0:
            months -=1
            days += days_in_month[current_month -2]

        if months < 0:
            years -=1
            months += 12

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