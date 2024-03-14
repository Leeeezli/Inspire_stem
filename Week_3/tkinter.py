import tkinter
root = tkinter.Tk()

root.title("Students registration form")
name_label = tkinter.Label(root,text = "Enter student's name")
name_label.pack()
name_textbox = tkinter.Entry(root)
name_textbox.pack()

root.title("Students registration form")
age_label = tkinter.Label(root,text = "Enter Age")
age_label.pack()
age_textbox = tkinter.Entry(root)
age_textbox.pack()

root.title("Students registration form")
date_label = tkinter.Label(root,text = "Enter date")
date_label.pack()
date_textbox = tkinter.Entry(root)
date_textbox.pack()

submit_button = tkinter.Button(root,text = "Submit")
submit_button.pack()

root.mainloop()
