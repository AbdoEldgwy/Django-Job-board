from django.db import models

# Create your models here.
Job_TYPE = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('contract', 'Contract'),
    ('internship', 'Internship'),
)
def upload_location(instance, filename):

    return "%s/%s" % (instance.id, filename)

class Job(models.Model):
    title = models.CharField(max_length=50) 
    # locataion
    job_type = models.CharField(max_length=15,choices=Job_TYPE)
    description = models.TextField(max_length=1000)
    published_date = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    experienceYear = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    img = models.ImageField(upload_to=upload_location, default='images/default.png')

    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    # job = models.ManyToManyField(Job,related_name='categories')
    def __str__(self):
        return self.name