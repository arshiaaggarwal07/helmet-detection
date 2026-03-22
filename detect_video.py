import cv2
from ultralytics import YOLO
import time

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Load video
cap = cv2.VideoCapture("input.mp4")

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resize for speed
    frame = cv2.resize(frame, (640, 480))

    # Run detection
    results = model(frame)

    annotated_frame = results[0].plot()

    # 🚨 Violation detection
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if cls == 1:  # no_helmet
                cv2.putText(annotated_frame, "NO HELMET!",
                            (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2)

                # Save violation image
                cv2.imwrite(f"violation_{time.time()}.jpg", frame)

    # Show video
    cv2.imshow("Helmet Detection", annotated_frame)

    # Save output
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()