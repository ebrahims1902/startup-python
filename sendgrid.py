# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

message = sendgrid.helpers.mail(
    from_email='ebrahims1902@gmail.com',
    to_emails='ebrahimsebrahims@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = sendgrid.sg("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

