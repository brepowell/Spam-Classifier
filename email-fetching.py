# Modified from https://github.com/bnsreenu/python_for_microscopists/blob/master/AMT_02_extract_gmails_from_a_user/AMT_02_extract_gmails_from_a_user.py
# by Dr. Sreenivas Bhattiprolu
# https://youtu.be/K21BSZPFIjQ


"""
Extract selected mails from your gmail account

1. Make sure you enable IMAP in your gmail settings
(Log on to your Gmail account and go to Settings, See All Settings, and select
 Forwarding and POP/IMAP tab. In the "IMAP access" section, select Enable IMAP.)

2. If you have 2-factor authentication, gmail requires you to create an application
specific password that you need to use. 
Go to your Google account settings and click on 'Security'.
Scroll down to App Passwords under 2 step verification.
Select Mail under Select App. and Other under Select Device. (Give a name, e.g., python)
The system gives you a password that you need to use to authenticate from python.

"""

# Importing libraries
import imaplib
import email
from email.header import decode_header
import os
import re
import json


def loginToGmail():
    # Open the json file
    # json implementation https://www.geeksforgeeks.org/read-json-file-using-python/
    f = open('credentials.json')
    my_credentials = json.load(f)

    # TODO: FETCH THE CREDENTIALS FROM THE DATABASE

    
    #Load the user name and passwd
    user, password = my_credentials["user"], my_credentials["password"]

    #URL for IMAP connection
    imap_url = 'imap.gmail.com'

    # Connection with GMAIL using SSL
    imap = imaplib.IMAP4_SSL(imap_url)

    # Log in using your credentials
    imap.login(user, password)
    return imap

# Adapted from https://stackoverflow.com/questions/61232095/reading-spam-folder-messages-with-gmail-imap
def getSpamFolder():
    raw_answer = imap.list()
    if raw_answer[0] == "OK":
        answer_body = raw_answer[1]
        parts = []
        for part in answer_body:
            part = part.decode('utf-8')
            parts.append(part.split('"/"')[1])

    # https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
    spam = [i for i in parts if "Spam" in i]
    # https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
    spamfolder = re.sub('"', '', spam[0])
    return spamfolder.strip()

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)



# TODO: SAVE TO A TXT FILE

def fetchAllinFolder(imap, folder):

    # Select the Spam to fetch messages
    status, messages = imap.select(folder, readonly=True)

    # total number of emails
    messages = int(messages[0])

    # Count ALL messages in folder
    # http://tech.franzone.blog/2012/11/29/counting-messages-in-imap-folders-in-python/
    resp, msgnums = imap.search(None, 'ALL')
    mycount = len(msgnums[0].split())

    # Adapted from : https://www.thepythoncode.com/code/reading-emails-in-python
    for i in range(messages, max(messages-mycount, 1), -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)
                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if isinstance(From, bytes):
                    From = From.decode(encoding)
                print("Subject:", subject)
                print("From:", From)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            # print text/plain emails and skip attachments
                            print(body)
                        elif "attachment" in content_disposition:
                            # download attachment
                            filename = part.get_filename()
                            if filename:
                                folder_name = clean(subject)
                                if not os.path.isdir(folder_name):
                                    # make a folder for this email (named after the subject)
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                # download attachment and save it
                                open(filepath, "wb").write(part.get_payload(decode=True))
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)
                # if content_type == "text/html":
                #     # if it's HTML, create a new HTML file and open it in browser
                #     folder_name = clean(subject)
                #     if not os.path.isdir(folder_name):
                #         # make a folder for this email (named after the subject)
                #         os.mkdir(folder_name)
                #     filename = "index.html"
                #     filepath = os.path.join(folder_name, filename)
                #     # write the file
                #     open(filepath, "w").write(body)
                #     # open in the default browser
                #     webbrowser.open(filepath)
                print("="*100)


imap = loginToGmail()
spam = getSpamFolder()
fetchAllinFolder(imap, spam)

# TODO: FETCH FROM INBOX TOO

# TODO: SAVE AS TXT FILES FOR UPLOAD TO THE DATABASE - SAVE ATTRIBUTES TOO


# Select the Inbox to fetch messages
# imap.select('Inbox')
# Envelope = 

# close the connection and logout
imap.close()
imap.logout()
