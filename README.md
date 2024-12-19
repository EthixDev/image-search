# Image Semantic Search Project

This project implements an Image Semantic Search system. It extracts feature vectors from images using a pre-trained deep learning model and searches for similar images based on cosine similarity.

## Features
- Extract feature vectors from images using a VGG19 model.
- Store and retrieve feature vectors for efficient similarity search.
- A Django web application for image upload, search, and display.

---

## Getting Started

### Prerequisites
1. **Python**: Ensure you have Python 3.8 or above installed.
2. **Virtual Environment**: Use `venv` or any virtual environment manager.

---

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd image_semantic_search
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 1: Preprocess the Model
1. Run the `model_extraction.py` file to create the feature extraction model:
   ```bash
   python model_extraction.py
   ```
   This step saves a modified version of the VGG19 model (`model.pt`) with the last few layers removed for feature extraction.

---

### Step 2: Start the Django Application
1. Apply migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

2. Open the application in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage
1. Upload an image using the search feature.
2. The system extracts the image's feature vector and compares it with stored images.
3. Similar images are displayed based on cosine similarity.

---

## Project Structure

```plaintext
image_semantic_search/
├── data/                  # Dataset or images for testing
├── media/                 # Uploaded media files
├── model_extraction.py    # Script to modify and save the pre-trained model
├── helper.py              # Utility functions (e.g., `get_feature_vector`)
├── manage.py              # Django management script
├── myapp/                 # Django application
├── requirements.txt       # Project dependencies
├── venv/                  # Python virtual environment
```

---

## Important Files

### `model_extraction.py`
This script modifies the VGG19 model, removing the last three layers for feature extraction. The modified model is saved as `model.pt`.

### `helper.py`
Defines the `get_feature_vector` function, which:
- Loads the pre-trained model (`model.pt`).
- Processes input images (resize, normalize, etc.).
- Extracts and returns feature vectors for similarity comparison.

---

## Example Code

### Extracting Feature Vectors
```python
from helper import get_feature_vector

path = 'media/sample_image.jpg'
feature_vector = get_feature_vector(path)
print(feature_vector.shape)
```

### Searching for Similar Images
Refer to `views.py` in the `search_images` function for detailed implementation using cosine similarity.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- Pre-trained models provided by [PyTorch](https://pytorch.org).
- Frontend styled using [Tailwind CSS](https://tailwindcss.com).
