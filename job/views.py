from django.shortcuts import render
from .models import Job, Category

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {'job_list': job_list}

    return render(request, 'job/jobs.html', context)

def job_detail(request, job_id):
    job_list = Job.objects.get(id=job_id)
    print(job_list)
    context = {'job': job_list}
    return render(request, 'job/job_details.html', context)
    