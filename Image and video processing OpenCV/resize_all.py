#               Create a script that resizes all imgs in a directory to 100px x 100px

import cv2
import os

dir = "Image and video processing OpenCV\sample_images"

for filename in os.listdir(dir):
    if 'resized_' not in filename:
        try:
            path = dir + '/' + filename
            img=cv2.imread(path,1)
            resized_img = cv2.resize(img,(100,100))
            cv2.imwrite(dir + '/' + 'resized_' + filename,resized_img)
        except:
            continue
#               notes for improvement - speciy the except for files that are not img types 


#               below is the given solution for the course 
# import cv2
# import glob

# images=glob.glob("*.jpg")

# for image in images:
#     img=cv2.imread(image,0)
#     re=cv2.resize(img,(100,100))
#     cv2.imshow("Hey",re)
#     cv2.waitKey(500)
#     cv2.destroyAllWindows()
#     cv2.imwrite("resized_"+image,re)