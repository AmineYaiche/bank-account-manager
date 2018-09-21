from django.db import models
from django.utils.translation import ugettext as _

from administrators.models import Administrator
from .validators import validate_name, validate_iban


class Client(models.Model):
    first_name = models.CharField(max_length=30, validators=[validate_name])
    last_name = models.CharField(max_length=30, validators=[validate_name])
    iban = models.CharField(max_length=34, validators=[validate_iban])
    administrator = models.ForeignKey(Administrator, related_name='clients', on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')