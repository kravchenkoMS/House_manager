from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Resident, Flat

def update_residents_count(flat):
    flat.residents_count = flat.residents.count()
    flat.save(update_fields=["residents_count"])

@receiver(post_save, sender=Resident)
def resident_added(sender, instance, **kwargs):
    update_residents_count(instance.flat)

@receiver(post_delete, sender=Resident)
def resident_removed(sender, instance, **kwargs):
    update_residents_count(instance.flat)
