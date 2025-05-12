from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder_email(entrepreneur_email, mentor_email, meeting_date, meeting_time):
    subject = 'Meeting Reminder'
    message = f"This is a reminder that your meeting is scheduled on {meeting_date} at {meeting_time}."

    # Send email to entrepreneur
    send_mail(
        subject,
        message,
        'startupconnect8@gmail.com',  # replace with your sender email
        [entrepreneur_email],
        fail_silently=False,
    )

    # Send email to mentor
    send_mail(
        subject,
        message,
        'startupconnect8@gmail.com',  # replace with your sender email
        [mentor_email],
        fail_silently=False,
    )
