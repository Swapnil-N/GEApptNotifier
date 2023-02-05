import requests
import time
from datetime import datetime

url = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId=5444&minimum=1"
deadline = datetime(2023, 6, 25)

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

        nextAppt = datetime.strptime(data[0]['startTimestamp'], '%Y-%m-%dT%H:%M')
        print(type(nextAppt))
        print(nextAppt.month)

        if (nextAppt < deadline):
            print("Notify User")

    else:
        print("Request failed with status code:", response.status_code)
        
    time.sleep(120) # wait 120 seconds before making the next request

