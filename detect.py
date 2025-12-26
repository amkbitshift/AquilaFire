from ultralytics import YOLO
from smoke_filter import smoke_color_score
import cv2

model = YOLO("yolov8n.pt")

def detect_smoke(image_path):
    img = cv2.imread(image_path)
    results = model(img)

    yolo_conf = 0.0
    for r in results:
        for box in r.boxes:
            yolo_conf = max(yolo_conf, float(box.conf))

    color_score = smoke_color_score(image_path)

    # Hybrid confidence
    final_conf = (0.6 * yolo_conf) + (0.4 * color_score)
    return final_conf
