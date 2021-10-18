from django.db import models

from django.db import models

# class homework(models.Model):
#     #pr1
#     name = models.CharField(max_length=30,null=True)
#     #pr2
#     age = models.IntegerField(default=18,blank=True)
# pr3
# 'car.apps.CarConfig',
# 'user.apps.UserConfig'
# pr4
#  python manage.py makemigrations myfirstapp
# python manage.py migrate myfirstapp
class pr5_student(models.Model):
    styear = (
        ('F','Freshman'),
        ('S','Sophomore'),
        ('J','Junior'),
        ('S','Senior')
    )
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    major = models.CharField(max_length=50)
    student_year = models.CharField(max_length=1,choices=styear)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)

class Adress(models.Model):
    street = models.CharField(max_length=100)
    house = models.IntegerField()
    city = models.CharField(max_length=100)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)

# class Musician(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     instrument = models.CharField(max_length=100)
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()
#
# class Owner(models.Model):
#     name = models.CharField(max_length=50, null=False)
#
#
# class Dog(models.Model):
#     name = models.CharField(max_length=50,null=False)
#     owner = models.ForeignKey(Owner,on_delete=models.CASCADE)
#     breed = models.CharField(max_length=50)
#     age = models.IntegerField(default=1)






# Create your models here.
