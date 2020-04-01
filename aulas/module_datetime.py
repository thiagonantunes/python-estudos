# https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strftime
import os
import datetime

my_date = datetime.datetime.today()
print(my_date)

sentence = f'{my_date:%d %B, %Y }'
print(sentence)

formated_date = f'{my_date:%B %d, %Y fell on %A and was the %j day of the year}'
print(formated_date)

mod_time = os.stat('abc.txt').st_mtime  #-> 1585084202.5290809
print(datetime.datetime.fromtimestamp(mod_time))  # modify timestamp