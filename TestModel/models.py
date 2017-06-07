from django.db import models
from datetime import date,time


# Create your models here.
class Testing(models.Model):
    def __str__(self):
        return self.t_name
    t_name = models.CharField(max_length=100)
    t_method = models.CharField(max_length=100)


class Student(models.Model):
    stu_fname = models.CharField(max_length=100)
    stu_lname = models.CharField(max_length=100)
    stu_birth_date = models.DateField('birthday', default=date(1990, 1, 1))
    stu_join_date = models.DateField('join date', default=date.today)


class Instructor(models.Model):
    ins_id = models.AutoField(primary_key=True)
    ins_name = models.CharField(max_length=20)
    ins_birth_date = models.DateField('instructor birthday', default=date(1980,1,1))
    ins_phone = models.CharField(max_length=30)
    ins_email = models.EmailField()
    ins_address = models.CharField(max_length=100)


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_time = models.TimeField('class time',default=time(10,0,0))
    class_dayOfTheWeek = models.CharField(max_length=20)
    class_level = models.CharField(max_length=20)
    class_location = models.CharField(max_length=20)
    ins_id = models.ForeignKey(Instructor)


class Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    meeting_date = models.DateField(default=date.today)
    class_id = models.ForeignKey(Class)


class Students(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    stu_id = models.AutoField(primary_key=True)
    stu_fname = models.CharField(max_length=100)
    stu_lname = models.CharField(max_length=100)
    stu_birth_date = models.DateField('birthday',default=date(1990,1,1))
    stu_join_date = models.DateField('join date',default=date.today)
    stu_phone = models.CharField(max_length=30,null=True)
    stu_email = models.EmailField(null=True)
    stu_address = models.CharField(max_length=100,null=True)
    meeting_id = models.ForeignKey(Meeting,default=4001)
    ins_id=models.ForeignKey(Instructor,default=2001)


class Parent(models.Model):
    par_id = models.AutoField(primary_key=True)
    par_phone= models.CharField(max_length=30)
    par_email = models.EmailField()
    stu_id = models.ForeignKey(Students)


class Rank(models.Model):
    rank_id = models.AutoField(primary_key=True)
    rank_name = models.CharField(max_length=20)
    rank_belt_color = models.CharField(max_length=20)


class Gain(models.Model):
    stu_id = models.ForeignKey(Students,null=True)
    rank_id = models.ForeignKey(Rank,default=5001)
    gain_date = models.DateField(default=date.today)

    class Meta:
        unique_together = (('stu_id', 'rank_id'),)


class Requirement(models.Model):
    req_id = models.AutoField(primary_key= True)
    req_info = models.CharField(max_length=100)
    rank_id = models.ForeignKey(Rank)


class Invoice(models.Model):
    inv_id = models.AutoField(primary_key=True)
    inv_date = models.DateField(default=date.today)
    inv_info = models.CharField(max_length=100)
    stu_id = models.ForeignKey(Students)


class Purchasing(models.Model):
    pur_id = models.AutoField(primary_key=True)
    pur_item_name= models.CharField(max_length=30)
    inv_id = models.ForeignKey(Invoice)


class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    stu_id = models.ForeignKey(Students,null=True)
