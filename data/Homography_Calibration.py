from pickle import TRUE
import cv2
import numpy as np

path= r'C:\Users\shama\Desktop\Iaac\Term 02\Hardware\Py Code\Line Tracking\Warp_01.JPG'  #Replace with path to calibration img
img = cv2.imread (path,cv2.IMREAD_COLOR)

#Image is flipped to correct the camera view
img = cv2.flip(img,0)
img = cv2.resize(img, (860, 460))

# Create 2 sets of points. One set on the Flat image and the other set on the perspective image

#Pts1 points below

# cv2.circle(img,(330,250),5,(0,255,0),5)
# cv2.circle(img,(523,260),5,(0,255,0),5)
# cv2.circle(img,(530,380),5,(0,255,0),5)
# cv2.circle(img,(300,370),5,(0,255,0),5)

#pts2 points below

# path= r'C:\Users\shama\Desktop\Iaac\Term 02\Hradware\Py Code\Line Tracking\Warpcrt_01.png'
# img = cv2.imread (path,cv2.IMREAD_COLOR)
# # img = cv2.flip(img,0)
# img = cv2.resize(img, (860, 460))
# cv2.circle(img,(357,250),5,(0,0,255),5)
# cv2.circle(img,(490,253),5,(0,0,255),5)
# cv2.circle(img,(490,378),5,(0,0,255),5)
# cv2.circle(img,(358,378),5,(0,0,255),5)

pts1=np.float32([[330,250],[523,260],[530,380],[300,370]])
pts2=np.float32([[357,250],[490,253],[490,378],[358,378]])

#Find Homography
matrix01=cv2.findHomography(pts1,pts2)
matrix=cv2.getPerspectiveTransform(pts1,pts2)

#correct the perspective
result=cv2.warpPerspective(img,matrix,(860, 460))

#cv2.imshow('Frame',img)
print(result)
cv2.imshow('Image',result)
cv2.waitKey()
cv2.destroyAllWindows()
