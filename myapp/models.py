from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to='media')
    feature_vector = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
