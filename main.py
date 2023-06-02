from messaging_program import excelScraper
from messaging_program import MobileAnnouncer
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class mainProgram(Tk):

    def __init__(self):

        super().__init__()

        self.title("Oasis Academy Hobmoor Messaging Service")
        self.geometry("450x375")
        self.resizable(False, False)

        font_options = ("Terminal", 15)

        message_options = "Normal Important Events".split()
        self.message_clicked = StringVar(self, value=message_options[0])

        self.welcomeLabel = Label(self, text="OAH Messaging Service", font=font_options)
        
        self.messageTypeLabel = Label(self, text="Message type: ", font=font_options)
        self.messageTypeValue = OptionMenu(self, self.message_clicked, *message_options)
        self.messageTypeValue.config(font=(("Terminal", 10)))
        self.messageTypeMenu = self.nametowidget(self.messageTypeValue.menuname)
        self.messageTypeMenu.config(font=("Terminal", 10))
        

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
        filename = fd.askopenfilename(title = 'Open a file', initialdir = 'C:\Program Files', filetypes = filetypes)
        mb.showinfo(title="Selected File", message=filename)
        Scraper = excelScraper(filename)
        self.num_list = Scraper.retrieveNumbers()

    def send_messages(self):
        confirmation = mb.askyesno(title = "Confirmation", message = f"Are you sure you want to send to this message to {len(self.num_list)} parent/s?")
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
        

if __name__ == "__main__":
    applicationGUI = mainProgram()
    applicationGUI.mainloop()

