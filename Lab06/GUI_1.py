from tkinter import *

def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_label.configure(text = 'Converted: {:.1f}'.format(temp))
    entry.delete(0,END) 

root = Tk()
message_label = Label(text='Enter a temperature',
font=('Poppins', 14))
output_label = Label(font=('Poppins', 14))
entry = Entry(font=('Poppins', 14), width=10)
calc_button = Button(text='Ok', font=('Poppins', 14),command=calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
mainloop()
