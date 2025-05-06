from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.job_list),
    path('<int:job_id>',views.job_detail),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


