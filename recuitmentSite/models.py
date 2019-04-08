from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Actiontype(models.Model):
    type_action = models.CharField(max_length=20, null=True)
    accept = models.IntegerField(default=0)
    reject = models.IntegerField(default=0)

    def __str__(self):
        return self.type_action

class Employeedetails(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    phone =  models.CharField(max_length=17, blank=True)
    d_b = models.CharField(max_length=10,null=True)
    email =  models.EmailField(blank=True, unique=True)
    location = models.CharField(max_length=20,null=True)
    organisation = models.CharField(max_length=20,null=True)
    experience = models.FloatField(default=0)
    re_experience = models.FloatField(default=0)
    designation = models.CharField(max_length=20, null=True)
    skills = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=20, null=True)
    action_type = models.CharField(max_length=20, null=True)
    action = models.IntegerField(default=0)
    # action_type = models.ForeignKey(Actiontype ,on_delete=models.CASCADE)


    def __str__(self):
        return self.fname

class Employee_details_list(models.Model):
    name = models.ForeignKey(Employeedetails ,on_delete=models.CASCADE)
    action_type = models.ForeignKey(Actiontype ,on_delete=models.CASCADE)


    def __str__(self):
        return self.name