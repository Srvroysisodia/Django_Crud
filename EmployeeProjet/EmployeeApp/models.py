from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
gender_choice = [
    ('Male','M'),
    ('Female','F'),
    ('Other','O'),
]

qualification = [
    ('B-tech','B-tech'),
    ('BCA','BCA'),
]

experience = [
    ('0','Fresher'),
    ('3','three months'),
    ('6+','Six months +'),
]
awards=[
    ('best emp of month','BEOM'),
    ('best emp of Year','BEOY'),
]

class Position(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Nick(models.Model):
    title= models.CharField(max_length=10)

    def __str__(self):
        return self.title
    

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name =models.CharField(max_length=10)
    emp_qual = models.CharField(max_length=10,choices=qualification,default=0)
    emp_mobile = models.IntegerField()
    emp_email= models.EmailField()
    emp_gender = models.CharField(max_length=10,choices=gender_choice,default=gender_choice[1])
    emp_sal = models.IntegerField()
    emp_position = models.ForeignKey(Position,on_delete=models.CASCADE)
    emp_add = models.TextField(max_length=10)
    emp_experience = models.CharField(max_length=20,choices=experience,default=experience[2])
    emp_awards = models.CharField(max_length=17,choices=awards,default=awards[0])
    emp_nick = models.ForeignKey(Nick,on_delete=models.CASCADE,null=True)