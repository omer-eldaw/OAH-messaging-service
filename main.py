from tkinter import *
from tkinter import messagebox
from tkinter import font
import os
import tkinter


class MainProgram(Tk):

    def __init__(self):
        super().__init__()

        self.title("Oasis Academy Hobmoor Messaging Service")
        self.geometry("600x375")

        font_options = ("Malgun Gothic", 15)

        message_options = [
            "Normal Message",
            "Important Announcement",
            "Events Announcement"
        ]

        # ALLOWS THE SIGN THAT IS CLICKED IN THE MENU TO BE ASSIGNED TO A VARIABLE WHICH IN THIS CASE IS sign_clicked
        message_clicked = StringVar()
        message_clicked.set(message_options[0])

        welcomeLabel = Label(self, text="OAH Messaging Service", font=font_options).grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=26)
        

        messageTypeLabel = Label(self, text="Message type: ", font=font_options).grid(row=1, column=0, padx=5, pady=30, sticky=W, columnspan=26)
        messageTypeValue = OptionMenu(self, message_clicked, *message_options).grid(row=1, column=1, columnspan=26)

        encryptionLabel = Label(self, text="Body of message: ", font=font_options).grid(row=2, column=0, padx=5, sticky=W, columnspan=26)
        encryptionInput = Entry(self, width=75)
        encryptionInput.grid(row=3, column=0, sticky=W, padx=5, columnspan=26)





if __name__ == "__main__":
    mainProgram = MainProgram()
    mainProgram.mainloop()
