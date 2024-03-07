import imp
from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email,email_token):
    return 
    subject = "Your account needs to be verified"
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on  this url to activate your account localhost:8000/account/activate/{email_token}'
    send_email = (subject,message,email_from,[email])