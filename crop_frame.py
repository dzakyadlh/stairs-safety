import numpy as np
import cv2
import matplotlib.pyplot as plt

def crop(frame, pts1):
    frame = cv2.resize(frame,(416, 416))
    # Create a mask of the same size as the image, initialized with zeros (black)
    mask = np.zeros(frame.shape[:2], dtype=np.uint8)

   # Fill the two polygons on the mask with white (255)
    cv2.fillPoly(mask, [pts1], 255)
    # cv2.fillPoly(mask, [pts2], 255)

    # Apply the mask to the image
    masked_image = cv2.bitwise_and(frame, frame, mask=mask)

    return masked_image

def calculate_pixel(frame):
    return np.std(frame)

image = cv2.imread('tangga_lsb.jpg')
image = cv2.resize(image,(416, 416))
# sample_img = cv2.imread('clean_handrail.png')
# pts1 = np.array([[256, 234], [258, 234], [305, 132], [303, 132]])
# pts2 = np.array([[312, 113], [404, 92], [404, 94], [312, 115]])
pts1 = np.array([[88, 68], [88, 74], [202, 275], [286, 298], [286, 292], [203, 270]])

crop_image = crop(image, pts1)
# px1 = calculate_pixel(image)
# px2 = calculate_pixel(sample_img)
# print(px1)
# print(px2)
# cv2.imwrite('clean_handrail.png', crop_image)
cv2.imshow('image', crop_image)
cv2.waitKey(0)
# plt.imshow(image)
# plt.show()