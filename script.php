<?php

const IMG_WIDTH = 280;
const IMG_HEIGHT = 160;

foreach (['test', 'train', 'val'] as $set) {
    $csv_path = "./varroa_dataset_sm/$set/gt_one.csv";
    $csv_content = file_get_contents($csv_path);

    mkdir("./varroa_dataset_sm/$set/labels/", 0777, true);

    foreach (explode("\n", $csv_content) as $line) {
        $line_items = explode(' ', $line);

        $file_txt_name = "./varroa_dataset_sm/$set/labels/" . explode("/", $line_items[0])[2] . '.txt';
        unset($line_items[0]);

        foreach($line_items as $key => $item) {
            if ($key === 1) {
                continue;
            }

            if ($key % 2 == 1) {
                $line_items[$key] = (float) $item / IMG_WIDTH;
                continue;
            }

            $line_items[$key] = (float) $item / IMG_HEIGHT;
        }

        file_put_contents(
            str_replace('.png', '', $file_txt_name),
            implode(' ', $line_items),
        );
    }
}
