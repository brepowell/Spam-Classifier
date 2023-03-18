# Modified from https://github.com/bnsreenu/python_for_microscopists/blob/master/AMT_02_extract_gmails_senders[i]a_user/AMT_02_extract_gmails_senders[i]a_user.py
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

3. If you are running this program as $ python email_fetching.py from the terminal window
then make sure to create a credentials.json file and add it to gitignore so that 
your sensitive information will not go to the repository.

"""

# Importing libraries
import imaplib
import email
from email.header import decode_header
import os
import re
import json
import importlib
import sys
from email_parser import send_email_features_to_csv
from email.parser import BytesParser
from email.policy import default
# from SpammedALot import models
import time



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

def saveEmailAsTextFile(msg, i):
    # Save to a folder as a txt file
    directory = "emailsToFlag"
    workingDirectory = os.getcwd() #get current working directory
    path = os.path.join(workingDirectory, directory) 
    fileName = "email" + str(i-1)
    completeName = os.path.join(path, fileName+".txt") 
    text = msg.as_string(unixfrom=False, maxheaderlen=None, policy=None)
  
    with open(completeName, 'w') as f:
        f.write(text)
        f.close()

def fetchAllinFolder(imap, folder, countOfEmails):

    # Select the Spam to fetch messages
    status, messages = imap.select(folder, readonly=True)

    # total number of emails
    messages = int(messages[0])

    # Count ALL messages in folder
    # http://tech.franzone.blog/2012/11/29/counting-messages-in-imap-folders-in-python/
    resp, msgnums = imap.search(None, 'ALL')
    countOfEmailsInFolder = len(msgnums[0].split())

    subjects = []
    senders = []
    dates = []

    # Adapted from : https://www.thepythoncode.com/code/reading-emails-in-python
    for i in range(messages, max(messages-countOfEmailsInFolder, 1), -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")

        # Iterate through ALL messages
        for response in msg:
            if isinstance(response, tuple):

                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                
                
                subject_, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject_, bytes) and isinstance(encoding, str):
                    subject_ = subject_.decode(encoding)

                from_, encoding = decode_header(msg.get("From"))[0]
                if isinstance(from_, bytes) and isinstance(encoding, str):
                    from_ = from_.decode(encoding)

                date_, encoding = decode_header(msg.get("Date"))[0]
                if isinstance(date_, bytes) and isinstance(encoding, str):
                    date_ = date_.decode(encoding)

                # Adding the count of emails ensures no overwriting when called again
                saveEmailAsTextFile(msg, countOfEmails+i) 
                dates.append(date_)
                senders.append(from_)
                subjects.append(subject_)

    countOfEmails += countOfEmailsInFolder-1
    return countOfEmails

def parseEmails():
    folder = "emailsToFlag"
    send_email_features_to_csv(folder)

def classify():
    # TODO: CLASSIFY THE MESSAGE AS SPAM OR HAM
    print("classification magic")
    #return dates, senders, subjects, classifications

#def saveToDatabase(secondCount, dates, senders, subjects, classifications):
def saveToDatabase(secondCount):
    # TODO: SAVE WHETHER THE MESSAGE WAS SPAM OR HAM TO THE DATABASE
    # TODO: SAVE JUST THE SUBJECT LINE FOR THE DATABASE; DATE
    print("database magic")


tic = time.perf_counter()

countOfEmails = 0
imap = loginToGmail()
spam = getSpamFolder()
firstCount = fetchAllinFolder(imap, spam, countOfEmails)

# TODO: DO NOT OVERWRITE THE SPAM EMAILS - FIX THE NAMING CONVENTION
secondCount = fetchAllinFolder(imap, "INBOX", firstCount)
parseEmails()

# TODO: GRAB THE CSV
#dates, senders, subjects, classifications = 
classify()
#saveToDatabase(secondCount, dates, senders, subjects, classifications)
saveToDatabase(secondCount)
               
# print(dates)
# print(senders)
# print(subjects)
# print(len(dates))

# close the connection and logout
imap.close()
imap.logout()

toc = time.perf_counter()
totalTime = toc-tic

print(f"Fetched all emails from Spam and Inbox folders in {totalTime:0.4f} seconds or {totalTime/60:0.4f} minutes")
print(secondCount)