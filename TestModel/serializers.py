from django.contrib.auth.models import User, Group
from .models import Students
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ('stu_id','stu_fname','stu_lname','stu_birth_date','stu_join_date')