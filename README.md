# EyeQ-Analyzer-Multiclass-OCT-Disease-Detection
EyeQ Analyzer is a system for classifying Optical Coherence Tomography (OCT) images into four categories:  
- **CNV (Choroidal Neovascularization)**  
- **DRUSEN**  
- **DME (Diabetic Macular Edema)**  
- **NORMAL**  

By combining traditional Digital Image Processing (DIP) techniques with advanced machine learning and deep learning approaches, the project achieves high diagnostic accuracy and scalability, making it a valuable tool for retinal disease detection.  

---

## Table of Contents  
- [Introduction](#introduction)  
- [Features](#features)  
- [Methodology](#methodology) 
- [Results](#results)   

---

## Introduction  

Retinal diseases like **CNV**, **DRUSEN**, and **DME** are leading causes of vision impairment globally. Early detection through OCT imaging is crucial but often limited by the subjectivity and time constraints of manual diagnosis. The **EyeQ Analyzer** project addresses these challenges by automating the disease detection process using a hybrid approach of **traditional image processing** and **deep learning models**.  

The system preprocesses raw OCT images using advanced DIP techniques such as **non-local mean filtering**, **Otsu thresholding**, and **median filtering**. It then employs machine learning and deep learning models, including **SVM**, **CNN**, **VGG16**, and **ResNet50**, to classify images with high accuracy.  

---

## Features
EyeQ Analyzer offers the following key features:

### Automated Disease Classification:
#### Classifies OCT images into four categories:

- CNV (Choroidal Neovascularization)
- DRUSEN
- DME (Diabetic Macular Edema)
- NORMAL
  
### Hybrid Approach:
Integrates traditional machine learning techniques, such as HOG (Histogram of Oriented Gradients) and Local Binary Patterns (LBP), with advanced deep learning models like CNN, VGG16, and ResNet50.

### Advanced Preprocessing Techniques:
#### Enhances image quality and reduces noise through techniques like:

- Non-local mean filtering for noise reduction.
- Otsu thresholding for segmentation.
- Median filtering for final noise removal.
  
### Scalability and Accuracy:
Designed to process large datasets efficiently while maintaining high accuracy in disease classification.

## Methodology
The EyeQ Analyzer follows a structured methodology to ensure optimal performance:

1. Image Quality Analysis:

Evaluates the dataset for quality and consistency using metrics such as:
- Histogram similarity
- Sharpness threshold
- Brightness analysis
- Structural Similarity Index (SSIM)
- Duplicate detection
  
2. Image Preprocessing:

Prepares raw OCT images through advanced Digital Image Processing (DIP) techniques:
- Filling white borders with black pixels.
- Applying non-local mean filtering for noise reduction.
- Performing Otsu thresholding for segmentation.
- Using median filtering for enhanced image clarity.
  
3. Feature Extraction and Model Selection:

- Traditional Methods:
  - HOG (Histogram of Oriented Gradients)
  - Local Binary Patterns (LBP)
- Deep Learning Models:
  - CNN (Convolutional Neural Networks)
  - VGG16 with data normalization, augmentation, and a learning rate of 1e-4.
  - ResNet50 with similar preprocessing steps and a learning rate of 0.0001.
    
4. Classification:

- Outputs one of four categories: CNV, DRUSEN, DME, or NORMAL.

## Results
The EyeQ Analyzer achieved the following results during evaluation:

- Models Used:

  - VGG16:
    - Optimized with data normalization and augmentation.
    - Achieved high accuracy on preprocessed datasets.
  - ResNet50:
    - Demonstrated excellent performance with a learning rate of 0.0001.
    - Robust in handling noise and variations in the data.
- Evaluation Metrics:

  - Metrics used to evaluate model performance include:
    - Precision
    - Recall
    - F1-Score
    - Accuracy
- Highlights:

  - The non-local mean filter significantly improved the signal-to-noise ratio in images.
  - Both VGG16 and ResNet50 models outperformed traditional approaches in terms of classification accuracy and robustness.
