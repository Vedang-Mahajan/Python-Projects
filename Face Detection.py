import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('Ourpic3.png')
# To capture image video from webcam
webcam = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while True:
    
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    
    for (x, y ,w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), ((randrange(256)), (randrange(256)), (randrange(256))), 10)
    
    cv2.imshow('Face Detection', frame)
    key = cv2.waitKey(1)

    if key==88 or key==120:
        break

webcam.release()

print("Code completed!")