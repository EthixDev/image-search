from django.db import models

# Create your models here.


class Image(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to='media',null=True, blank=True)
    discrpition = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    feature_vector = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

