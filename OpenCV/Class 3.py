# OpenCV Python Tutorial For Beginners 3 - How to Read, Write, Show Images in OpenCV

import cv2

img = cv2.imread('lena.jpg', 1) # flag 0, 1, -1
print(img) # if file name is wrong then it will print none
cv2.imshow('image', img) # (name of window, variable)
cv2.waitKey(0) #image will show only for 5 sec. otherwis it will show only milisecond; If we write 0 then it will stay infinity time.
cv2.destroyAllWindows() # for destroy all window

cv2.imwrite('lena_copy.png', img)