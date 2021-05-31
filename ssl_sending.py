import smtplib 
from email.mime.text import MIMEText 

def sendMail(me, you, msg): 
	smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp.login(me, 'Rycbar123!') 
	msg = MIMEText(msg) 
	msg['Subject'] = 'Sang Tech Alert' 
	smtp.sendmail(me, you, msg.as_string()) 
	smtp.quit() 

if __name__ == "__main__": 
	sendMail('louis.tw.kim@gmail.com', 'louis.tw.kim@gmail.com', 'mail test')

