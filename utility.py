def sendEmail(email_add, purpose, message):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("", "")
    msg = 'Subject: {}\n\n{}'.format(purpose, message)
    response = server.sendmail("sender_email", email_add, msg)
    return True
