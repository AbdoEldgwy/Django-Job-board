from django.shortcuts import render
from .models import Job, Category

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    print(job_list)
    context = {'jobs_list': job_list}

    return render(request, 'job/jobs.html', context)

def job_detail(request, job_id):
    job_list = Job.objects.get(id=job_id)
    double_salary = job_list.salary * 2
    print('double_salary:',double_salary)
    context = {'job': job_list,
               'double_salary': double_salary,
            }
    return render(request, 'job/job_details.html', context)
    