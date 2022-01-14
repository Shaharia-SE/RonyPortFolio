from django.db import models


# Create your models here.
class about(models.Model):
    name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name
