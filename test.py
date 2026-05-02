from ultralytics import YOLO
import easyocr
import cv2

# Load model
model = YOLO("runs/detect/train-8/weights/best.pt")

# Initialize OCR
reader = easyocr.Reader(['en'])

# Run detection
results = model.predict(source="test", save=True, imgsz=320)

# Process each image
for r in results:
    img = r.orig_img

    for box in r.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box)

        # Crop number plate
        plate = img[y1:y2, x1:x2]

        # OCR
        text = reader.readtext(plate)

        print("Detected Text:", text)