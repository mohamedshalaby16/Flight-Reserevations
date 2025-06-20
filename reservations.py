from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta
from database import view_reservations, delete_reservation

def reserevations():
    for r in view_reservations():
        reservations_list.insert(END,r)


def delete():
    selected = reservations_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a reservation to delete.")
        return
    fid = selected[0] + 1

    delete_reservation(fid)
    reservations_list.delete(selected)


window = Tk()

window.title("Flight Reservations")
window.geometry('+1920+100')
window.geometry('1920x1000')
window.config(background='#f5c542')

reservations_list = Listbox(window, width=100, height=20, font=("Times New Roman", 15), bg='white', fg='black')
reservations_list.grid(row=0, column=0, padx=20, pady=20)
reserevations()

button1 = Button(window, text="Edit Selected Reservation", font=("Times New Roman", 20), bg='blue', fg='white')
button1.grid(row=1, column=0, padx=20, pady=20)
button2 = Button(window, text="Delete Selected Rservation", font=("Times New Roman", 20), bg='red', fg='white', command=delete)
button2.grid(row=2, column=0, padx=20, pady=20)



window.mainloop()