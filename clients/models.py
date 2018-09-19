from django.db import models

from administrators.models import Administrator


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    iban = models.CharField(max_length=34)
    administrator = models.ForeignKey(Administrator, related_name='clients', on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
