from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.auth.models import User

def generate_tracking_id():
    import uuid
    return str(uuid.uuid4())[:8]

class SchemeReport(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('financial', 'Financial'), ('pyramid', 'Pyramid'), ('other', 'Other')])
    evidence = models.FileField(upload_to='evidence/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tracking_id = models.CharField(max_length=10, unique=True, default=generate_tracking_id)

    def __str__(self):
        return f"Sky Report {self.tracking_id}"

# Function to generate a unique tracking ID
def generate_tracking_id():
    return str(uuid.uuid4())[:8]

class SchemeReport(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('financial', 'Financial'), ('pyramid', 'Pyramid'), ('other', 'Other')])
    evidence = models.FileField(upload_to='evidence/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    tracking_id = models.CharField(max_length=10, unique=True, default=generate_tracking_id)  # Use the function here

    def __str__(self):
        return f"Sky Report {self.tracking_id}"

class Verification(models.Model):
    report = models.OneToOneField(SchemeReport, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    is_legitimate = models.BooleanField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

class CounselingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(SchemeReport, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)