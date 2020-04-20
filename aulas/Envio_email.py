from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'djthiago82@gmail.com'
minha_senha = 'techinical2017'

with open(r'C:\Users\Thiago\Documents\PyhtonProgresso\Estudos\aulas\template.html', 'r', encoding='UTF-8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Thiago Antunes', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Thiago Antunes'
msg['to'] = 'thiagotna@hotmail.com'
msg['subject'] = 'E-mail: Python'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# with open('image.jpg', 'rb') as image:
#     image = MIMEImage(image.read())
#     msg.attach(image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso...')
    except Exception as e:
        print('E-mail não enviado')
        print('Erro: ', e)
