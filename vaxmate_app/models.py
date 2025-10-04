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

class FamilyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="family_members")
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    relation = models.CharField(max_length=50)
    vaccine_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    notification_type = models.CharField(max_length=50, choices=[
        ("Email", "Email"),
        ("SMS", "SMS"),
        ("App Notification", "App Notification")
    ])

    def __str__(self):
        return f"{self.name} ({self.relation})"