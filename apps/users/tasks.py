import string

from django.utils.crypto import get_random_string

from users.models import User


def generate_unique_invitation_code(length=8):
    chars = string.ascii_uppercase + string.digits
    while True:
        code = get_random_string(length, chars)
        if not User.objects.filter(invitation_code=code).exists():
            return code
