import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)



def getContours(img, imgContours):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    global Counter
    Counter = 0
    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 2000:
            Counter = Counter + 1
            cv2.drawContours(imgContours, contours,-1,(255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours,(x,y), (x+w, y +h),(0,255,0),5)
    cv2.putText(imgContours, "Num Cars: " + str(Counter), (70, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0),
                        2)
    #print(int(Counter))

    return img
  
  
  while True:
    # SIGNAL ONE
    success, img = cap.read()
    imgContours = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7,7),1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(img, cv2.CV_64F).var()
    #print(laplacian)
    
        if laplacian > 100:
        kerrnel = np.ones((5, 5))

        imgCanny = cv2.Canny(imgGray,51, 51)
        imgDil = cv2.dilate(imgCanny, kerrnel, iterations=1)
        getContours(imgDil,imgContours)
        cv2.imshow("Contours", imgContours)
        #cv2.imshow("Dilate", imgDil)
        #cv2.imshow("Canny", imgCanny)
        #cv2.imshow("img", img)
        #cv2.imshow("Gray", imgGray)
        #cv2.imshow("Blur", imgBlur)

    else:
        print(" Normal is ON")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
