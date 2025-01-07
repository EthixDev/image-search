from django.shortcuts import render, HttpResponse
from helper import get_feature_vector
import torch
import json
from django.http import HttpResponse
from .forms import UploadImageForm
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app import models
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response



from django.http import JsonResponse
from .models import Image



def create_feature_vector(request):
    all_images = models.Image.objects.filter(feature_vector__isnull=True)
    for image in all_images:
        path = image.image.path
        final_output = get_feature_vector(path)
        final_output = final_output.to(torch.float64)
        my_data = {"fv": list(final_output.numpy())}
        my_data = json.dumps(my_data)
        image.feature_vector = my_data
        # my_image.name = 'new namel'
        image.save()

    return HttpResponse("Successfully created feature vector!")


def index(request):
    return render(request, "app/index.html")


def all_posts(request):
    return render(request, "app/all.html")

def search_images(request):
    return render(request, "app/search.html")

def image_detail(request, id):
   
    return render(
        request,
        "app/detail.html", 
    )



def image_details(request, id):
    try:
        selected_image = Image.objects.get(id=id)
        return JsonResponse({
            "Image_found": True,
            "id": selected_image.id,
            "name": selected_image.title,
            "content": selected_image.discrpition,
            "image_url": selected_image.image.url,
        })
    except Image.DoesNotExist:
        return JsonResponse({"Image_found": False}, status=404)

def get_latest_images(request):
    images = Image.objects.all().order_by("-image")[:3]
    data = [
        {
            "id": image.id,
            "title": image.title,
            "description": image.discrpition,
            "url": image.image.url,
        }
        for image in images
    ]
    return JsonResponse({"images": data})


def all_images(request):
    search_query = request.GET.get('search', '')
    page = request.GET.get('page', 1)

    # Filter images based on the search query
    all_posts = models.Image.objects.filter(title__icontains=search_query).order_by("-image")

    # Paginate the results
    paginator = Paginator(all_posts, 9)  # 9 items per page
    page_obj = paginator.get_page(page)

    # Serialize the data
    posts_data = [
        {
            "id": post.id,
            "title": post.title,
            "description": post.discrpition,
            "image_url": post.image.url,
        }
        for post in page_obj
    ]

    return JsonResponse({
        "posts": posts_data,
        "pagination": {
            "has_previous": page_obj.has_previous(),
            "has_next": page_obj.has_next(),
            "current_page": page_obj.number,
            "total_pages": paginator.num_pages,
        },
    })






@api_view(['POST'])
def search_similar_images(request):
    """
    API endpoint to search for similar images.
    """
    if 'image' not in request.FILES:
        return Response({"error": "No image file uploaded."}, status=400)

    image_file = request.FILES['image']
    
    # Extract the feature vector from the uploaded image
    feature_vector = get_feature_vector(image_file)
    feature_vector = feature_vector.reshape(1, -1)

    # Retrieve all feature vectors from the database
    all_images = Image.objects.all()
    all_feature_vectors = [json.loads(img.feature_vector)['fv'] for img in all_images]
    all_feature_vectors = np.array(all_feature_vectors)

    # Calculate similarity scores
    similarity_scores = cosine_similarity(feature_vector, all_feature_vectors).flatten()
    indices_sorted = np.argsort(similarity_scores)[::-1]  # Sort in descending order

    # Get top N similar images (e.g., top 5)
    top_indices = indices_sorted[:5]
    similar_images = [all_images[i] for i in top_indices]
    similar_images_data = [{"id": img.id, "url": img.image.url} for img in similar_images]

    return Response({"similar_images": similar_images_data})
