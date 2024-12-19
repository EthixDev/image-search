from django.contrib import admin
from django.urls import path
from myapp.views import create_feature_vector,index,image_detail, search_images,all_posts

urlpatterns = [
   path('create/', create_feature_vector, name='create'),
   # path('index/', index, name='index'),
   path("posts/", all_posts, name='posts'),
   path('get/<int:id>', image_detail, name='detail_image'),
   path('search/', search_images, name='search_images'),
]
