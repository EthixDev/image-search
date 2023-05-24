from django.contrib import admin
from django.urls import path
from myapp.views import create_feature_vector

urlpatterns = [
   path('create/<int:id>', create_feature_vector, name='create')
]
