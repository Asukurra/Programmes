import cv2

#               opening the image and set colour and transparancy if needed
#               in imread(<filepath>,<colour settings>)  -1 for RGBA or 0 for black and white or 1 for RGB
#               the images are a numpy array
img=cv2.imread("Image and video processing OpenCV\galaxy.jpg",0)

#               returning the 2D array - to get the pixel size you can add .shape on the the end (2d as its current in black and white, -1 or 1 would be a 3d array)
# print(img)
# print(img.shape)

#               you can resize the images by using the .resize(<img>,(<tuple for newsize>) - width,height
# resized_image = cv2.resize(img,(1000,500))
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#               cv2.imshow is image show (<title you want to call it>, <img>) this can be a path or a vari
# cv2.imshow("Night Sky",img)
cv2.imshow("Night Sky",resized_image)
#               saving the new resized image - use imwrite(<newfilenameand path>,<img>)
cv2.imwrite("Image and video processing OpenCV/Nightsky_resize.jpg", resized_image)
#               the waitKey is how long to have this image opem - 0 is when any key is clicked or you can set in ms how to long to keep open - example is waitKey(2000) is 2 seconds
cv2.waitKey(0)
#               the destroy all windows closes all the windows after the set time in waitKey
cv2.destroyAllWindows()

