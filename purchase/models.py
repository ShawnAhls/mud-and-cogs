from django.db import models
from django.db.models import Sum
from parts.models import Parts
from django_countries.fields import CountryField
import uuid


class Purchase(models.Model):
    purchase_number = models.CharField(max_length=32, editable=False)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    country = CountryField(blank_label='Country *')
    date = models.DateTimeField(auto_now_add=True)
    purchase_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0)
    original_basket = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def refresh_total(self):
        self.total = self.purchasepart.aggregate(
            Sum('purchasepart_total'))['purchasepart_total__sum'] or 0
        self.save()

    def _purchase_number_create(self):
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.purchase_number


class PurchasePart(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    quantity = models.IntegerField
    total = models.DecimalField(max_digits=6, decimal_places=2,
                                editable=False)

    def save(self, *args, **kwargs):
        self.total = self.part.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.purchase_number}'
