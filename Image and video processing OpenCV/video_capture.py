import cv2

# there is a built in method for cv2 called .VideoCapture, this will take an index for your camera as an argument
#  or for a video file, the filepath of the video
# laptop intergrated camera will have an index of 0, second camera, index of 1 etc
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# setting the video to a new vari and the check is a boolian value 
# using a while loop to keep it all going, this wil refresh the value to show a moving video instead of a static image
while True:
    check, frame = video.read()

    grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # using the image show method to show the video frames
    cv2.imshow("Video",grey)
    key = cv2.waitKey(100)

    if key==ord('q'):              # to add a break to to while loop we specify a specific key to end the video - q for quit
        break

video.release()    # the .release() MUST be after the waitkey or the video will stop before the frame is rendered
cv2.destroyAllWindows()
