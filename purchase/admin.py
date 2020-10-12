from django.contrib import admin
from .models import Purchase, PurchasePart


class PurchasePartAdminInline(admin.TabularInline):
    model = PurchasePart
    readonly_fields = ('total',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchasePartAdminInline,)

    readonly_fields = ('date', 'purchase_number',
                       'total', 'original_basket',
                       'stripe_pid',)

    fields = ('purchase_number', 'full_name',
              'email', 'phone_number',
              'street_address1', 'street_address2', 'town_or_city',
              'county', 'postcode', 'country', 'date',
              'total', 'original_basket',
              'stripe_pid',)

    list_purchases = ('date', 'purchase_number', 'full_name',
                      'total',)

    purchased = ('+date',)


admin.site.register(Purchase, PurchaseAdmin)
