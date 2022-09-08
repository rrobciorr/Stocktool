import smtplib, ssl
from email.message import EmailMessage

def send(content ='message from python' ):
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = 'Przykładowy temat '
    msg['From'] = "me@gmail.com"
    msg['To'] = "rrobciorr@gmail.com"

    port = 465  # For SSL
    login = "rrobciorr@gmail.com"
    password = 'ceifjuojpaipieke'

    # Create a secure SSL context
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(login, password)
            server.send_message(msg)
            print('E-mail sent successfully!')
    except: 
        print('Opss .. Error sending mail')

#send("siema")


