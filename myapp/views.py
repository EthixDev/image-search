from django.shortcuts import render, HttpResponse
from helper import get_feature_vector
import torch
import json
from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from .forms import UploadImageForm
from django.http import JsonResponse
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
from myapp import models

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

    return HttpResponse('Successfully created feature vector!')
def index(request):
    images = models.Image.objects.all().order_by('name')[:3]

    return render(request, "myapp/index.html", 
                  {
                    'images' : images
                  })


def image_detail(request, id):
    try:
      selected_image = models.Image.objects.get(id=id)
    
      return render(request, "myapp/detail.html",{

          'Image_found' : True,
          'image' : selected_image,
      })
    except Exception as exc:
       return render(request, "myapp/detail.html",{
          'Image_found' : False,
       })


def search_images(request):

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Do something with the uploaded file
            image = form.cleaned_data['image']
            feature_vector = get_feature_vector(image)
            feature_vector = feature_vector.reshape(1,-1)
            # Get all feature vectors from database
            all_images = models.Image.objects.all()
            all_feature_vectors = []
            for b in all_images:
                all_feature_vectors.append(json.loads(b.feature_vector)['fv'])
            all_feature_vectors = np.array(all_feature_vectors)
            # all_feature_vectors = np.array([json.loads(b.feature_vector)['fv'] for b in all_images])

            # Calculate similarity scores
            similarity_scores = cosine_similarity(feature_vector, all_feature_vectors)
            similarity_scores_falt = similarity_scores.flatten()
            indices_sorted = np.argsort(similarity_scores_falt)
            top_indices = indices_sorted[-2:][::-1]
            top_indices = [index.item() for index in top_indices]
            similar_images = [all_images[i] for i in list(top_indices)]

            # Return the similar images
            # You might want to return more information here, like the actual similarity scores
            form = UploadImageForm()
            
            context={
                 'similar_images': similar_images,
                 'form':form
            }
            response = render(request,'myapp/search.html',context)
            return response

    else:
        form = UploadImageForm()
    response = render(request, 'myapp/search.html', {'form': form})
    return response

