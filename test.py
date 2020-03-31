import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email="from__email",
    to_emails="to__email__",
    subject="Cambridge Computer Science Admissions Updated",
    html_content="The admissions test information for cambridge has been updated"
)

try:
    sg = SendGridAPIClient("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")
    sg.send(message)
except Exception as e:
    print(e)