import cv2
from tracker import *

# Create tracker object
tracker = EuclideanDistTracker()
tracker2 = EuclideanDistTracker()

cap =cv2.VideoCapture('highway.mp4')
cap2 = cv2.VideoCapture('highway.mp4')


# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=70, varThreshold=40)
object_detector2 = cv2.createBackgroundSubtractorMOG2(history=70, varThreshold=40)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
    height, width, _ = frame.shape
    # Extract Region of interest
    roi = frame[0: 720, 0: 1280]


    ret1, frame1 = cap2.read()
    height1,width2,_=frame1.shape
    roi2 = frame1[0: 720, 0: 1280]
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    laplacian1 = cv2.Laplacian(gray1, cv2.CV_64F).var()



    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    print(len(detections))
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 300:
            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)


            detections.append([x, y, w, h])

    mask1 = object_detector2.apply(roi2)
    _, mask1 = cv2.threshold(mask1, 254, 255, cv2.THRESH_BINARY)
    contours1, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections2 = []
    print(len(detections2))
    for cnt in contours1:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 300:
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)

            detections2.append([x, y, w, h])

    # 2. Object Tracking
    boxes_ids = tracker.update(detections)

    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        count_traffic_one = int(len(boxes_ids)) #print how many object detected in the frame
        print(count_traffic_one)
        #print(type(count_traffic_one))
        if count_traffic_one >0 and count_traffic_one<3:
            print(" few cars")
        elif count_traffic_one >=3:
            print("medium traffic")
        else:
            print(" high traffic !")

    boxes_ids2 = tracker.update(detections)

    for box_id2 in boxes_ids2:
        x2, y2, w2, h2, id2 = box_id2
        cv2.putText(roi2, str(id2), (x2, y2 - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi2, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 3)
        count_traffic_two = int(len(boxes_ids2))  # print how many object detected in the frame
        print(count_traffic_two)
        # print(type(count_traffic_one))
        if count_traffic_two > 0 and count_traffic_two < 3:
            print(" few cars TRAFFIC TWO !")
        elif count_traffic_one >= 3:
            print("medium traffic TRAFFIC TWO!")
        else:
            print(" high traffic TRAFFIC TWO!")



        if count_traffic_one > count_traffic_two:
            print("Green light is on for traffic one!")
            print("Red light for traffic TWO ")
   # cv2.imshow("roi TRAFFIC TWO", roi2)
   # cv2.imshow("Frame TRAFFIC TWO", frame1)
    #cv2.imshow("Mask TRAFFIC TWO", mask1)

    #cv2.imshow("roi", roi)
    #cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:

        break
bob = count_traffic_one
cap.release()
cv2.destroyAllWindows()
