import os
from flask import Blueprint, request, jsonify, send_from_directory
from dotenv import load_dotenv
from utils.HttpStatus import HttpStatus
from utils.ImageManipulator import ImageManipulator
from utils.YoloModel import YoloModel
from utils.DataAnalisys import DataAnalisys

load_dotenv()

api = Blueprint('main', __name__)

image_manipulator = ImageManipulator()
model = YoloModel()

@api.route('/predict', methods=['POST'])
def predict():
    images = request.files.getlist('images')
    analized_images_count = len(images)
    bee_count_estimate = request.form.get('bee_count_estimate')

    try:
        image_manipulator.validate(images)
        image_manipulator.save_temporarily(images)
        image_paths = image_manipulator.get_paths()

        predicted_info = []

        for image_path in image_paths:
            model.load_best_weights()
            model.predict(image_path)
            model.filter_by_confidence(0.2)
            predict_info = model.get_predict_info()

            if predict_info:
                predicted_info.append(predict_info)

        if len(predicted_info) == 0:
            return jsonify({
                "message": "Imagens processadas com sucesso.",
                "results": {
                    "varroa_detected_count": 0,
                    "infestation_level": None,
                    "infestation_percent": 0,
                    "analized_images": analized_images_count,
                },
                "labeled_images": [],
            }), HttpStatus.HTTP_OK

        labeled_images = [f"{os.getenv('API_URL')}/images/predict/{predict_info['filename']}" for predict_info in predicted_info]

        analisys_results = DataAnalisys.calculate_infestation(
            predicted_info,
            int(bee_count_estimate),
            analized_images_count
        )

        image_manipulator.delete_temporary_images()

        return jsonify({
            "message": "Imagens processadas com sucesso.",
            "results": analisys_results,
            "labeled_images": labeled_images,
        }), HttpStatus.HTTP_OK
    except Exception as e:
         return jsonify({ "message": str(e) }), HttpStatus.BAD_REQUEST       


@api.route('/images/predict/<filename>', methods=['GET'])
def get_image(filename):
    return send_from_directory(os.path.abspath("../api/images/predict"), filename)
  
