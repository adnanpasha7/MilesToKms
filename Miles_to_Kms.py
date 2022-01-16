from tkinter import *
def calculate_f():
    mile_in_int = int(miles_input.get())
    kilometer = 1.6 * mile_in_int
    km_r.config(text=kilometer)

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=70)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0, padx= 10, pady= 10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0, padx= 10, pady= 10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx= 10, pady= 10)

km_r = Label(text="0")
km_r.grid(column=1, row=1, padx= 10, pady= 10)

km = Label(text="Km")
km.grid(column=2, row=1, padx= 10, pady= 10)

cal_button = Button(text="Calculate", command=calculate_f)
cal_button.grid(column=1, row=2, padx= 10, pady= 10)














window.mainloop()