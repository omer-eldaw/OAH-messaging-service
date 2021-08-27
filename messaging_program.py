import os
from twilio.rest import Client
from datetime import date
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

class MobileAnnouncer():
    def __init__(self, list_of_nums):
        
        self.list_of_nums = list_of_nums

        account = "ACee20a96f5c0e98c713a5b0bcaf372180"
        token = "fe765b3b83a17c72e79bc9626d6be8f2"
        self.client = Client(account, token)

        today = date.today()
        self.day_today = today.strftime("%d/%m/%Y")

    def normalMessage(self, body_message):
        self.body_message = body_message

        for num in self.list_of_nums:
            message = self.client.messages.create(
                body=f"{self.day_today}\n\n{self.body_message}\n\nThank You,\nOasis Academy Hobmoor",
                from_="+447888871147",
                to={num}
            )

    def importantAnnouncement(self, body_message):
        self.body_message = body_message

        for num in self.list_of_nums:
            message = self.client.messages.create(
                body=f"{self.day_today}\n\nIMPORTANT ANNOUNCEMENT\n\n{self.body_message}\n\nThank You,\nOasis Academy Hobmoor",
                from_="+447888871147",
                to={num}
            )
        

    def eventAnnouncement(self, body_message):
        self.body_message = body_message

        for num in self.list_of_nums:
            message = self.client.messages.create(
                body=f"{self.day_today}\n\nEVENT\n\n{self.body_message}\n\nThank You,\nOasis Academy Hobmoor",
                from_="+447888871147",
                to={num}
            )
        
        



        


