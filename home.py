from tkinter import *
#from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
def clicked():
    window2= Tk()
    window2.title("Hellow")
    window2.geometry('+1920+100')
    window2.geometry('1920x1000')
    window2.mainloop()

def clicked2():
    messagebox.showinfo(message= "No Reservations")

def HomePage():
    window = Tk()

    window.title("Flight Reservation")
    window.geometry('+1920+100')
    window.geometry('1920x1000')
    window.config(background='#f5c542')

    lbl1 = Label(window , text ="Welcome in our reservation site" , font =( "Times New Roman bold" , 50) , fg= '#42adf5' , bg ='#f5c542' )
    lbl1.grid(row = 0, column =0,columnspan=2 ,padx=20,pady=20)

    lbl2=Label(window , text ="Book your flights and manage your reservations with our simple and intuitive system" , font =( "Ink Free" , 30,'italic'),bg = '#f5c542', wraplength=1000)
    lbl2.grid(row=1, column=0, columnspan=2, padx=20, pady=20)




    button1 = Button(window , text = "Book new flight",  font=("Times New Roman", 20, 'bold'), fg = 'red', bg = '#f5c542' ,command=clicked)
    image1_original= Image.open('image.png')
    resized_img=image1_original.resize((50,50))
    image1 = ImageTk.PhotoImage(resized_img)
    button1.config(image=image1)
    button1.config(compound='top')
    button1.grid(row=2, column=0, padx=20, pady=50)

    button2 = Button(window , text = "View Reservations",  font=("Times New Roman", 20, 'bold'), fg = 'red', bg = '#f5c542', command=clicked2)
    button2.grid(row=2, column=1, padx=20, pady=50)

    window.mainloop()