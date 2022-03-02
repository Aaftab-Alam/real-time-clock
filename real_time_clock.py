from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Real time clock")
# window.geometry("250x100")
window.configure(bg="black")
window.resizable(True, True)

time_label = Label(window, bg="black", fg="white", font=("Times", 30, "bold"), relief="flat")
# time_label.pack(ipadx=50,ipady=30)
time_label.place(relx=0.5,rely=0.5,anchor="center")


def update_label():
    current_time = strftime("%H: %M: %S")
    time_label.configure(text=current_time)
    time_label.after(80, update_label)


update_label()
window.mainloop()
