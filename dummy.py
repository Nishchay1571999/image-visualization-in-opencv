import cv2
import glob

images = glob.glob("./assets/*.jpg")
# This is a list of images in the assets folder 

# Batch image resizing 

# iterating through the lists using for loop

for image in images:
    # This loop contains each image 
    img = cv2.imread(image,0)
    # resizing the selected image 
    re = cv2.resize(img,(100,100))
    # Showing the resized image 
    cv2.imshow("Hey",re)
    # telles the window to wait for the nest 5 seconds 
    cv2.waitKey(5000)
    # after 5 second destroy the newly created window 
    cv2.destroyAllWindows()
    # This will create a new file nameed resized+ the name of the image for the re image 
    # which was created after resizing 
    cv2.imwrite("resized"+image,re)

img = cv2.imread('./assets/Lighthouse.jpg',1)
# read the image as it is pass 1 as second parameter 
# color image :-1
# black and white/gray scale image :0


print(type(img))
print(img.shape)

# python stores the image as a pixels of image 

resizedimage = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))


cv2.imshow("Avatar",resizedimage)
cv2.waitKey(20000)
cv2.destroyAllWindows()