# https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strftime
import datetime
import pytz

my_date = datetime.datetime.today()
sentence = f'{my_date:%d %B, %Y }'
formated_date = f'{my_date:%B %d, %Y fell on %A and was the %j day of the year}'

# mod_time = os.stat('abc.txt').st_mtime  #-> 1585084202.5290809
# print(datetime.datetime.fromtimestamp(mod_time))  # modify timestamp

dt = datetime.datetime(2020, 4, 1, 12, 14, 45, tzinfo=pytz.UTC)
# print(dt)

dt_today = datetime.datetime.today() 
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_sp = dt_utcnow.astimezone(pytz.timezone('America/Sao_Paulo'))
dt_now = datetime.datetime.now(tz=pytz.timezone('America/Sao_Paulo'))

print(dt_now.strftime('%B %d, %Y'))
dt_str = 'April 01, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

#  strftime - Datetime to String
#  strptime - String to Datetime

# for tz in pytz.all_timezones:
#     print(tz)

# print(dt_sp)
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)