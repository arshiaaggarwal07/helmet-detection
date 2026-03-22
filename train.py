from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/last.pt")  # resume from last

model.train(
    data="dataset/data.yaml",
    epochs=8,      # total epochs (not additional!)
    imgsz=416,
    batch=8,
    resume=True
)