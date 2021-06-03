from typing import Counter
import cv2

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
first_frame = None

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #by adding GuassianBlur it reduces noise in the image and improves accurracy when compairing delta frame to current frame
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    # the delta frame is made with .absdiff, this shows the intentisy differance between the two images passed
    delta_frame = cv2.absdiff(first_frame,gray)

    # the .threshold frame lets up set a limit for detecting the difference between the 2 images and reassign them a new colour
    # so here we are setting anything that has a intensity difference of >30 to black 
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=4)

    #setting a new param as (cnts,_) - how this is written is important later, and we pass a copy of the threshold frame(As we dont want to modify it directly) 
    # and then use the built in methods of cv2.retrieve external and cv2. chain approx simple to the .findContours method to mark out an area where these are
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # to 'draw' the contour we are looping through every contour found in the .findCountours method and checking if they are larger then an expected size 
    # and if so, set these values to new params - x, y, width, height
    # then drawing this rectangle on the current frame 
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 3)

    cv2.imshow("feed",frame)
    cv2.imshow("Video",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("threshold",thresh_frame)
    key = cv2.waitKey(100)

    if key==ord('q'):
        break



video.release()
cv2.destroyAllWindows()