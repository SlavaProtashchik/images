import cv2
import numpy as np

from helper import file_output_path


def circles_detect(path: str):
    image = cv2.imread(path)

    # Преобразование в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем размытие, чтобы уменьшить шум
    gray = cv2.medianBlur(gray, 5)

    # Применяем преобразование Хафа для окружностей
    circles = cv2.HoughCircles(
        image=gray,
        method=cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=120,
        param1=50,
        param2=30,
        minRadius=0,
        maxRadius=0
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

    output_path = file_output_path(path, "hough")
    cv2.imwrite(output_path, image)
