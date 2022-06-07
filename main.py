import ssl
import random
import smtplib
import time

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

port = 587

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gmail = ""
email1 = ""
email2 = ""
email3 = ""

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

password = ""
password1 = ""
password2 = ""
password3 = ""

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to the Gmail Spam Bot")
howManyEmails = input(
    "Please write [1] if you want to use 1 email, write [2], if you want to use 2 and [3] if you want to use 3... ")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if howManyEmails == "1" or howManyEmails == "[1]":

    email1 = input("Please enter the email you want to use... ")
    password1 = input(
        "Please enter the password for the email that you want to use... ")

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")

    what_to_send = input("What do you want to send... ")

    emails = email1
    email2 = email1
    email3 = email1

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif howManyEmails == "2" or howManyEmails == "[2]":

    email1 = input("Please enter the first email that you want to use... ")
    password1 = input(
        "Please enter the password for the first email that you want to use... ")

    email2 = input("Please enter the second email that you want to use... ")
    password2 = input(
        "Please enter the password for the second email that you want to use... ")

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")

    what_to_send = input("What do you want to send... ")

    emails = [email1, email2]

    email3 = email2

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

elif howManyEmails == "3" or howManyEmails == "[3]":

    email1 = input("Please enter the first email that you want to use... ")
    password1 = input(
        "Please enter the password for the first email that you want to use... ")

    email2 = input("Please enter the second email that you want to use... ")
    password2 = input(
        "Please enter the password for the second email that you want to use... ")

    email3 = input("Please enter the third email that you want to use... ")
    password3 = input(
        "Please enter the password for the third email that you want to use... ")

    reciever = input(
        "Please write the email of the person that you want to recieve the emails... ")

    what_to_send = input("What do you want to send... ")

    emails = [email1, email2, email3]

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

else:
    print("You didnt write [1] [2] or [3]")
    quit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


for_while = input(
    "Write [1] if you want to only send a limited amount of messages and write [2] if you want to write an unlimited amound of messages... ")

amount_of_times_for_loop = 0
start_while_loop = False


if for_while == "1" or for_while == "[1]":
    amount_of_times_for_loop = input(
        "How many times do you want it to repeat? ")
    amount_of_times_for_loop = int(amount_of_times_for_loop)
    sleep_wait = input(
        "How long do you want to wait between each message (in seconds, minimum 1)? ")
    sleep_wait = int(sleep_wait)


if for_while == "2" or for_while == "[2]":
    sleep_wait = input(
        "How long do you want to wait between each message (in seconds, minimum 1)? ")
    sleep_wait = int(sleep_wait)
    start_while_loop = True

if sleep_wait < 0.1:
    print("An error has occured")
    quit()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

    server = "smtp.gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(server, port)
        server.starttls()
        server.login(gmail, password)
        server.sendmail(gmail, reciever, what_to_send)
    except Exception as e:
        print(e)

    print("Your messaage has been sent!")
    time.sleep(sleep_wait)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


while start_while_loop == True:
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

    server = "smtp.gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(server, port)
        server.starttls()
        server.login(gmail, password)
        server.sendmail(gmail, reciever, what_to_send)
    except Exception as e:
        print(e)

    print("Your message has been sent!")
    time.sleep(sleep_wait)
