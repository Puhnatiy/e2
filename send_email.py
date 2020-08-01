import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email_with_text(text, email_from, email_to):
    text = text
    print(text)
    message = Mail(
        from_email=email_from,
        to_emails=email_to,
        subject='Email from the past',
        html_content=f'<strong>{text}</strong>')
    print(message)
    try:
        #sg = SendGridAPIClient(os.get('SENDGRID_API_KEY'))
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response)
        return response
    except Exception as e:
        print("error1")