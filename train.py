from ultralytics import YOLO

print("STARTING TRAINING...")

model = YOLO("yolov8n.pt")

results = model.train(
    data="data.yaml",
    epochs=50,
    imgsz=320,      # 🔥 reduce image size
    batch=1,        # 🔥 lowest memory usage
    device="cpu",
    workers=0,      # important for low RAM
    cache=False
)

print("TRAINING COMPLETED")