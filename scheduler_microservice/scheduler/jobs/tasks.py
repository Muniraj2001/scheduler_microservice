from celery import shared_task
from .models import Job
from django.utils import timezone

@shared_task
def execute_job(job_id):
    job = Job.objects.get(id=job_id)
    print(f"Executing job: {job.name}")
    job.last_run = timezone.now()
    job.next_run = None  
    job.save()
