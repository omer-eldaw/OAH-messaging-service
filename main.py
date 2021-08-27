from tkinter import *
from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os


class MainProgram(Tk):

    def __init__(self):
        super().__init__()

        self.title("Oasis Academy Hobmoor Messaging Service")
        self.geometry("475x375")
        self.resizable(False, False)

        font_options = ("Terminal", 15)

        message_options = "Normal Important Events".split()
        message_clicked = StringVar(self, value=message_options[0])

        welcomeLabel = Label(self, text="OAH Messaging Service", font=font_options)
        
        messageTypeLabel = Label(self, text="Message type: ", font=font_options)
        messageTypeValue = OptionMenu(self, message_clicked, *message_options)
        messageTypeValue.config(font=(("Terminal", 10)))
        messageTypeMenu = self.nametowidget(messageTypeValue.menuname)
        messageTypeMenu.config(font=("Terminal", 10))
        

        bodyOfMessageLabel = Label(self, text="Body of message: ", font=font_options)
        bodyOfMessageInput = Text(self, width=50, height=10)

        open_button = Button(self, text="Open Excel File", font=("Terminal", 10), command=self.select_excel_file)
        send_button = Button(self, text="Send Message", font=("Terminal", 10), command=self.send_messages)


        welcomeLabel.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=26)

        messageTypeLabel.grid(row=1, column=0, padx=5, pady=30, sticky=W, columnspan=26)
        messageTypeValue.grid(row=1, column=1, columnspan=26)
        

        bodyOfMessageLabel.grid(row=2, column=0, padx=5, sticky=W, columnspan=26)
        bodyOfMessageInput.grid(row=3, column=0, sticky=W, padx=5, columnspan=26)

        open_button.grid(row=4, column=0, sticky=W, padx=5, pady=5, columnspan=26)
        send_button.grid(row=4, column=2, sticky=E, padx=5, pady=5, columnspan=26)
    
    def select_excel_file(self):
        filetypes = (
            ('Excel Files', '*.xlsx'),
            ('All Files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )

        showinfo(
            title="Selected File",
            message=filename
        )

    def send_messages(self):
        Login()

from tkinter import *
from tkinter import ttk

class Login(Tk):
    user = 'admin'
    passw ='admin'

    def __init__(self):
        super().__init__()

        self.title('LOGIN SCREEN')
        self.geometry("425x225")

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.login_user).grid(row=3,column=2)


    def login_user(self):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:

            # Do the work done by the main of DBMSproject.py

            #Destroy the current window
            self.destroy()
        else:

            '''Prompt user that either id or password is wrong'''
            self.message = Label(text = 'Username or Password incorrect. Try again!',fg = 'Red')
            self.message.grid(row=6,column=2)


# if __name__ == '__main__':

#     root = Tk()
#     root.geometry('425x225')
#     application = xyz(root)

#     root.mainloop()




if __name__ == "__main__":
    mainProgram = MainProgram()
    mainProgram.mainloop()
