import numpy as np  # Import NumPy for handling arrays
import cv2  # Import OpenCV for color conversions

def get_limits(color):
    # Reshape color array to be a proper 3-channel image (1x1 image with the given color)
    c = np.uint8([[color]])

    # Convert the color from BGR to HSV format for easier color detection
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Define lower and upper limits for the HSV range around the target color
    # Hue range is +/- 10 around the target hue, and fixed saturation and value ranges
    lowerLimit = hsvC[0][0][0] - 10, 100, 100  # Lower bound for hue, saturation, and value
    upperLimit = hsvC[0][0][0] + 10, 255, 255  # Upper bound for hue, saturation, and value

    # Convert the limits to NumPy arrays for use in OpenCV functions
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit  # Return the HSV limits for the color
