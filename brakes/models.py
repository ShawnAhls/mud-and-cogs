from django.db import models

# Create your models here.


class Brakes(models.Model):

    def __str__(self):
        return self.name