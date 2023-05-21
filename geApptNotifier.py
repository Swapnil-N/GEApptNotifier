import requests
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from settings import sender_email, receiver_emails, password

airportCode = "5444" # LocationId: EWR = 5444, JFK = 5140, PHL = 5445
url = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId="+airportCode
deadline = datetime(2023, 11, 20)

def notify_user(body):
    message = MIMEText(body)
    message["Subject"] = "Global Entry Appt Found"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_emails, message.as_string())
    smtp.quit()

while True:
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        # [ {
        #     "locationId" : 5444,
        #     "startTimestamp" : "2023-05-11T08:15",
        #     "endTimestamp" : "2023-05-11T08:30",
        #     "active" : true,
        #     "duration" : 15,
        #     "remoteInd" : false
        # } ]
        if (len(data) >= 1):
            nextAppt = datetime.strptime(data[0]['startTimestamp'], '%Y-%m-%dT%H:%M')
            if (nextAppt < deadline):
                notify_user(nextAppt.strftime('%m/%d/%Y @ %H:%M'))
        else:
            print("No Appts Found")
    else:
        print("Request failed with status code:", response.status_code)

    response.close()
        
    time.sleep(300) # wait x seconds before making the next request
