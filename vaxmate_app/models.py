from django.db import models
from django.contrib.auth.models import User

class Update(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male','Male'),('Female','Female')], blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

