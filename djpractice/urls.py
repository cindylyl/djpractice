"""djpractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#from djpractice.view import hello
from TestModel import views
from TestModel.testdb import testdb
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'students',views.StudentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', views.hello),
    url(r'^testdb/$', testdb),
    #url(r'^profile/(?P<stu_id>\d+)/$', profile,name='profile'),
    url(r'^profile/', include('TestModel.urls',namespace='profile')),
    url(r'^edit/', views.edit_profile),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup),
    url(r'^report/', views.report),
    url(r'^report_filter/',views.report_filter),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
