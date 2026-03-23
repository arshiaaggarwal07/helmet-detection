# AI Helmet Detection System

## Overview:
This project is a real-time helmet detection system built using **YOLOv8** and **OpenCV**. It detects whether 2-wheeler riders are wearing helmets from video input and flags violations.

## Features:
* Real-time object detection using YOLOv8
* Helmet / No Helmet classification
* Video processing and output generation
* Violation detection alerts

## Tech Stack:
* Python
* YOLOv8
* OpenCV
* NumPy

## How to Run:
* Clone the repository:  
git clone https://github.com/arshiaaggarwal07/helmet-detection.git
* Install dependencies:  
pip install -r requirements.txt
* Run detection:  
python detect_video.py

## Project Structure:
```text
helmet-detection/  
├── train.py                # Model training  
├── detect_video.py         # Video detection pipeline  
├── test.py                 # Model testing  
├── requirements.txt        # Dependencies  
└── README.md               # Documentation
```
## Results
<img width="793" height="635" alt="result" src="https://github.com/user-attachments/assets/11a08cf8-b4d0-4adf-bb3d-69c493e94507" />  
<img width="796" height="632" alt="result2" src="https://github.com/user-attachments/assets/529e39f4-8e97-4d20-ab40-74b945b7228f" />

## Future Improvements:
* Number plate detection
* Traffic violation tracking
* Web-based interface

## Author:
**Arshia Aggarwal**
