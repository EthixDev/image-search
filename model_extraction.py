# import sys
# sys.path.append('..')
import torch
from torchvision import models
from torch import nn
# from PIL import Image
# import torchvision.transforms as transforms

# # device = torch.device('cuda', if torch.cuda.is_available() else 'cpu')
# model = models.resnet50(pretrained=True)
# print(model)

# for param in model.parameters():
#     param.requires_grad = False


# Load the pretrained model from pytorch
# def get_feature_vector(path):
res = models.resnet50(pretrained=True)
model = nn.Sequential(*list(res.children())[:-2])
layer7_2 = nn.Sequential(*list(model[7][2].children())[:-2])
model[7][2] = layer7_2
print(model)
torch.save(model, 'model.pt')


# new_layer4 = model.layer4[2][:5]
# model.layer4 = new_layer4
# print(model)

# my_new_model = res
# my_new_model.avgpool = nn.Identity()
# my_new_model.fc = nn.Identity()
# my_new_model.classifier = new_classifier
# torch.save(my_new_model, 'model.pt')









