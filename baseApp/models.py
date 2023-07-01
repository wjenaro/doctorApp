from django.db import models


class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.TextField(max_length=100)
    #email=models.TextField(max_length=100)
    password=models.TextField(max_length=100)
    #will include other fields later 


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    qualifications = models.CharField(max_length=255)
    experience = models.IntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    #average_rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.full_name
class Review(models.Model):
    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.doctor.full_name