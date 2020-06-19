from django.db import models


class Categories(models.Model):
    name = models.CharField(max_lenght=100)
    friendly_name = models.CharField(max_lenght=100, blank=True)

    def __str__(self):
        return self.name

