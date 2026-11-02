"""
models.py
=========
Extended user profile model storing extra fields with regex-validated data.
"""

from django.db import models
from django.contrib.auth.models import User
from .validators import validate_phone, validate_full_name


class UserProfile(models.Model):
    """Extended profile linked one-to-one with Django's built-in User model."""

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user       = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name  = models.CharField(max_length=50, validators=[validate_full_name])
    phone      = models.CharField(max_length=15, validators=[validate_phone], blank=True)
    gender     = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    bio        = models.TextField(max_length=300, blank=True)
    joined_on  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} (@{self.user.username})"

    class Meta:
        verbose_name = 'User Profile'
