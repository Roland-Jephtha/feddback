
from django.db import models

class Feedback(models.Model):
    POSITION_CHOICES = [
        ("Staff", "Staff"),
        ("Student", "Student"),
        ("Contractor", "Contractor"),
        ("Others", "Others"),
    ]
    RATING_CHOICES = [
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Very Good", "Very Good"),
        ("Fair", "Fair"),
    ]
    FEEDBACK_SATISFACTION_CHOICES = [
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Very Good", "Very Good"),
        ("Fair/Poor", "Fair/Poor"),
    ]

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    services_requested = models.TextField(blank=True)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES)
    complaint = models.TextField(blank=True)
    department = models.CharField(max_length=255, blank=True)
    staff_name = models.CharField(max_length=255, blank=True)
    suggestions = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    feedback_satisfaction = models.CharField(max_length=20, choices=FEEDBACK_SATISFACTION_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.position})"
