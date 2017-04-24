import smtplib


def send_email(name, email, message):
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login('gamereviewbros@outlook.com', 'PythonPro')
    receiver = 'gamereviewbros@outlook.com'

    message = 'Sender name: ' + name + '\nSender Email: ' + email + '\n\n\n' + message

    try:
        server.sendmail('gamereviewbros@outlook.com', receiver, message)
        server.quit()
        return True
    except Exception:
        return False