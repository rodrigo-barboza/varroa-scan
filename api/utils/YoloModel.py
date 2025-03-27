import os
import torch
import torchvision.ops as ops  # Para aplicar NMS
from ultralytics import YOLO
from ultralytics.engine.results import Boxes

class YoloModel:
    def __init__(self):
        self.model = None
        self.results = None
        self.current_image_path = None
        self.IOU_THRESHOLD = 0.5
        self.predict_info = None

    def set_iou_threshold(self, threshold):
        self.IOU_THRESHOLD = threshold

        return self
    
    def best_weights_path(self):
        return os.path.abspath("../api/weights/best.pt")
    
    def predict_images_directory(self):
        return os.path.abspath("../api/images/predict")

    def load_best_weights(self):
        self.model = YOLO(self.best_weights_path())

        return self

    def predict(self, image_path):
        self.current_image_path = image_path
        self.results = self.model(image_path)

        return self

    def filter_by_confidence(self, confidence_threshold=0.5):
        if not self.results:
            return self

        boxes = self.results[0].boxes

        if boxes and len(boxes) > 0:
            confs = boxes.conf  # Confianças das detecções
            xyxy = boxes.xyxy  # Coordenadas das bounding boxes
            labels = boxes.cls  # Classes detectadas

            # Filtra caixas com confiança maior que CONFIDENCE_THRESHOLD
            high_conf_idx = confs > confidence_threshold
            confs = confs[high_conf_idx]
            xyxy = xyxy[high_conf_idx]
            labels = labels[high_conf_idx]

            if len(confs) > 0:
                # Aplica Non-Maximum Suppression (NMS) para remover caixas redundantes
                keep_indices = ops.nms(xyxy, confs, self.IOU_THRESHOLD)

                # Mantém apenas as caixas filtradas
                best_boxes_data = torch.cat((xyxy[keep_indices], confs[keep_indices].unsqueeze(1), labels[keep_indices].unsqueeze(1)), dim=1)

                # Atualiza os resultados com apenas as melhores bounding boxes
                self.results[0].boxes = Boxes(best_boxes_data, boxes.orig_shape)

                # Salva a imagem com as melhores detecções filtradas
                image_path = f"{self.predict_images_directory()}/{self.current_image_path.split('/')[-1]}"
                self.results[0].save(filename=image_path)

                self.predict_info = {
                    "image_path": image_path,
                    "filename": self.current_image_path.split('/')[-1],
                    "varroa_detected_count": len(keep_indices),
                    "total_boxes": len(boxes),
                    "high_conf_boxes": len(high_conf_idx.nonzero()),
                }

                return self

        return self
    
    def resetState(self):
        self.model = None
        self.results = None
        self.current_image_path = None
        self.IOU_THRESHOLD = 0.5
        self.predict_info = None

    def get_predict_info(self):
        info = self.predict_info
        self.resetState()

        return info

