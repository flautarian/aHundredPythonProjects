import os
from random import randint
import random
import smtplib

my_email = "fgiacconi.dev@gmail.com"
password = "abcd1234"

script_dir = os.path.dirname(__file__)

connection = smtplib.SMTP("smtp.gmail.com")

""" targets = ['target1@gmail.com']
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=targets, msg="Suject:Hello mail!😇") """


import datetime as dt

day_indexes = ["Monday", "Tuesday", "Wendsday", "Thursday", "Friday", "Saturday", "Sunday"]



with open(script_dir + "/quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()

current_date = dt.datetime.now()

current_day = day_indexes[current_date.weekday()]

subject = f"Hi Facundo!, today is {current_day}, and here is your motivational tip for today 😎"
msg = random.choise(all_quotes)


connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=my_email, subject=subject, msg=msg)

