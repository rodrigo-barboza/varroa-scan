import os

class ImageManipulator:
    def __init__(self):
        self.image_paths = []

    def validate(self, images):
        if not images:
            raise Exception("Nenhuma imagem foi enviada.")
        if len(images) > 5:
            raise Exception("No máximo 5 imagens podem ser enviadas por requisição.")

        return self

    def save_temporarily(self, images):
        for image in images:
            image.save(f"../api/images/received/{image.filename}")
            self.image_paths.append(f"{os.path.abspath('../api/images/received/')}/{image.filename}")

        return self

    def get_paths(self):
        return self.image_paths

    def delete_temporary_images(self):
        for image_path in self.image_paths:
            os.remove(image_path)

        self.image_paths = []