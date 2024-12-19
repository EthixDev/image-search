
import torch
from PIL import Image
from torchvision import transforms


def get_feature_vector(path):
    # Load the pretrained model from pytorch
    my_model = torch.load('model.pt')
    my_model.eval()  # Set model to evaluation mode (important for inference)
    
    # Disable gradients since we're only doing inference
    for param in my_model.parameters():
        param.requires_grad = False

    # Load the image
    img = Image.open(path)

    # Convert image to RGB if it has an alpha channel (RGBA)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Define the transforms
    transform = transforms.Compose([
        transforms.Resize(256),         # Resize to 256x256
        transforms.CenterCrop(224),     # Crop to 224x224
        transforms.ToTensor(),          # Convert image to Tensor
        transforms.Normalize(           # Normalize using mean and std for ImageNet
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    # Apply the transforms to the image
    img_tensor = transform(img)

    # Add a batch dimension (i.e., make it a 4D tensor: [batch_size, channels, height, width])
    img_tensor = img_tensor.unsqueeze(0)  # Shape: [1, 3, 224, 224]

    # Run the image through the model to get the feature vector
    with torch.no_grad():  # No need to calculate gradients during inference
        output = my_model(img_tensor)  # Output shape depends on the model

    # Squeeze the output to remove extra dimensions (if necessary)
    output = output.squeeze()  # Shape: [num_features] or [num_classes] based on your model

    return output


if __name__ == "__main__":

    path = 'media/cat.2636.jpg'
    output = get_feature_vector(path)
    print(output.shape)
    print(output)