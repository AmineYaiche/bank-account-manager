from django.contrib.auth.models import User
from django.db import models


class Administrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.user)
