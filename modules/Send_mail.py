import tkinter as tk
from tkinter import filedialog, PhotoImage
import smtplib
from email.message import EmailMessage
import os
import colorama
from colorama import Fore,Back,Style

EMAIL_ADDRESS = os.environ.get('useremail')
EMAIL_PASSWORD = os.environ.get('userpass')

def AskFile():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilenames()
    return file_path

def send_email_smtp(subject, to, body, optionTwo):
    """
    Subject: Matter of Message
    To: to whome you wanna send message to
    Body: What are your message
    optionTwo: y if you wanna send attachments else n
    """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['to'] = to
    msg.set_content(body)

    if str(optionTwo).lower() == 'y':
        print(Fore.GREEN, "Choose your Files: ", Fore.RESET)
        fileArray = AskFile()
        if len(fileArray) == 0:
            pass
        else:
            print(Fore.GREEN, 'Uploaded Files:', Fore.RESET)
            for file in fileArray:
                with open(file,'rb') as f:
                    file_data = f.read()
                    file_name = f.name
                    fileArrayString = f.name.split('/')
                    file_name = fileArrayString[len(fileArrayString) - 1]
                    print(Fore.MAGENTA,file_name, Fore.RESET)
                msg.add_attachment(file_data, maintype='image', subtype='video', filename=file_name)
    else:
        pass
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        print(Fore.BLUE, "Message is being Sent", Fore.RESET)
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print(f"\nMessage has been Sent to {to}", Fore.RESET)