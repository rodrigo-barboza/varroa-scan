import os
from ultralytics import YOLO

# Treinamento do modelo
model = YOLO("yolov8n.yaml")  # Arquitetura base (pode ser 'yolov8m.yaml' ou 'yolov8l.yaml' para modelos maiores)

model.train(
    data=os.path.abspath("yolo-model/data.yml"),
    epochs=50,  # Ajuste conforme necessário
    batch=16,
    imgsz=640,  # Ajuste conforme o tamanho das imagens do dataset
)

# Carrega o modelo treinado
model = YOLO("runs/detect/train/weights/best.pt")  # Caminho para os pesos treinados

print(model)
# # Faz a inferência em uma imagem
results = model(os.path.abspath("yolo-model/bee-with-mite.jpg"), save=True)

# Conta a ocorrência do ácaro Varroa (assumindo que ele tem ID 1)
contagem_varroa = sum(1 for r in results[0].boxes.cls if r == 1)

print(f"Total de Varroa detectados: {contagem_varroa}")

