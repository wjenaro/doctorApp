from django.db import models


class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.TextField(max_length=100)
    password=models.TextField(max_length=100)
    #will include other fields later 
