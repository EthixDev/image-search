from django.contrib import admin

from app.models import Image

# Register your models here.

class ImageAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'title','image','feature_vector'
    ]


admin.site.register(Image, ImageAdmin)