# Real-time Color Detection with OpenCV and PIL

This project demonstrates a real-time color detection system using a webcam feed, built with OpenCV and PIL (Python Imaging Library). The system identifies and tracks objects of a specified color (blue in this case), displaying a bounding box around the detected object on the video feed.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Future Improvements](#future-improvements)

## Overview

The project captures live video from a webcam and processes it in real-time to detect objects of a specific color (blue by default). It uses a custom function to determine the HSV (Hue, Saturation, Value) color limits, creates a mask to highlight the detected color, and then draws a bounding box around the object.


## Features

- **Real-time video processing**: Captures and processes each frame from the webcam in real-time.
- **Color detection**: Detects objects of a specified color using a custom color detection function.
- **Bounding box**: Draws a green bounding box around the detected object.
- **Flexible color detection**: Can easily be adapted to detect other colors by modifying the color input.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Pillow (PIL)

You can install the required packages by running:
```bash
pip install opencv-python-headless numpy pillow
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/color-detection-opencv.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd color-detection-opencv
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main Python script**:
   ```bash
   python main.py
   ```
   
2. The webcam feed will open in a new window. The script will detect objects of the specified color (blue by default) and display a bounding box around them.

3. **Press `q`** to close the webcam feed and exit the application.

## Code Explanation

### `main.py`
- Captures video from the default webcam (`cv2.VideoCapture(0)`).
- Converts each frame from BGR to HSV color space for easier color detection.
- Uses the `get_limits()` function from `Color_Detection.py` to get the HSV limits for the specified color (blue).
- Creates a binary mask where the detected color is highlighted.
- Finds the bounding box around the detected object and draws a green rectangle over it.
- Displays the processed video in a window.
- Exits when the 'q' key is pressed.

### `Color_Detection.py`
- Contains the `get_limits()` function that takes a BGR color as input and returns the HSV lower and upper limits for color detection.
- The HSV limits are used to create a mask for detecting the color in each frame.

## Future Improvements

- **Multi-color detection**: Add the ability to detect and track multiple colors simultaneously.
- **Object tracking**: Implement advanced tracking algorithms for smoother detection.
- **Improved UI**: Create a graphical user interface to select colors dynamically.