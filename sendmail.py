import smtplib
import config
from datetime import date

LECTURER = "nsofor@gmail.com"
today = date.today()
course = "SOC 101"
lecturerName = "Dr. Nsofor"
link = ""

def send_email(subject, msg):
    try:
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        server = smtplib.SMTP('smtp.gmail.com', 25)
        server.ehlo()
        server.starttls()
        # server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        server.login
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, LECTURER, message)
        server.set_debuglevel(1)
        server.quit()
        print("Email send success 1")
    except:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, LECTURER, message)
        server.set_debuglevel(1)
        server.quit()
        print("Email send success")

    # try:
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.ehlo()
    #     server.starttls()
    #     server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    #     message = 'Subject: {}\n\n{}'.format(subject, msg)
    #     server.sendmail(config.EMAIL_ADDRESS, LECTURER, message)
    #     server.set_debuglevel(1)
    #     server.quit()
    #     print("Email send success")
    # except:
    #     print("Email failed to send")

subject = f"{course}: {today}"
msg = f"Good day, {lecturerName}, \n\n here is a link to today's attendance: {link} \n\n Truly,\nAttendance Bot"

send_email(subject, msg)
