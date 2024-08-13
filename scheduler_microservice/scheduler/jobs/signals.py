from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Job
from .tasks import execute_job

@receiver(post_save, sender=Job)
def schedule_job(sender, instance, created, **kwargs):
    """
    Signal to schedule the job whenever a new job is created or an existing job is updated.
    """
    if created:
        schedule = instance.schedule  
        instance.next_run = timezone.now() + timezone.timedelta(seconds=10)
        instance.save()
        
        execute_job.apply_async((instance.id,), eta=instance.next_run)
    else:
        
        execute_job.apply_async((instance.id,), eta=instance.next_run)
