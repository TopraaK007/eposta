# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
import smtplib
def sendmail():
    sender="toprakmustafaali1@gmail.com"
    reciever=sender
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender,"malitprk45")
        subject="Selamun Aleykümm"
        body="adam mısın?"
        mailContent=f"To:{reciever}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,reciever,mailContent)
        print("Mail gönderildi")
    except smtplib.SMTPException as e:
        print(e)

