import cv2
import numpy as np
from skimage.measure import shannon_entropy
import cv2

# Function to compute Local Variance focus measure
def compute_local_variance(image, ksize=5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean = cv2.blur(gray, (ksize, ksize))
    squared_mean = cv2.blur(gray**2, (ksize, ksize))
    variance = squared_mean - (mean**2)
    return np.mean(variance)

 
def compute_entropy(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return shannon_entropy(gray)


def compute_tenengrad(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Sobel filter in X direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Sobel filter in Y direction
    tenengrad = np.sqrt(sobel_x**2 + sobel_y**2)  # Compute gradient magnitude
    return np.mean(tenengrad)  # Return mean gradient magnitude as focus score


def compute_brenner_gradient(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    shifted = np.roll(gray, -2, axis=1)  # Shift by 2 pixels horizontally
    diff = (gray - shifted) ** 2  # Compute squared difference
    return np.sum(diff)  # Sum all differences as the focus measure


def compute_sobel_variance(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X gradient
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y gradient
    sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)  # Compute gradient magnitude
    variance = np.var(gray)  # Compute variance of pixel intensities
    return np.mean(sobel_magnitude) + variance  # Combine Sobel and variance

def compute_laplacian(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)  # Apply Laplacian filter
    return np.var(laplacian)  # Compute variance of Laplacian






videoPath = "Floux.png"
cap = cv2.VideoCapture(videoPath)
focus_scores = []
frames = []
 
# Include the function for focus measures here
# def compute_focus_measure(image):
 
#     Implement the focus measure function here (e.g., Tenengrad, Brenner, etc.)
if cap.isOpened():
    print("Video file successfully retrieved")
else:
    print("Video file wasn't retrieved properly")
while True:
    ret, frame = cap.read()
    if ret:
        focus_scores.append(compute_entropy(frame))  # Replace with actual function
        frames.append(frame)
    else:
        print("Frame not read")
        break
cap.release()
 
# Find the best-focused frame
best_score_index = np.argmax(focus_scores)
best_frame = frames[best_score_index]
print(f"Best frame index: {best_score_index} with score {focus_scores[best_score_index]}")
 
# Get the original dimensions
original_height, original_width = best_frame.shape[:2]
new_width = 600
aspect_ratio = new_width / original_width
new_height = int(original_height * aspect_ratio)  # Compute height based on aspect ratio
 
# Resize the image
resized_image = cv2.resize(best_frame, (new_width, new_height))
 
# Display the best frame
cv2.imshow("Best Frame", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




