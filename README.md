Vehicle Detection for Traffic Management

Overview

This project implements a real-time vehicle detection system using OpenCV to monitor traffic and reduce accidents. The system processes video input, detects vehicles using a pre-trained Haar cascade classifier (cars.xml), and highlights detected vehicles in the video stream.

Features

Detects vehicles in real-time from video input.

Uses OpenCV and Haar cascade classification for vehicle recognition.

Enhances traffic monitoring and accident prevention.

Works with both video files and live webcam feed.

Requirements

Ensure you have the following installed:

Python 3.x

OpenCV (cv2)

Install dependencies using:

pip install opencv-python

Usage

Place the cars.xml file in the project directory.

Run the Python script:

python vehicle_detection.py

The script will process a video (traffic.mp4) or a webcam feed (uncomment cv2.VideoCapture(0)).

Press q to exit the detection window.

Code Explanation

Loads the Haar cascade classifier (cars.xml).

Converts each video frame to grayscale.

Detects vehicles and highlights them with rectangles.

Displays the processed frames in real-time.



License

This project is open-source and available under the MIT License.

Contact

For any inquiries, reach out via email: madesh61waran@gmail.com
