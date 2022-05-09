# Hello this is a quick script that I made
# Please read 'Read First' before doing anything else
# Do not change anything unless you know what you are doing

from email import message
from multiprocessing import context
import ssl
import random
import smtplib
import time

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gmail = ""  # Here I declared a few variables for the emails
email1 = ""
email2 = ""
email3 = ""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

password = ""  # Here I declared some variables for the passwords
password1 = ""
password2 = ""
password3 = ""

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to the Gmail Spam Bot")
howManyEmails = input(     # This is a variable that uses the input command which can let you pick between the 3 options
    "Please write [1] if you want to use 1 email, write [2], if you want to use 2 and [3] if you want to use 3... ")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This is what would happen if you wrote 1 for the answer above
if howManyEmails == "1" or howManyEmails == "[1]":

    # This is where it asks for your email
    email1 = input("Please enter the email you want to use... ")
    password1 = input(
        "Please enter the password for the email that you want to use... ")  # This is where it asks you for your password

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")  # This is where it asks you who is recieving the emails

    # This is what to send to the email
    what_to_send = input("What do you want to send... ")

    # This changes all email variables to email 1 (This was for bug fixing)
    emails = email1
    email2 = email1
    email3 = email1

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This is what would happen if you wrote 2 above
elif howManyEmails == "2" or howManyEmails == "[2]":

    # This is the first email
    email1 = input("Please enter the first email that you want to use... ")
    password1 = input(
        "Please enter the password for the first email that you want to use... ")  # This is the first password

    # This is the second email
    email2 = input("Please enter the second email that you want to use... ")
    password2 = input(
        "Please enter the password for the second email that you want to use... ")  # This is the second password

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")  # This is who recieves the emails

    # This is what to send to the email
    what_to_send = input("What do you want to send... ")

    emails = [email1, email2]

    email3 = email2

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This is what would happen if you wrote 3 above
elif howManyEmails == "3" or howManyEmails == "[3]":

    # This is the first email
    email1 = input("Please enter the first email that you want to use... ")
    password1 = input(
        "Please enter the password for the first email that you want to use... ")  # This is the first password

    # This is the second email
    email2 = input("Please enter the second email that you want to use... ")
    password2 = input(
        "Please enter the password for the second email that you want to use... ")  # This is the second password

    # This is the third email
    email3 = input("Please enter the third email that you want to use... ")
    password3 = input(
        "Please enter the password for the third email that you want to use... ")  # This is the third password

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")  # This is who recieves the email

    # This is what you want to send
    what_to_send = input("What do you want to send... ")

    emails = [email1, email2, email3]

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

else:  # This is what would happen if you didnt write [1] [2] or [3]
    print("You didnt write [1] [2] or [3]")
    quit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


for_while = input(  # This is whether you want to send a limited or unlimited amound of emails
    "Write [1] if you want to only send a limited amount of messages and write [2] if you want to write an unlimited amound of messages (it might stop if your account ran out of storage) ")

amount_of_times_for_loop = 0
start_while_loop = False

# This is what happenes if you wanted a limited amound
if for_while == "1" or for_while == "[1]":
    amount_of_times_for_loop = input(
        "How many times do you want it to repeat? ")
    amount_of_times_for_loop = int(amount_of_times_for_loop)
    sleep_wait = input(
        "How long do you want to wait between each message (in seconds, minimum 0.1)? ")
    sleep_wait = int(sleep_wait)

if amount_of_times_for_loop < 1:
    print("An error has occured - The minimum number you can enter is 1")
    quit()

# This is what happenes if you want an unlimited amound
if for_while == "2" or for_while == "[2]":
    sleep_wait = input(
        "How long do you want to wait between each message (in seconds, minimum 0.1)? ")
    sleep_wait = int(sleep_wait)
    start_while_loop = True

if sleep_wait < 0.1:  # This is some bug fixing
    print("An error has occured")
    quit()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This is a for loop for what would happen if you wanted a limited amound
for i in range(0, amount_of_times_for_loop):
    gmail1 = random.randint(0, 2)

    if gmail1 == 0:
        gmail = email1

    elif gmail1 == 1:
        gmail = email2

    elif gmail1 == 2:
        gmail = email3

    else:
        print("An error has occured")
        quit()

    if email1 == gmail:
        password = password1

    elif email2 == gmail:
        password = password2

    elif email3 == gmail:
        password = password3

    else:
        print("An error has occured")
        quit

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    smtp_server = "smtp.gmail.com"  # This is the gmail bot for the for loop
    port = 465

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail, password)
    except Exception as e:
        print(e)
    finally:
        server.quit()

    print("Your messaage has been sent!")
    time.sleep(sleep_wait)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


while start_while_loop == True:  # This is would would happen if you wanted an unlimited amound of emails
    gmail1 = random.randint(0, 2)

    if gmail1 == 0:
        gmail = email1

    elif gmail1 == 1:
        gmail = email2

    elif gmail1 == 2:
        gmail = email3

    else:
        print("An error has occured")
        quit

    if email1 == gmail:
        password = password1

    elif email2 == gmail:
        password = password2

    elif email3 == gmail:
        password = password3

    else:
        print("An error has occured")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    smtp_server = "smtp.gmail.com"  # This is the gmail bot for the while loop
    port = 465

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail, password)
    except Exception as e:
        print("An error has occured")
        print(e)
        quit
    finally:
        server.quit()

    print("Your message has been sent!")
    time.sleep(sleep_wait)
