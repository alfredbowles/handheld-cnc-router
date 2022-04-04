import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
# Set screen ratio
cap.set(3, 480)
cap.set(4, 2)

# Find Distance between object center and screen center
def distance(cx,cy,sx,sy):
    dist_x = abs(cx - sx)
    dist_y = abs(cy - sy)
    dist = math.sqrt(dist_x**2 + dist_y**2)
    return dist

#Read Frames
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    #detect colour change
    l = 70
    h = 0
    low_b = np.uint8([l,l,l])
    high_b = np.uint8([h,h,h])

    #mask Colour Range and find contours
    mask = cv2.inRange(frame, high_b, low_b)
    contours, hierarchy = cv2.findContours(mask, 1, cv2.CHAIN_APPROX_SIMPLE)

    # Showing the final image. 
    dc=cv2.drawContours(mask,contours,0,(0,255,0),5)
    #Image Center
    (h, w) = frame.shape[:2]
    (sx, sy) = (w//2, h//2)
    if len(contours) > 0 :
            c = max(contours, key=cv2.contourArea)
            midPoints = []
            threshold = 60
            step = 5
            # print(type(c[0]))
            for j in range(0,len(c),step):
                point = c[j]
                midPoint = [0, 0]
                counter = 0
                for j2 in range(0, len(c), step):
                    point2 = c[j2]
                    pointsDist = distance(point[0][0],point[0][1],point2[0][0],point2[0][1]) 
                    if pointsDist < threshold:
                        midPoint[0] += point2[0][0]
                        midPoint[1] += point2[0][1]
                        counter += 1
                midPoints.append([np.array((int(midPoint[0]/counter),int(midPoint[1]/counter)))])
            midPoints = np.array(midPoints)
            print(midPoints)

            #To find centre of the line
            M = cv2.moments(midPoints)
            if M["m00"] !=0 :
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                print("CX : "+str(cx)+"  CY : "+str(cy))
                cv2.circle(mask,(cx,cy),7, (0,255,255), 3)
                cv2.circle(mask, (sx, sy), 7, (255, 0, 255), -1)
                cv2.line(mask, (cx,cy), (sx, sy), (0,0,255), 4)
                dist = distance(cx,cy,sx,sy) 
                print(dist)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(mask,"Distance = " +str(round(dist,3)),(50,70), font, .5,(255,255,255),2,cv2.LINE_AA)

                #conditions if the tool goes out of frame
                if cx >= 330 :
                    print("Move Left")
                    cv2.putText(mask,"Move Left!",(50,50), font, .5,(255,255,255),2,cv2.LINE_AA)
                    #GPIO PINS TO BE ADDED
                if cx > 300 and cx < 330 :
                    print("BRAVO!")
                    cv2.putText(mask,"On Track!",(50,50), font, .5,(255,255,255),2,cv2.LINE_AA)
                    #GPIO PINS TO BE ADDED
                if cx <=300 :
                    print("Move Right")
                    cv2.putText(mask,"Move Right!",(50,50), font, .5,(255,255,255),2,cv2.LINE_AA)
                
                #Center point
                cv2.circle(frame, (cx,cy), 5, (255,255,255), -1)
        
    #img = cv2.add(mask, blank)
    cv2.drawContours(frame, c, -1, (0,255,0), 1)
    cv2.drawContours(frame, midPoints, -1, (0,0,255), 1)

    cv2.imshow('Output',mask)
    cv2.imshow('frame',frame)

    #print(len(contours))
    if cv2.waitKey(1) & 0xff == ord('q'):   # 1 is the time in ms
        break

cap.release()
cv2.destroyAllWindows()
