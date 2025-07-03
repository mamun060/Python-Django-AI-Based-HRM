from ultralytics import YOLO
from huggingface_hub import hf_hub_download
from facenet_pytorch import InceptionResnetV1

def load_yolo_model():
    model_path = hf_hub_download(repo_id="arnabdhar/YOLOv8-Face-Detection", filename="model.pt")
    return YOLO(model_path)

def load_facenet_model():
    return InceptionResnetV1(pretrained='vggface2').eval()
