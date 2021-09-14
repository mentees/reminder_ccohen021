import datetime
import tkinter
import time
from tkinter import messagebox
# tkinter credit: https://stackoverflow.com/questions/177287/alert-boxes-in-python 

def main():
    # Get input
    user_date, user_time, user_task, long_date = user_input()

    # Process
    timer(user_date, user_time, long_date)

    # Output
    # Hide the main tkinter window
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo("Reminder", user_task)
    
# Input
def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        print("Date format is incorrect. The correct format is YYYY-MM-DD. Please try again.")
        return False

def validate_time(time_text):
    try:
        datetime.datetime.strptime(time_text, '%H:%M')
        return True
    except ValueError:
        print("Time format is incorrect. The correct format is HH:MM. Please try again.")
        return False    

def user_input():
    # Input and validation
    user_task = input("Enter a task to be reminded of: ")
    while True:
        user_date = input("Enter a date (YYYY-MM-DD): ")
        date_flag = validate_date(user_date)
        if date_flag:
            long_date = user_date
            user_date = datetime.datetime.strptime(user_date, "%Y-%m-%d") 
            today = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
            #if date_flag:
            if today <= user_date:
                #if all is fine, you start the time
                while True:
                    user_time = input("Enter a time (HH:MM in 24-hour format): ")
                    date_flag = validate_time(user_time)
                    if date_flag:
                        temp = user_time
                        user_time = datetime.datetime.strptime(user_time, "%H:%M")
                        now = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
                        if today == user_date:
                            if now < user_time:
                                long_date = long_date + " " + temp + ":00"
                                break
                            else:
                                print("The time has already passed. Enter a different time")
                        else:
                            long_date = long_date + " " + temp + ":00"
                            break
                break
            else:
                print("The date has already passed. Try a different date")                

    return user_date, user_time, user_task, long_date

# Process
def timer(user_date, user_time, long_date):    
    # check how much time is left
    user_long_date = datetime.datetime.strptime(long_date, "%Y-%m-%d %H:%M:%S")
    current_long_date = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    time_left = (user_long_date - current_long_date).seconds
    time.sleep(time_left)


    # check date
    while True:
        today = datetime.datetime.strptime(datetime.date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
        if today == user_date:
            break

    # Check time
    while True:
        now = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M"), "%H:%M")
        if now == user_time:
            break

main()