import cv2

# using haarcascade model for reconition

face_cascade = cv2.CascadeClassifier("Image and video processing OpenCV\Files\haarcascade_frontalface_default.xml")

# using greyscale images are better for accurracy
img = cv2.imread("Image and video processing OpenCV\Files\photo.jpg")
# because we want to keep the colour as the output, we load the image then use a built in method to covert to greyscale before outputting back in colour
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# setting a new vari for the detection and using the built in .detectmultiscale method and passing the needed params
# grey img is the image we converted from the input image
# scaleFactor is how much the image scales every pass, the lower the number the more accurate but longer it takes
# numNeighbors is how many pixels around the current scan is being looked at to help determine if face
faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=5)

# print(faces)
# printing this out gives a numpy array with an x,y data and width and height in pixels
# the above img being used gives [[157  84 379 379]] - this is 157th row and 84th column is the top left of the detected face and a with/height of 379 

# to draw this rectangle over the image to check where the face is found we can use a for loop and built in .rectangle method 
# we need to pass in at least 5 params - (img,(topleft x and y),(bottom right x and y), (BGR colour range for the box), (box thickness in px))
# the x and y are from the numpy array provided from the .detectMultiScale used above
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0), 3)

# could add a resize element here or put all this into a method to do with the .shape element etc

cv2.imshow("image",gray_img)
cv2.imshow("box_image", img)
cv2.waitKey(0)
cv2.destroyAllWindows


