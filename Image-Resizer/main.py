# in this project we will create an image resizer

import cv2

#configuration
source_image='bunny.webp'
destination_image='honey-bunny.png'
scale_percentage = 50

image = cv2.imread(source_image,cv2.IMREAD_UNCHANGED)
# cv2.imshow('bunny',image)  # to show image

# calculate the dimensions
new_width = int(image.shape[1] * scale_percentage / 100)   #shape[0] means width
new_height = int(image.shape[0] * scale_percentage / 100)  #shape[0] means height

#dsize
dsize = (new_width,new_height)

# resizing image
final_image = cv2.resize(image, dsize)

cv2.imwrite(destination_image, final_image)
cv2.waitKey(0)