import os
from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  # Arquitetura base (pode ser 'yolov8m.yaml' ou 'yolov8l.yaml' para modelos maiores)

model.train(
    data=os.path.abspath("yolo-model/data.yml"),
    epochs=50,
    batch=16,
    imgsz=320,
)

model = YOLO("runs/detect/train/weights/best.pt")  # Caminho para os pesos treinados

print(model)

results = model(os.path.abspath("yolo-model/bee-with-mite.jpg"), save=True)

contagem_varroa = sum(1 for r in results[0].boxes.cls if r == 1)

print(f"Total de Varroa detectados: {contagem_varroa}")

