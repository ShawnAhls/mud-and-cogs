from django.db import models


class Purchase(models.Model):
    purchase_number = models.CharField(max_length=32, editable=False)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                                 related_name='orders')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    # country = CountryField(blank_label='Country *')
    postcode = models.CharField(max_length=20)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80)
    county = models.CharField(max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    purchase_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0)
    original_basket = models.TextField(default='')
    stripe_pid = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.purchase_number
