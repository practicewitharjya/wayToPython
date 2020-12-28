import smtplib

def sendMail(to_mail, sub, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('practicewitharjya@gmail.com', 'Java@1234')
    server.sendmail('practicewitharjya@gmail.com', to_mail, f"Subject: {sub}\n\n{msg}")
    server.quit()


if __name__ == '__main__':

    tomail = input("Please enter the mail id")
    sub = input("Please enter the subject")
    msg = input("Please enter the mail content")
    sendMail(tomail, sub, msg)
    print("Your mail has been sent!!!!!!!!!!")
