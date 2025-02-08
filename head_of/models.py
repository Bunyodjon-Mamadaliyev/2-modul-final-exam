from django.db import models
from departments.base_models import BaseModel
from django.shortcuts import reverse
from django.conf import settings


class HeadDepartment(BaseModel):
    STATUS_CHOICES = [
        ('ac', 'Active'),
        ('in', 'Inactive'),
        ('pd', 'Pending'),
    ]

    name = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='in')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def get_update_url(self):
        return reverse('head_of:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('head_of:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"