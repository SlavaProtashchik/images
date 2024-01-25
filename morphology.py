import cv2 as cv
import numpy as np

from helper import file_output_path


def morphology(path: str):
    # Читаем изображение
    image = cv.imread(path)

    size = 7
    kernal = {
        'rect': cv.getStructuringElement(cv.MORPH_RECT, (size, size)),
        'cross': cv.getStructuringElement(cv.MORPH_CROSS, (size, size)),
        'ell': cv.getStructuringElement(cv.MORPH_ELLIPSE, (size, size)),
        'diamond': np.array([
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ], dtype=np.uint8)
    }

    for ker in kernal:
        erosian = cv.erode(image, kernal[ker])
        file_path = file_output_path(path, f'morphology/erosian/{ker}')
        cv.imwrite(file_path, erosian)

        dilate = cv.dilate(image, kernal[ker])
        file_path = file_output_path(path, f'morphology/dilate/{ker}')
        cv.imwrite(file_path, dilate)

        morph_open = cv.morphologyEx(image, cv.MORPH_OPEN, kernal[ker])
        file_path = file_output_path(path, f'morphology/open/{ker}')
        cv.imwrite(file_path, morph_open)

        morph_close = cv.morphologyEx(image, cv.MORPH_CLOSE, kernal[ker])
        file_path = file_output_path(path, f'morphology/close/{ker}')
        cv.imwrite(file_path, morph_close)

        morph_blackhat = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernal[ker])
        file_path = file_output_path(path, f'morphology/blackhat/{ker}')
        cv.imwrite(file_path, morph_blackhat)

        morph_gradient = cv.morphologyEx(image, cv.MORPH_GRADIENT, kernal[ker])
        file_path = file_output_path(path, f'morphology/gradient/{ker}')
        cv.imwrite(file_path, morph_gradient)




