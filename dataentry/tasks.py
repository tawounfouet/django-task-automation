from awd_main.celery import app
import time
from django.core.management import call_command
from .utils import generate_csv_file, send_email_notification
from django.conf import settings

from django.core.mail import EmailMessage


# @app.task
# def celery_test_task():
#     time.sleep(5) # simulation of any task that's going to take 10 seconds
#     return "Task Executed Successfull"

def send_email_notification(mail_subject, message, to_email, attachement=None):
    try:
        from_email = settings.DEFAULT_FROM_EMAIL
        mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
        if attachement is not None:
            mail.attach_file(attachement)
        mail.send()
    except Exception as e:
        raise e


@app.task
def celery_test_task():
    time.sleep(5) # simulation of any task that's going to take 10 seconds
    # send an email
    mail_subject = 'Test subject'
    message = 'This is a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    #send_email_notification(mail_subject, message, to_email)
    from_email = settings.DEFAULT_FROM_EMAIL
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
    return 'Email sent successfully.'

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    # notify the user by email
    mail_subject = 'Import Data Completed'
    message = 'Your data import has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    #send_email_notification(mail_subject, message, [to_email])
    
    from_email = settings.DEFAULT_FROM_EMAIL
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()

    return 'Data imported successfully.'


@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    # Send email with the attachment
    mail_subject = 'Export Data Successful'
    message = 'Export data successful. Please find the attachment'
    to_email = settings.DEFAULT_TO_EMAIL

    send_email_notification(mail_subject, message, [to_email], attachment=file_path)
    #send_email_notification(mail_subject, message, [to_email])

    
    #EmailMessage(mail_subject, message, [to_email], attachment=file_path)
    # from_email = settings.DEFAULT_FROM_EMAIL
    # mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    # mail.attach_file(file_path)
    # mail.send()
 
    return 'Export Data task executed successfully.'
