from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

print("Model loaded successfully!")