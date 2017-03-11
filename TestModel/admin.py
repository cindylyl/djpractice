from django.contrib import admin
from .models import User,Student,Students,Invoice,Instructor,Parent,Purchasing,Rank,Requirement,Meeting,Class,Gain

# Register your models here.
class StuAdmin(admin.ModelAdmin):
    list_display = ('id','stu_fname','stu_lname','stu_birth_date','stu_join_date')
    search_fields = ('id','stu_fname','stu_lname','stu_birth_date','stu_join_date')


class StusAdmin(admin.ModelAdmin):
    list_display = ('stu_id','stu_fname','stu_lname','stu_birth_date','stu_join_date','stu_phone','stu_email',
                    'meeting_id','ins_id')


class InsAdmin(admin.ModelAdmin):
    list_display = ('ins_id','ins_name','ins_birth_date','ins_phone','ins_email','ins_address')

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('meeting_id','meeting_date','class_id')


class InvAdmin(admin.ModelAdmin):
    list_display = ('inv_id','inv_date','inv_info','stu_id')


class PurAdmin(admin.ModelAdmin):
    list_display = ('pur_id','pur_item_name','inv_id')


class ParAdmin(admin.ModelAdmin):
    list_display = ('par_id','par_phone','par_email','stu_id')

class RankAdmin(admin.ModelAdmin):
    list_display = ('rank_id','rank_name','rank_belt_color')

class ReqAdmin(admin.ModelAdmin):
    list_display = ('req_id','req_info','rank_id')

class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id','class_time','class_dayOfTheWeek','class_level','class_location','ins_id')

class GainAdmin(admin.ModelAdmin):
    list_display = ('stu_id','rank_id','gain_date')

admin.site.register(User)
admin.site.register(Student, StuAdmin)
admin.site.register(Students, StusAdmin)
admin.site.register(Instructor, InsAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Parent,ParAdmin)
admin.site.register(Gain, GainAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Requirement, ReqAdmin)
admin.site.register(Invoice, InvAdmin)
admin.site.register(Purchasing, PurAdmin)