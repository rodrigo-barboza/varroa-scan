import os
from ultralytics import YOLO

# Treinamento do modelo
model = YOLO('yolov8m.pt')

model.train(
    data="/content/drive/MyDrive/Dataset/data-v2.yml",
    epochs=100,
    freeze=10,
    batch=32,
    imgsz=640,
    mosaic=0.8
)

# Carrega o modelo treinado
model = YOLO("/content/runs/detect/train/weights/best.pt")  # Caminho para os pesos treinados

# Testar com imagens da internet

image_paths = [
    "/content/drive/MyDrive/Dataset/lg-b-foto varroa para portada de blog mundo abejas.jpg",
    "/content/drive/MyDrive/Dataset/bee-with-mite.jpg",
    "/content/drive/MyDrive/Dataset/2017-08-28_09-30-00-1_500_dirty_glass.mp4-bee_id_6843-15735-1.png",
    "/content/drive/MyDrive/Dataset/varroa-colonia.jpg",
    "/content/drive/MyDrive/Dataset/sensors-21.png",
    "/content/drive/MyDrive/Dataset/varroainfestation.webp",
    "/content/drive/MyDrive/Dataset/resistance-bioassay-varroa_main.jpeg",
    "/content/drive/MyDrive/Dataset/varroamite.jpg",
    "/content/drive/MyDrive/Dataset/190849.png",
    "/content/drive/MyDrive/Dataset/shutterstock_417000916.webp",
    "/content/drive/MyDrive/Dataset/how-to-monitor-and-control-varroa-mites.jpg",
]

for image_path in image_paths:
    # as imagens serão salvas já rotuladas em /content/runs/detect/predict
    model(image_path, save=True)
