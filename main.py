import os

from hough_transform import circles_detect
from morphology import morphology
from segment import segment

origin_images = os.path.abspath('./images')

for file in os.listdir(origin_images):
    file_path = os.path.join(origin_images, file)
    if os.path.isfile(file_path):
        circles_detect(file_path)
        morphology(file_path)
        segment(file_path)
