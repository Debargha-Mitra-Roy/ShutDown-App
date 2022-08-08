from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -l")


def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")  # Title of the App
st.geometry("500x500")  # Size of the App
st.config(bg="Blue")  # Background color of the App

# Restart Button
r_button = Button(st, text="Restart", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart)
r_button.place(x=150, y=70, height=50, width=200)

# Restart Time Button
rt_button = Button(st, text="Restart Time", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

# Log-Out Button
lg_button = Button(st, text="Log-Out", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

# ShutDown Button
lg_button = Button(st, text="ShutDown", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=shutdown)
lg_button.place(x=150, y=370, height=50, width=200)


st.mainloop()
