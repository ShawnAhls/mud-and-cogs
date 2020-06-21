from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Parts(models.Model):
    category = models.ForeignKey('Categories',
                                 null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    url_of_image = models.URLField(max_length=1100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parts'
