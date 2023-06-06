import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(api_key, to_email, from_email):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Notification: Push event on main branch',
        plain_text_content='A push event has occurred on the main branch.'
    )

    try:
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        response = sg.send(message)
        print('Email sent successfully')
    except Exception as e:
        print('Error sending email:', str(e))

if __name__ == '__main__':
    import sys

    api_key = sys.argv[0]
    to_email = sys.argv[1]
    from_email = sys.argv[2]
    send_email(api_key, to_email, from_email)
