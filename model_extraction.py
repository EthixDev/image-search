
import torch
from torchvision import models
from torch import nn

model = models.resnet50(pretrained=True)
modules = list(model.children())[:-1]
model = nn.Sequential(*modules)

torch.save(model, 'model.pt')











