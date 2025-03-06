import os
import shutil

def convert_to_yolo_format(label_file, image_width, image_height, save_to_file):
    if not os.path.exists(label_file):
        print(f"Arquivo de rótulo não encontrado: {label_file}")
        return

    with open(label_file, "r") as file:
        lines = file.readlines()

    if not lines:
        print(f"Arquivo de rótulos vazio: {label_file}")
        return

    class_id = lines[0].strip()
    yolo_labels = []

    for line in lines[1:]:
        values = list(map(float, line.split()))

        if len(values) != 4:
            print(f"Rótulo inválido encontrado e ignorado: {line.strip()}")
            continue

        x_min, y_min, x_max, y_max = values

        # Conversão para formato YOLO
        x_center = ((x_min + x_max) / 2) / image_width
        y_center = ((y_min + y_max) / 2) / image_height
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        yolo_labels.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    if not yolo_labels:
        print(f"Nenhuma label válida foi encontrada em: {label_file}")
        return

    os.makedirs(os.path.dirname(save_to_file), exist_ok=True)
    with open(save_to_file, "w") as file:
        file.write("\n".join(yolo_labels))

    print(f"Convertido e salvo em: {save_to_file}")


datasets = ['train', 'test', 'val']

for dataset in datasets:
    labels_set_path = f"./dataset-sm/original/{dataset}/labels"
    
    if not os.path.exists(labels_set_path):
        print(f"Diretório não encontrado: {labels_set_path}")
        continue

    files = [f for f in os.listdir(labels_set_path) if f.endswith('.txt')]

    for file_name in files:
        yolo_labels_dir = f"./dataset-sm/yolo/{dataset}/labels"
        os.makedirs(yolo_labels_dir, exist_ok=True)

        convert_to_yolo_format(
            os.path.join(labels_set_path, file_name),
            160, 280,
            os.path.join(yolo_labels_dir, file_name)
        )

        image_name = file_name.replace('.txt', '.png')
        image_source_path = os.path.join(labels_set_path.replace('labels', 'videos'), image_name)
        image_dest_dir = f"./dataset-sm/yolo/{dataset}/images"
        os.makedirs(image_dest_dir, exist_ok=True)

        if os.path.exists(image_source_path):
            shutil.copy(image_source_path, os.path.join(image_dest_dir, image_name))
        else:
            print(f"Imagem não encontrada: {image_source_path}")
