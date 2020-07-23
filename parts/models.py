from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category'


class Parts(models.Model):
    category = models.ForeignKey('Category',
                                 null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    url_of_image = models.URLField(max_length=1100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parts'
