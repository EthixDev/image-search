from django.contrib import admin
from django.urls import path
from myapp.views import create_feature_vector,index,image_detail

urlpatterns = [
   path('create/<int:id>', create_feature_vector, name='create'),
   path('index/', index, name='index'),
   path('get/<int:id>', image_detail, name='detail_image'),
]
