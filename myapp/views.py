from django.shortcuts import render, HttpResponse
from myapp.models import Image
# import json
from helper import get_feature_vector
import torch
import json


def create_feature_vector(request, id):

    my_image = Image.objects.get(id=id)
    path = my_image.file.path

    final_output = get_feature_vector(path)
    final_output = final_output.to(torch.float64)
    my_data = {"fv": list(final_output.numpy())}
    my_data = json.dumps(my_data)
    my_image.feature_vector = my_data
    # my_image.name = 'new namel'
    my_image.save()

    return HttpResponse('Successfully created feature vector!')
