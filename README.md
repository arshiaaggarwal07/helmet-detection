AI Helmet Detection System

Overview:
This project is a real-time helmet detection system built using YOLOv8 and OpenCV. It detects whether 2-wheeler riders are wearing helmets from video input and flags violations.

Features:
-Real-time object detection using YOLOv8
-Helmet / No Helmet classification
-Video processing and output generation
-Violation detection alerts

Tech Stack:
-Python
-YOLOv8
-OpenCV
-NumPy

How to Run:
1. Clone the repository:
git clone https://github.com/arshiaaggarwal07/helmet-detection.git
2. Install dependencies:
pip install -r requirements.txt
3. Run detection:
python detect_video.py

Project Structure:
-train.py → model training
-detect_video.py → video detection
-dataset → training data

Future Improvements:
-Number plate detection
-Traffic violation tracking
-Web-based interface

Author:
Arshia Aggarwal
