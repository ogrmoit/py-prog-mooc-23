# Write your solution here

hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")

if day_of_week == "Sunday":
    hourly_wage = hourly_wage * 2

daily_wages = hourly_wage * hours_worked

print(f"Daily wages: {daily_wages} euros")
