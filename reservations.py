from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta
from database import view_reservations, delete_reservation
from edit_reservations import editing

def reserevations():
    reservations_list.delete(0, END)  # Clear the listbox before inserting new items
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

def clicked():
    if not reservations_list.curselection():
        messagebox.showerror("Error", "Please select a reservation to edit.")
        return
    select = False
    select = messagebox.askokcancel(title= "Confirm Selection" ,message=reservations_list.get(reservations_list.curselection()))
    if not select:
        return
    indx = reservations_list.curselection()
    fid  = indx[0] + 1
    full_name = reservations_list.get(indx)[1]
    flight_number = reservations_list.get(indx)[2]  
    departure = reservations_list.get(indx)[3]
    destination = reservations_list.get(indx)[4]
    date = reservations_list.get(indx)[5]
    seat_number = reservations_list.get(indx)[6]
    editing(fid, full_name, flight_number, departure, destination, date, seat_number, reserevations)
    
    

    
    
    

window = Tk()

window.title("Flight Reservations")
window.geometry('+1920+100')
window.geometry('1920x1000')
window.config(background='#f5c542')

reservations_list = Listbox(window, width=100, height=20, font=("Times New Roman", 15), bg='white', fg='black')
reservations_list.grid(row=0, column=0, padx=20, pady=20)
reserevations()

button1 = Button(window, text="Edit Selected Reservation", font=("Times New Roman", 20), bg='blue', fg='white', command=clicked)
button1.grid(row=1, column=0, padx=20, pady=20)
button2 = Button(window, text="Delete Selected Rservation", font=("Times New Roman", 20), bg='red', fg='white', command=delete)
button2.grid(row=2, column=0, padx=20, pady=20)



window.mainloop()