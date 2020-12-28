import smtplib

#Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)

#Start TLS for security
server.starttls()

#Authentication
server.login('practicewitharjya@gmail.com','Java@1234')

#Msg I want to send
message = "This mail has been sent using Python"

#Sending the mail
server.sendmail('practicewitharjya@gmail.com', 'arjya.net@gmail.com', message)

# terminating the session
server.quit()

