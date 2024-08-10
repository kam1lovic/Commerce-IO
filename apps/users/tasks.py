import random
import string

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse

from users.models import User


@shared_task
def send_welcome_email(user_id, token):
    try:
        user = User.objects.get(id=user_id)
        confirmation_url = f"{settings.DOMAIN}{reverse('confirm_account', args=[token])}"
        email_html_message = render_to_string('welcome_email.html',
                                              {'user': user, 'confirmation_url': confirmation_url})
        email_subject = 'Welcome to Our Site'
        email = EmailMessage(
            subject=email_subject,
            body=email_html_message,
            to=[user.email],
        )
        email.content_subtype = 'html'
        email.send(fail_silently=False)
    except User.DoesNotExist:
        pass
    except Exception as e:
        print(f'ERROR: {e}')


def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))


def generate_unique_invitation_code():
    while True:
        invitation_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if not User.objects.filter(invitation_code=invitation_code).exists():
            return invitation_code
