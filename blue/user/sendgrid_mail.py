import sendgrid
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("aakashgupta291@gmail.com")
to_email = Email("aakashgupta291@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content(type_="text/plain",value="and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)


response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
