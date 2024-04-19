import pandas
from datetime import datetime
import random

today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv('birthdays.csv')

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 4)}.txt"
    birthday_person = birthdays_dict[today_tuple]
    with open(file_path) as letterfile:
        content = letterfile.read()
        content.replace("[NAME]", birthday_person['name'])
