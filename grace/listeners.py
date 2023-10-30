import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NurseApplication, NurseOrder, ErrorLogs
from .utils import bitrix_add_lead, bitrix_change_active, bitrix_delete_lead, bitrix_change_processed
from django.contrib import messages # Here
from .choices import OrderStatuses

@receiver(post_save, sender=NurseApplication, dispatch_uid=uuid.uuid4())
def application_saved(sender, instance, created, **kwargs):
    
    if created:
        ans = bitrix_add_lead(instance)
        instance.bitrix_id = int(ans)
        instance.save()
        
@receiver(post_save, sender=NurseOrder, dispatch_uid=uuid.uuid4())
def order_saved(sender, instance, created, **kwargs):
    
    if instance.status == OrderStatuses.active:
        bitrix_change_active(instance.application.bitrix_id)
    else:
        bitrix_change_processed(instance.application.bitrix_id, instance.cost_per_week)


    if created:
        ans = False
        try:
            bitrix_change_processed(instance.application.bitrix_id, instance.cost_per_week)
        except: 
            ErrorLogs.objects.create(
                log={'message':'Lead not in bitrix, errr'},
                user='admin'
            )
        instance.application.active = False
        instance.application.save()