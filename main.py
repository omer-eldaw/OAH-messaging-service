from messaging_program import excelScraper
from messaging_program import MobileAnnouncer
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import sys


class mainProgram(Tk):

    def __init__(self):

        super().__init__()

        self.title("Oasis Academy Hobmoor Messaging Service")
        self.geometry("475x375")
        self.resizable(False, False)

        font_options = ("Terminal", 15)

        message_options = "Normal Important Events".split()
        self.message_clicked = StringVar(self, value=message_options[0])

        self.welcomeLabel = Label(self, text="OAH Messaging Service", font=font_options)
        
        self.messageTypeLabel = Label(self, text="Message type: ", font=font_options)
        self.messageTypeValue = OptionMenu(self, self.message_clicked, *message_options)
        self.messageTypeValue.config(font=(("Terminal", 10)))
        messageTypeMenu = self.nametowidget(self.messageTypeValue.menuname)
        messageTypeMenu.config(font=("Terminal", 10))
        

        self.bodyOfMessageLabel = Label(self, text="Body of message: ", font=font_options)
        self.bodyOfMessageInput = Text(self, width=50, height=10)

        self.open_button = Button(self, text="Open Excel File", font=("Terminal", 10), command=self.select_excel_file)
        self.send_button = Button(self, text="Send Message", font=("Terminal", 10), command=self.send_messages)


        self.welcomeLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=26)

        self.messageTypeLabel.grid(row=1, column=0, padx=5, pady=30, sticky=W, columnspan=26)
        self.messageTypeValue.grid(row=1, column=1, columnspan=26)
        

        self.bodyOfMessageLabel.grid(row=2, column=0, padx=5, sticky=W, columnspan=26)
        self.bodyOfMessageInput.grid(row=3, column=0, sticky=W, padx=5, columnspan=26)

        self.open_button.grid(row=4, column=0, sticky=W, padx=5, pady=5, columnspan=26)
        self.send_button.grid(row=4, column=2, sticky=E, padx=5, pady=5, columnspan=26)
    
    def select_excel_file(self):
        filetypes = (('Excel Files', '*.xlsx'), ('All Files', '*.*'))
        filename = fd.askopenfilename(title = 'Open a file', initialdir = '/', filetypes = filetypes)
        mb.showinfo(title="Selected File", message=filename)
        Scraper = excelScraper(filename)
        self.num_list = Scraper.retrieveNumbers()

    def send_messages(self):
        confirmation = mb.askyesno(title = "Confirmation", message = f"Are you sure you want to send to this message to {len(self.num_list)} parents?")
        if confirmation == True:
            body = self.bodyOfMessageInput.get("1.0",END)
            mobile_messenger = MobileAnnouncer(self.num_list)
            if self.message_clicked.get() == "Normal":
                mobile_messenger.normalMessage(body_message = body)
                mb.showinfo(title="Messages Sent", message = "Messages have been successfully sent")
            elif self.message_clicked.get() == "Important":
                mobile_messenger.importantAnnouncement(body_message = body)
                mb.showinfo(title="Messages Sent", message = "Messages have been successfully sent")
            elif self.message_clicked.get() == "Events":
                mobile_messenger.eventAnnouncement(body_message = body)
                mb.showinfo(title="Messages Sent", message = "Messages have been successfully sent")
        
class mainProgramLogin(Tk):

    def __init__(self):
        
        super().__init__()
        
        self.user = 'admin'
        self.passw ='admin'

        self.title('LOGIN SCREEN')
        self.geometry("275x200")

        # CREATING THE WIDGETS WITH ITS SPECIFIED PROPERTIES

        self.usernameLabel = Label(self, text = ' Username:',font=('Terminal', 15))
        self.username = Entry(self)

        self.passwordLabel = Label(self, text = ' Password:', font=('Terminal', 15))
        self.password = Entry(self, show='*')
        
        self.loginButton = Button(self, text='LOGIN', font=("Terminal", 10), command=self.login_user)

        # APPLYING GRID SYSTEM FOR WIDGETS TO DISPLAY

        self.usernameLabel.grid(row=1,column=1,pady=20)
        self.username.grid(row=1,column=2,columnspan=10)

        self.passwordLabel.grid(row=2,column=1,pady=10)
        self.password.grid(row=2,column=2,columnspan=10)

        self.loginButton.grid(row=3,column=2, columnspan=3)


    def login_user(self):
        if self.username.get() == self.user and self.password.get() == self.passw:
            self.destroy()
        else:
            mb.showerror("Incorrect Login", "Username or Password incorrect. Try again!")


if __name__ == "__main__":
    applicationLoginGUI = mainProgramLogin()
    applicationLoginGUI.mainloop()
    applicationGUI = mainProgram()
    applicationGUI.mainloop()

