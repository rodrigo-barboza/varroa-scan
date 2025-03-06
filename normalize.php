<?php

function convertToYoloFormat($labelFile, $imageWidth, $imageHeight, $saveToFile) {
    if (!file_exists($labelFile)) {
        echo "Arquivo de rótulo não encontrado!\n";
        return;
    }

    $lines = file($labelFile);

    if (!$lines) {
        echo "Arquivo de rótulos vazio!\n";
        return;
    }

    $classId = trim($lines[0]);
    $yoloLabels = [];

    foreach (array_slice($lines, 1) as $line) {
        $values = array_map('floatval', explode(" ", $line));

        if (count($values) !== 4) {
            echo "Rótulo inválido encontrado e ignorado: $line\n";
            continue;
        }

        [$xMin, $yMin, $xMax, $yMax] = $values;

        // Conversão para formato YOLO
        $xCenter = (($xMin + $xMax) / 2) / $imageWidth;
        $yCenter = (($yMin + $yMax) / 2) / $imageHeight;
        $width = ($xMax - $xMin) / $imageWidth;
        $height = ($yMax - $yMin) / $imageHeight;

        $yoloLabels[] = sprintf("%s %.6f %.6f %.6f %.6f", $classId, $xCenter, $yCenter, $width, $height);
    }

    if (empty($yoloLabels)) {
        echo "Nenhuma label válida foi encontrada!\n";
        return;
    }

    file_put_contents($saveToFile, implode("\n", $yoloLabels));

    echo "Convertido e salvo em: $saveToFile\n";
}

foreach(['train', 'test', 'val'] as $set) {
    $labels_set_path = "./dataset-sm/original/{$set}/labels";

    $files = array_diff(scandir($labels_set_path), ['..', '.']);

    foreach($files as $file_name) {
        if (!is_dir("./dataset-sm/yolo/$set/labels")) {
            mkdir("./dataset-sm/yolo/$set/labels", 0777, true);
        }

        convertToYoloFormat("$labels_set_path/$file_name", 160, 280, "./dataset-sm/yolo/$set/labels/$file_name");

        $file_name = str_replace('.txt', '.png', $file_name);

        if (!is_dir("./dataset-sm/yolo/$set/images")) {
            mkdir("./dataset-sm/yolo/$set/images", 0777, true);
        }

        copy(
            str_replace('labels', 'videos', $labels_set_path) . '/' . $file_name,
            "./dataset-sm/yolo/$set/images/$file_name"
        );
    }
}
