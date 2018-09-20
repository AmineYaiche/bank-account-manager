from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Administrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('Administrator')
        verbose_name_plural = _('Administrators')
