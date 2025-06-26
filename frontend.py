import streamlit as st
from source_code import compress_image
import numpy as np
from PIL import Image
st.title("Compress your image")

uploaded_file = st.file_uploader("Choose your file format", type=["png", "jpg", "jpeg"])


if uploaded_file is not None:
    pil_image = Image.open(uploaded_file)

    # Display original image
    st.image(pil_image, caption="Original Image", use_column_width=True)

    # Convert to NumPy array
    img_np = np.array(pil_image)
    st.write("**File Name:**", uploaded_file.name)
    st.write("**File Type:**", uploaded_file.type)
    st.write("**File Size (bytes):**", uploaded_file.size)
    compressed_image = compress_image(img_np, k=15)  # Compress the image with k=15 clustersS
    st.image(compressed_image, caption="Compressed Image")
