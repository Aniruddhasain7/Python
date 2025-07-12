from tkinter import *
import time

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="#000")
root.resizable(False, False)

heading = Label(root, text="Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

Label(root, font=("arial", 15, "bold"), text="current time:", bg="papaya whip").place(x=65, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=190, y=70)
clock()

hrs = StringVar(value="00")
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)

mins = StringVar(value="00")
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)

sec = StringVar(value="00")
Entry(root, textvariable=sec, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)

Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="min", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="sec", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)

def countdown(times):
    if times >= 0:
        minute, second = divmod(times, 60)
        hour = minute // 60
        minute = minute % 60

        hrs.set(f"{hour:02}")
        mins.set(f"{minute:02}")
        sec.set(f"{second:02}")

        root.after(1000, countdown, times - 1)
    else:
        print("Timer finished!")

def start_timer():
    try:
        total_seconds = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
        countdown(total_seconds)
    except ValueError:
        print("Invalid input!")

button = Button(root, text="Start", command=start_timer, bg="#ea3548", bd=0, fg="#fff", width=20, height=2, font="arial 10 bold")
button.pack(padx=5, pady=40, side=BOTTOM)

root.mainloop()
