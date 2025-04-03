import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login('scytheblack991@gmail.com','blackscythe911@')

