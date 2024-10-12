import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to calculate histogram
def calculate_histogram(image):
    # Convert image to grayscale if needed
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate histogram of grayscale image
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    # Normalize the histogram
    hist = cv2.normalize(hist, hist).flatten()
    return hist

# Path to the folder containing images
folder_path = '/Users/sheenamittal/Desktop/work /DIP/Dataset - train+val+test/train/CNV'

# Load the ideal image
ideal_image = cv2.imread('image.png')

# Get all image file names from the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# List to store similarity scores
similarities = []

for file_name in image_files:
    # Build the full file path
    image_path = os.path.join(folder_path, file_name)
    
    # Load the image
    image = cv2.imread(image_path)
    
    # Resize the dataset image to match the ideal image
    resized_image = cv2.resize(image, (ideal_image.shape[1], ideal_image.shape[0]))
    
    # Calculate histograms
    hist1 = calculate_histogram(ideal_image)
    hist2 = calculate_histogram(resized_image)
    
    # Compare histograms using correlation (can use other methods)
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    similarities.append(similarity)

# Plot histogram of similarities
plt.hist(similarities, bins=20, color='blue', alpha=0.7)
plt.title('Histogram of Image Similarities to Ideal Image')
plt.xlabel('Similarity Score')
plt.ylabel('Number of Images')
plt.show()
