import smtplib # Simple mail transfer protocol
conn= smtplib.SMTP('smtp.gmail.com', 587) # connection object, port 587 for emails
conn.ehlo() # To conncet to smtp server
conn.starttls() # To begin encryption
conn.login('zoe9955@gmail.com','xwjymwahtvswmxbm')
conn.sendmail('zoe9955@gmail.com','zoe9955@gmail.com','''Subject: The Bell Jar\n\nDear Zoe,\n
I read this very exciting book called the Bell Jar. Hope you read it too and tell me what you
think! \n Sincerely,\nZoe''')
conn.quit()