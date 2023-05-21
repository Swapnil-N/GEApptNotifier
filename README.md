# GEApptNotifier

## About
This script can be used to automatically send text or email notifications if a global entry appt opens up. It directly pings the dhs api and parses the JSON response to determine whether to send a notification. It uses Google's smpt port and linked email to send email notifications. Text notifications are also send through the email service as emailing (1111111111@tmomail.net, 2222222222@txt.att.net, 3333333333@vtext.com) send a text message to that phone number.

## Setup
- Set `airportCode` to the airport you would like notifications regarding
- Set `deadline` (Year, Month, Day). If you don't want a deadline then set a date far away.
- Set emails or phone numbers with appropriate carrier domain for `receiver_emails` in settings.py
- `sender_email` and `password` must be configured with your own email and app password enabled from google settings.