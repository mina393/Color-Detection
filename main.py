import cv2  # Import OpenCV for video capture and image processing
from PIL import Image  # Import PIL to manipulate the image and detect bounding boxes
from Color_Detection import get_limits  # Import custom function from util.py to get color limits

blue = (255, 0, 0)  # Define the color blue in BGR format
cap = cv2.VideoCapture(0)  # Start video capture from the default camera (index 0)

while True:
    ret, frame = cap.read()  # Read each frame from the camera

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame from BGR to HSV color space

    lowerLimit, upperLimit = get_limits(color=blue)  # Get the lower and upper HSV limits for the color blue

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)  # Create a binary mask where the blue areas are white

    mask_ = Image.fromarray(mask)  # Convert the mask to a PIL image to use its getbbox() method

    bbox = mask_.getbbox()  # Get the bounding box around the white areas (detected color)

    if bbox is not None:  # If a bounding box is found
        x1, y1, x2, y2 = bbox  # Extract the coordinates of the bounding box

        # Draw a green rectangle around the detected blue object
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)  # Display the video frame with the detected object

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit the loop when the 'q' key is pressed
        break

cap.release()  # Release the camera resource

cv2.destroyAllWindows()  # Close all OpenCV windows
