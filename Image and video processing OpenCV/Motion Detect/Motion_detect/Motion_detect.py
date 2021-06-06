import cv2, time, pandas
from datetime import datetime
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool, ColumnDataSource

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
first_frame = None
status_list = [None,None]  #this is set to None, None because it needs 2 valid entries for the if datetime block below
times = []
df = pandas.DataFrame(columns=["Start","End"])

# adding a status vari to monitor when there is something moveing in frame - 0 is nothing and 1 is movement
while True:
    check, frame = video.read()
    status = 0

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
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    #setting a new param as (cnts,_) - how this is written is important later, and we pass a copy of the threshold frame(As we dont want to modify it directly) 
    # and then use the built in methods of cv2.retrieve external and cv2. chain approx simple to the .findContours method to mark out an area where these are
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # to 'draw' the contour we are looping through every contour found in the .findCountours method and checking if they are larger then an expected size 
    # and if so, set these values to new params - x, y, width, height
    # then drawing this rectangle on the current frame 
    for contour in cnts:
        if cv2.contourArea(contour) < 20000:
            continue
        status = 1   # while the contor is over the value above it sets status to 1

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 3)

    #making a new array for when there is something in the shot and when there is not by appending each loop pass
    status_list.append(status)
    #memory issues when running for a long time = only keeping the last 2 elements in the array 
    status_list = status_list[-2:]

    #checking the last 2 elements of the list array to see if it has changed - this triggers a datestamp for it in a new array called times so we have access to when an object enters and leaves the frame
    if status_list[-1] ==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1] ==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("feed",frame)
    cv2.imshow("Video",gray)
    cv2.imshow("delta",delta_frame)
    cv2.imshow("threshold",thresh_frame)
    key = cv2.waitKey(100)

    #added a new if inside this, if the screen closes while something is in the screen is adds a new timestamp so there is not an an odd number in the array
    if key==ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)

# for loop with step of 2 to read all the start times from the array, adding into dictonary and usinf i+1 to access the end times (when item has left the frame)
for i in range(0,len(times),2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

# below is all the bokeh graph creation and modifying
df["Start_string"] = df["Start"].dt.strftime("%H:%M:%S: %d-%m-%Y")
df["End_string"] = df["End"].dt.strftime("%H:%M:%S: %d-%m-%Y")

cds = ColumnDataSource(df)

f = figure(x_axis_type='datetime',height=100, width=500,sizing_mode = "scale_width", title="Motion Graph")
f.yaxis.minor_tick_line_color=None
f.yaxis[0].ticker.desired_num_ticks=1
f.yaxis.visible = False

hover = HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
f.add_tools(hover)

q=f.quad("Start","End",bottom=0,top=1,color="green", source=cds)

output_file("motion graph.html")
show(f)

df.to_csv("Image and video processing OpenCV/Motion Detect/Motion_detect/Motion_Times.csv")    

video.release()
cv2.destroyAllWindows()