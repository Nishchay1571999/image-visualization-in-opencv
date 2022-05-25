from email.mime import image
import cv2
import glob

from cv2 import cvtColor


# detecting faces in image using opencv 

# The hardcascade_frontalcafe_default.xml has all the training data for the face training methoda in it 
# we will be using this xml file to train the module to detect face in the image 



face_cascade = cv2.CascadeClassifier('./assets/training/haarcascade_frontalface_default.xml')


img = cv2.imread("./assets/news.jpg")
# the better version is to use the grayscae image to search faces
# it will be better for accuracy


gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# This will convert a BGR image to a gray scale image 
# create aclassifier analyzer 

faces = face_cascade.detectMultiScale(gray_image,
                                      scaleFactor= 1.1,
                                      minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# print(type(faces))
# print(faces)

cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
















