import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email(api_key, to_email, from_email):
    print("hi");
    message = Mail(
        from_email="navya.nelluri98@gmail.com",
        to_emails="navya.nelluri98@gmail.com",
        subject='Notification: Push event on main branch',
        plain_text_content=''' A push event has occurred on the main branch.
        
       
       Thanks,
        Team TWA'''
    )

    #try:
    sg = sendgrid.SendGridAPIClient(api_key='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')
    print("hello")
    response = sg.send(message)
    print('SendGrid API response:', response.status_code, response.body)
    print('Email sent successfully')
    #except Exception as e:
        #print('Error sending email:', str(e))

if __name__ == '__main__':
    import sys

    api_key = sys.argv[0]
    to_email = sys.argv[1]
    from_email = sys.argv[2]
    send_email(api_key, to_email, from_email)
