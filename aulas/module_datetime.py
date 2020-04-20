# https://docs.python.org/3/library/datetime.html?highlight=strftime#datetime.datetime.strftime

# https://docs.python.org/2/library/datetime.html
import datetime
import pytz
from locale import setlocale, LC_ALL
from calendar import mdays

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

data = datetime.datetime.today()  #(2020, 7, 14, 10, 53, 20)
print(data.strftime('%d/%m/%Y'))
hoje = datetime.datetime.strptime('20/04/2020', '%d/%m/%Y')
hoje = hoje + datetime.timedelta(days=15)

setlocale(LC_ALL, 'pt_BR.utf-8') # s deixar em branco pega o local do pc
dt = datetime.datetime.now()

formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)
mes_atual = int(dt.strftime('%m'))
print(mdays[mes_atual])