from django.urls import path
from .views import JobListCreateView, JobDetailView, list_jobs  
urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('jobs/view/', list_jobs, name='job-view'),  
]
