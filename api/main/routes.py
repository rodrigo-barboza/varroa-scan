import os
import threading
from flask import Blueprint, request, jsonify, send_from_directory
from dotenv import load_dotenv
from datetime import datetime
from utils.HttpStatus import HttpStatus
from utils.ImageManipulator import ImageManipulator
from utils.YoloModel import YoloModel
from utils.DataAnalisys import DataAnalisys

load_dotenv()

api = Blueprint('main', __name__)

model = YoloModel()
model_lock = threading.Lock()

@api.route('/predict', methods=['POST'])
def predict():
    images = request.files.getlist('images')
    analized_images_count = len(images)
    bee_count_estimate = request.form.get('bee_count_estimate')
    treshold = request.form.get('threshold', 0.55)

    image_manipulator = ImageManipulator()

    try:
        image_manipulator.validate(images)
        image_manipulator.save_temporarily(images)
        image_paths = image_manipulator.get_paths()

        predicted_info = []

        with model_lock:
            model.load_best_weights()

            for image_path in image_paths:
                model.predict(image_path)
                model.filter_by_confidence(float(treshold))
                predict_info = model.get_predict_info()

                if predict_info:
                    predicted_info.append(predict_info)

        if len(predicted_info) == 0:
            return jsonify({
                "message": "Imagens processadas com sucesso.",
                "results": {
                    "varroa_detected_count": 0,
                    "infestation_level": 'healthy',
                    "infestation_percent": 0,
                    "analized_images": analized_images_count,
                },
                "labeled_images": [],
                "analized_at": datetime.now().timestamp(),
            }), HttpStatus.HTTP_OK

        labeled_images = [f"{os.getenv('API_URL')}/images/predict/{predict_info['filename']}" for predict_info in predicted_info]

        analisys_results = DataAnalisys.calculate_infestation(
            predicted_info,
            int(bee_count_estimate),
            analized_images_count
        )

        return jsonify({
            "message": "Imagens processadas com sucesso.",
            "results": analisys_results,
            "labeled_images": labeled_images,
            "analized_at": datetime.now().timestamp(),
        }), HttpStatus.HTTP_OK
    except Exception as e:
         return jsonify({ "message": str(e) }), HttpStatus.BAD_REQUEST
    finally:
        image_manipulator.delete_temporary_images()


@api.route('/images/predict/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(os.path.abspath("../api/images/predict"), filename)
