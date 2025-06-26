import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image
import io

def compress_image(image_array, k=15):
    """
    Compress an image using K-means clustering.
    
    Parameters:
    - image_path: str, path to the input image
    - k: int, number of clusters for K-means
    
    Returns:
    - compressed_image: PIL Image object of the compressed image
    """
    
    
    h, w, c = image_array.shape  # Get dimensions of the image
    image_pixels = image_array.reshape(-1, 3)  # Reshape to a 2D array
    
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(image_pixels)
    
    new_colors = kmeans.cluster_centers_.astype('uint8')
    labels = kmeans.labels_
    
    compressed_img = new_colors[labels].reshape(h, w, 3)  # Reshape back to original dimensions
    return Image.fromarray(compressed_img)

"""
fig, ax = plt.subplots(1, 2, figsize=(10, 5))


ax[0].imshow(image_array)
ax[0].set_title("Original")
ax[0].axis('off')
ax[1].imshow(compressed_img)
ax[1].set_title(f"Compressed (k={k})")
ax[1].axis('off')
plt.tight_layout()
plt.show()




compressed_pil = Image.fromarray(compressed_img)
buffer = io.BytesIO()
compressed_pil.save(buffer, format="JPEG", quality=90)  
size_bytes = len(buffer.getvalue())
size_kb = size_bytes / 1024
size_mb = size_kb / 1024

print(f"Compressed Image Size (in memory): {size_bytes} bytes ({size_kb:.2f} KB / {size_mb:.2f} MB)")

"""