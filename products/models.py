from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Products(models.Model):
    category = models.ForeignKey(Categories,
                                 null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, blank=True)

    def __str__(self):
        return self.name
