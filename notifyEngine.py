import smtplib

sender_email = ""
receiver_email = ['parikhjatin95@gmail.com']

def notifyviamail(subject, message):
    message = 'Subject: {}\n\n{}'.format(subject, message)
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, "")
        #print('subject ::: ' + subject)
        #print(message)
        #print(receiver_email)
        s.sendmail(sender_email, receiver_email, message)
        s.quit()
    except:
        print("Error: Unable to send email.")

