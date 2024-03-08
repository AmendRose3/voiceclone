from django.db import models
from django.contrib.auth.models import User 
from datetime import date

class regmodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact=models.CharField(max_length=10)
    date=models.DateField()
    

# class textmodel(models.Model):
#     field1=models.CharField(max_length=50,null=True)








