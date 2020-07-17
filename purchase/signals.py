from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import PurchasePart


@receiver(post_save, sender=PurchasePart)
def save_update(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=PurchasePart)
def delete_update(sender, instance, **kwargs):
    instance.order.update_total()
