import cv2
import os
import numpy as np
width = 300
height = 300
save_path = "data/cropped_images"
input_path = "data/images"
if not os.path.exists(save_path):
    os.makedirs(save_path)
for filename in os.listdir(input_path):
    if not filename.endswith(".jpg"):
        continue
    image = cv2.imread(os.path.join(input_path, filename))
    resized_image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
    h, w = resized_image.shape[:2]
    if h > w:
        cropped_image = resized_image[(h-w)//2:(h-w)//2+w, :, :]
    else:
        cropped_image = resized_image[:, (w-h)//2:(w-h)//2+h, :]
    if cropped_image.shape[2] not in [1, 3, 4]:
        cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(os.path.join(save_path, filename), cropped_image)
