import cv2
import numpy as np
import exifread
from skimage.restoration import estimate_sigma
from matplotlib import pyplot as plt

# Extract Metadata
def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as img_file:
            tags = exifread.process_file(img_file)
            if not tags:
                print("No EXIF data found.")
                return None
            # Convert tags to a dictionary with string values
            return {tag: str(tags[tag]) for tag in tags}
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None
    except Exception as e:
        print(f"Error reading EXIF data: {e}")
        return None

# Error Level Analysis (ELA)
def error_level_analysis(image_path):
    img = cv2.imread(image_path)
    cv2.imwrite('compressed.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    
    img_original = cv2.imread(image_path)
    img_compressed = cv2.imread('compressed.jpg')

    ela_image = cv2.absdiff(img_original, img_compressed)
    return ela_image

# Image Noise Analysis
def noise_analysis(image_path):
    image = cv2.imread(image_path)  # Loads image with multiple channels (e.g., RGB)
    sigma = estimate_sigma(image, channel_axis=-1)  # Automatically detects if the image is multichannel
    return sigma

# Full analysis function
def analyze_image(image_path):
    ela_result = error_level_analysis(image_path)
    noise_level = noise_analysis(image_path)

    # Save ELA result as image (for visualization in frontend)
    ela_path = 'uploads/ela_result.jpg'
    cv2.imwrite(ela_path, ela_result)

    return {
        'ela_image_path': ela_path,
        'noise_level': noise_level
    }
