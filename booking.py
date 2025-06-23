from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime, timedelta
from database import insert_flight, create_table



def create_date_list():
    start = datetime.today()
    end = datetime(2026, 12, 31)
    delta= timedelta(days=1)
    cur = start

    while cur <= end:
        date_box.insert(END, cur.strftime("%Y-%m-%d"))
        cur += delta

def clicked():
    if (textbox1.get() == "" or textbox2.get() == "" or 
        textbox3.get() == "" or textbox4.get() == "" or 
        textbox6.get() == "" or date_box.curselection() == ()):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if (not textbox1.get().isascii() or not textbox2.get().isascii() or
        not textbox3.get().isascii() or not textbox4.get().isascii() or
        not textbox6.get().isascii()):
        messagebox.showerror("Error", "Please enter only letters in all fields.")
        return
    
    messagebox.showinfo("Success", "Flight booked successfully!")
    insert_flight(textbox1.get(),
                  textbox2.get(),
                  textbox3.get(),
                  textbox4.get(),
                  date_box.get(date_box.curselection()),
                  textbox6.get())
    

    

    



window = Tk()
window.title("Book a Flight")
window.geometry('+1920+100')
window.geometry('1920x1000')
window.config(background='#f5c542')

create_table()

labl1=Label(window, text="Full Name", font=("Times New Roman", 20, 'bold'), fg='red')
labl2=Label(window, text="Flight Number", font=("Times New Roman", 20, 'bold'), fg='red')
labl3=Label(window, text="Departure", font=("Times New Roman", 20, 'bold'), fg='red')
labl4=Label(window, text="Destination", font=("Times New Roman", 20, 'bold'), fg='red')
labl5=Label(window, text="Date", font=("Times New Roman", 20, 'bold'), fg='red')
labl6=Label(window, text="Seat Number", font=("Times New Roman", 20, 'bold'), fg='red')


labl1.grid(row=0, column=0, padx=20, pady=20)
labl2.grid(row=1, column=0, padx=20, pady=20)
labl3.grid(row=2, column=0, padx=20, pady=20)
labl4.grid(row=3, column=0, padx=20, pady=20)
labl5.grid(row=4, column=0, padx=20, pady=20)
labl6.grid(row=5, column=0, padx=20, pady=20)

textbox1= Entry(window, font=("Times New Roman", 20), fg='black')
textbox1.grid(row=0, column=1, padx=20, pady=20)

textbox2= Entry(window, font=("Times New Roman", 20), fg='black')
textbox2.grid(row=1, column=1, padx=20, pady=20)

textbox3= Entry(window, font=("Times New Roman", 20), fg='black')
textbox3.grid(row=2, column=1, padx=20, pady=20)

textbox4= Entry(window, font=("Times New Roman", 20), fg='black')
textbox4.grid(row=3, column=1, padx=20, pady=20)

date_box=Listbox(window, font=("Times New Roman", 20), fg='black')
date_box.grid(row=4, column=1, padx=20, pady=20)
create_date_list()

textbox6= Entry(window, font=("Times New Roman", 20), fg='black')
textbox6.grid(row=5, column=1, padx=20, pady=20)


submit_button = Button(window, text="Book", font=("Times New Roman", 20, 'bold'), fg='blue', bg='#f5c542',command=clicked)
submit_button.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

window.mainloop()