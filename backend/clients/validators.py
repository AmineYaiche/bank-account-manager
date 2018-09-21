import re

from django.core.exceptions import ValidationError
from schwifty import IBAN


def validate_name(name):
    if re.match('^[a-zA-Z\s]+$', name) is None:
        raise ValidationError('This field accepts alphabets only')


def validate_iban(iban):
    try:
        IBAN(iban)
    except ValueError:
        raise ValidationError('Bad format')
