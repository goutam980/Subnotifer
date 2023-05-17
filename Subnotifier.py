#!/bin/bin/python3

import cgi
import subprocess as sp

from datetime import datetime, timedelta
from dateutil import parser
from smtplib import SMTP
from email.mime.text import MIMEText


had_r=input(""""

press 1 to Check the Subscription .
press 2 to Check the attached System attached with the Subscription)
Press 3 to Configure mail server.
Press 4 to Configure notification sender app.
Press 5 to Check expired subscribtion .
Enter 6 for exit: """)


had_r=int(had_r)


if had_r==1:
  grap = sp.getstatusoutput("subscription-manager list --consumed")
  print(grap)


elif had_r==5:
  grap = sp.getstatusoutput("subscription-manager list --consumed | grep Ends")
  expiry_date=grap

  current_date=datetime.now()
  #print(a)

  expiry_date_str=expiry_date[1].split()[-1]
  expiry_date = datetime.strptime(expiry_date_str, '%m/%d/%Y')
  time_remaining = expiry_date - current_date

  num_days = time_remaining.days
  print(num_days)

  if num_days >= 30:
    Subject="Subscription Expiration Alert"
    body="Your subscription is about to expire in {}".format(time_remaining)
#  function to send Email Notification
    print('Subject: ', Subject)
    print('Body: ', body)
#    msg = MIMEText(body)
#        msg["From"] = email_from
#        msg["To"] = email_to
#        msg["Subject"] = subject
#        with SMTP(smtp_server) as smtp:
#            smtp.send_message(msg)

