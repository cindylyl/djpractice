from django.conf.urls import url
from .views import profile

urlpatterns =[
    url(r'^(?P<stu_id>\d+)', profile, name='stu_id'),
]