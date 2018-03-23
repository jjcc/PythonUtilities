import numpy as np
import cv2

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('.\data\PEGLIST1to100.avi')
#cap = cv2.VideoCapture('data.avi')
cap = cv2.VideoCapture('video.mp4')

fcount  = 0
icount  = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        fcount += 1
        # write the flipped frame
        #out.write(frame)
        if (fcount%150):
            continue
        icount += 1
        cv2.imwrite("data/frame%d.jpg" % icount, frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
#out.release()
cv2.destroyAllWindows()