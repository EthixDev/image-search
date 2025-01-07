from django.urls import path
from app.views import create_feature_vector, get_latest_images,image_detail, image_details, search_images,all_posts,search_similar_images

urlpatterns = [
   path('create/', create_feature_vector, name='create'),
   # path('index/', index, name='index'),
   path("posts/", all_posts, name='posts'),
   path('get/<int:id>', image_detail, name='detail_image'),
   path('search/', search_images, name='search_images'),
   path('search_similar_images/',search_similar_images),
   path("images/latest/", get_latest_images, name="get_latest_images"),
   path("images/", get_latest_images, name="get_latest_images"),
   path("image/<int:id>/", image_details, name="get_image"),

   


]
