from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Resident, Flat

def update_residents_amount(flat):
    flat.residents_amount = flat.residents.count()
    flat.save(update_fields=["residents_amount"])

@receiver(post_save, sender=Resident)
def resident_added(sender, instance, **kwargs):
    update_residents_amount(instance.flat)

@receiver(post_delete, sender=Resident)
def resident_removed(sender, instance, **kwargs):
    update_residents_amount(instance.flat)