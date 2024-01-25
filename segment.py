import cv2

from helper import file_output_path


def segment(path):
    # Загружаем изображение в оттенках серого
    image = cv2.imread(path, 0)

    # Применяем пороговую сегментацию
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # Сохраняем обработанное изображение
    output_path = file_output_path(path, "segment")
    cv2.imwrite(output_path, thresh1)
