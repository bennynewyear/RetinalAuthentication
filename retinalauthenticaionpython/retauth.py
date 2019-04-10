import numpy as np
import cv2
import turtle

circles_lst = list()

def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click")
        circles_lst.append((x, y))


def main():
    # initiate face haar cascade
    face_cascade = cv2.CascadeClassifier('opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
    # initiate eye haar cascade
    eye_cascade = cv2.CascadeClassifier('opencv-master\data\haarcascades\haarcascade_eye.xml')

    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Pattern drawing")
    cv2.setMouseCallback("Pattern drawing", mouse_drawing)

    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # draw face recognition box
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            # draw eye recognition box
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                roi_gray_eyes = gray[ey:ey + eh, ex:ex + ew]
                roi_color_eyes = img[ey:ey + eh, ex:ex + ew]
                #circles = cv2.HoughCircles(roi_gray_eyes, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
                circles = cv2.HoughCircles(roi_gray_eyes, cv2.HOUGH_GRADIENT, 1, 200, param1=200, param2=1, minRadius=0,
                                           maxRadius=0)
                # draw pupil recognition box
                try:
                    for i in circles[0, :]:
                        cv2.circle(roi_color_eyes, (i[0], i[1]), i[2], (255, 255, 255), 2)
                        print("drawing circle")
                        # draw the center of the circle
                        cv2.circle(roi_color_eyes, (i[0], i[1]), 2, (255, 255, 255), 3)
                except Exception as e:
                    print(e)
                cv2.imshow('img', img)
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break

        for center_position in circles_lst:
            cv2.circle(img, center_position, 5, (0, 0, 255), -1)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        # specify img as fixed point on camera
        cv2.circle(img, (300,300), 2, (255, 255, 0), -1, 8, 0)

    cap.release()
    cv2.destroyAllWindows()


main()
