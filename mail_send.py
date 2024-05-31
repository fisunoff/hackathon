import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'testivan2003@mail.ru'
PASSWORD = 'qWWKS9hGFFjqxtvuPVhT'

def send_message(email_list):
    s = smtplib.SMTP_SSL(host='smtp.mail.ru', port=465)
    s.login(MY_ADDRESS, PASSWORD)
    for x in email_list:
        msg = MIMEMultipart()
        msg['From'] = MY_ADDRESS
        msg['To'] = x
        msg['Subject'] = 'Изменения в реестре СЗИ'
        html = """\
        <html>
          <head></head>
          <body>
            <p>В реестре появились изменения<br>
               <a href="http://www.python.org">Здесь</a> вы можете посмотреть изменения.
            </p>
            <table>
                <tr>
                    <td>Добавление</td>
                    <td>Изменение</td>
                </tr>
            </table>
          </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        s.send_message(msg)

send_message(['nneewday@mail.ru', 'knowslana@gmail.com'])