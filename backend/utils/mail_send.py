import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from backend import settings

MY_ADDRESS = 'testivan2003@mail.ru'
PASSWORD = 'qWWKS9hGFFjqxtvuPVhT'


def send_message(email_list, created, edited, deleted):
    s = smtplib.SMTP_SSL(host='smtp.mail.ru', port=465)
    s.login(MY_ADDRESS, PASSWORD)
    for email in email_list:
        msg = MIMEMultipart()
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = 'Изменения в реестре СЗИ'
        html = f"""\
        <html>
          <head></head>
          <body>
            <p>В реестре появились новые изменения в сертификатах<br>
                Вы можете посмотреть изменения по <a href="{settings.current_url}">ссылке</a>
            </p>
            <table style:border 1px>
                <tr>
                    <td>Добавлено</td>
                    <td>{created}</td>
                </tr>
                <tr>
                    <td>Изменено</td>
                    <td>{edited}</td>
                </tr>
                <tr>
                    <td>Удалено</td>
                    <td>{deleted}</td>
                </tr>
            </table>
          </body>
        </html>
        """
        msg.attach(MIMEText(html, 'html'))
        s.send_message(msg)


if __name__ == '__main__':
    send_message(['nneewday@mail.ru'])
