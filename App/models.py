from django.db import models


# Create your models here.
class about(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=2000, blank=True)
    firstname = models.CharField(max_length=200, blank=True)
    fathername = models.CharField(max_length=200, blank=True)
    mothername = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    mail = models.CharField(max_length=200, blank=True)
    Address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name
