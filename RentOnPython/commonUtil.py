import smtplib


class CommonUtil:
    @staticmethod
    def sendMail(to_mail, sub, msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('practicewitharjya@gmail.com', 'Java@1234')
        server.sendmail('practicewitharjya@gmail.com', to_mail, f"Subject: {sub}\n\n{msg}")
        server.quit()