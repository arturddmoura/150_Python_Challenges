#Create a window that will ask the user to enter their name. When they click on a button it should display the message “Hello” and their name and change the background colour and font colour of the message box.
from tkinter import *

def Call():
    #entry_box = Entry (text = 0)
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "blue"
    textbox2["text"] = message

window = Tk()
window.geometry("200x200")
button = Button(text="Press me!", command = Call)
button.place (x = 30, y = 20, width = 120, height = 25)

label1 = Label(text = "Enter name: ")
label1.place (x = 30, y = 50)

textbox1 = Entry(text=" ")
textbox1.place (x = 30, y = 70, width = 150, height = 20)
textbox1.focus()

textbox2 = Message(text=" ")
textbox2.place (x = 30, y = 100, width = 150, height = 30)

window.mainloop()