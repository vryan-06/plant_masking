import cv2
import numpy as np

img1 = cv2.imread("./masked_collected_data/p2._mask.jpg")
img2 = cv2.imread("./masked_collected_data/p2(2).._mask.jpg")
img2 = cv2.resize(img2,(img1.shape[1], img1.shape[0]))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

def mse(img1, img2):
   h, w = img1.shape
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse_val = err/(float(h*w))
   print(mse_val)
   return mse_val, diff

mse_val, diff = mse(img1, img2)

if(mse_val>0.5):
   print("There has been significant growth detected in the plant")
else:
   print("There is no significant growth in the plant")
# cv2.imshow("difference", diff)
resized_image = cv2.resize(diff, (300, 500))
cv2.imshow("Difference", resized_image)
cv2.imshow("1",cv2.resize(img1,(300,500)))
cv2.imshow("2",cv2.resize(img2,(300,500)))
cv2.waitKey(0)
cv2.destroyAllWindows()