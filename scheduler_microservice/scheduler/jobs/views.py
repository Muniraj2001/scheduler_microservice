from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .tasks import execute_job

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        execute_job.apply_async((job.id,), countdown=10)  

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Add this view
def list_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})
