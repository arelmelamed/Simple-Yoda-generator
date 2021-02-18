from tkinter import *

window = Tk()
window.title("Yoda Generator")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg="yellow")


def master_yoda():
    text_box_two.delete("1.0", END)
    yoda = text_box_one.get("1.0", END)
    yoda = yoda.split()[::-1]
    y = text_box_two.insert("1.0", yoda)


my_label = Label(text="Convert to Yoda", font=("David", 24, "bold"))
my_label.grid(column=1, row=2)
my_label.config(bg="green")

text_box_one = Text(height=5, width=50)
text_box_one.grid(column=1, row=3)
text_box_two = Text(height=5, width=50)
text_box_two.grid(column=1, row=4)

convert_button = Button(text="Convert to Yoda", command=master_yoda)
convert_button.grid(column=2, row=3)

window.mainloop()
