import smtplib

def sendEmail(msg):

    gusr = 'robot.verter@...'
    gpwd = 'SkN#...'
    sendTo = ['alert@...', 'it@...']

    letterBody = 'Subject: {}\n\n{}'.format('service restarted', msg)

    try:
        mailserv = smtplib.SMTP('smtp.gmail.com', 587)
        mailserv.ehlo()
        mailserv.starttls()
        mailserv.login(gusr, gpwd)
        mailserv.sendmail(gusr, sendTo, letterBody)
        # mailserv.close()
        mailserv.quit()
    except Exception as err:
        print('Oooops: ' + str(err))

msg = 'Service MSSQL on ... was restarted recently'
sendEmail(msg)
