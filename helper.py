
import torch
from PIL import Image
from torchvision import transforms


def get_feature_vector(path):

    # Load the pretrained model from pytorch
    my_model = torch.load('model.pt')
    for param in my_model.parameters():
        param.requires_grad = False

    # Load the image
    
    img = Image.open(path)

    # Define the transforms
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225])
    ])

    # Apply the transforms to the image
    img_tensor = transform(img)
    img_tensor = img_tensor.unsqueeze(0)

    output = my_model(img_tensor)
    output = output.squeeze()
    
    return output


if __name__ == "__main__":

    path = 'media/cat.2636.jpg'
    output = get_feature_vector(path)
    print(output.shape)
    print(output)