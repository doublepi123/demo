from django.db import models
from django.contrib import admin


# Create your models here.
class Student(models.Model):
    # 姓名
    name = models.CharField(max_length=20)
    # 学号
    stu_id = models.CharField(max_length=20, primary_key=True)
    # 电话号码
    phone = models.CharField(max_length=20)
    # 出生日期
    birthdate = models.DateField()
    # 家庭人数
    people = models.IntegerField()
    # 家庭收入
    income = models.FloatField()
    # 特殊情况
    special = models.CharField(max_length=200)


admin.site.register(Student)
