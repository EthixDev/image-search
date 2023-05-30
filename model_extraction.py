
import torch
from torchvision import models
from torch import nn

model = models.vgg19(pretrained=True)

new_classifier =  model.classifier[:-3]
model.classifier = new_classifier
print(model)
torch.save(model, 'model.pt')











