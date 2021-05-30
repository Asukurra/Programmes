import cv2

# using haarcascade model for reconition

face_cascade = cv2.CascadeClassifier("Image and video processing OpenCV\Files\haarcascade_frontalface_default.xml")

# using greyscale images are better for accurracy
img = cv2.imread("Image and video processing OpenCV/Files/news.jpg")
# because we want to keep the colour as the output, we load the image then use a built in method to covert to greyscale before outputting back in colour
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.15,
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0), 3)


cv2.imshow("image",gray_img)
cv2.imshow("box_image", img)
cv2.waitKey(0)
cv2.destroyAllWindows


#this will highlight the ladys face but the mans face is too off to be detected with this model haarcascade being used,
#  with scale of 1.05 and minN of 5 will detect his hand as a face,
# moving the scale up to 1.1 will remove the hand detection but will not detect his face