from ultralytics import YOLO
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp|timeout;5000"
# Load a pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Single stream with batch-size 1 inference
source = "rtsp://192.168.3.25:9554"  # RTSP, RTMP, TCP, or IP streaming address

# Run inference on the source
results = model(source, stream=True)  # generator of Results objects


for result in results:
    print(result)

