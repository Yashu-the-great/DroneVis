import face_recognition
import numpy as np
import cv2
import matplotlib.pyplot as plt
from pyautogui import size

from movement import move_forward,move_backward,move_left,move_right

my_face=face_recognition.load_image_file('../Assets/img.jpg')
my_face_encoding=face_recognition.face_encodings(my_face)[0]
my_face_landmarks=face_recognition.face_landmarks(my_face)

fl=600 #Focal Length set to be any random number for experimentation purposes    
cap = cv2.VideoCapture(0)
d=0
t = 0
b = 0
l=0
r=0
# width,height = size()
width,height = 700,700
def main(t,b,r,l):
    while True:
        _,img= cap.read()
        img=cv2.flip(img,1)
        cv2.resize(img,(width,height))
        face_encoding= face_recognition.face_encodings(img)
        if(face_encoding!=[]):
            result = face_recognition.compare_faces([my_face_encoding],face_encoding[0])#Checking if face is recognised
            if(result[0]):
                t,r,b,l = face_recognition.face_locations(img)[0]
                # face_image = img[t:b, l:r]
                cv2.rectangle(img,(l,t),(r,b),(255,0,0),2)
                p=r-l
                w=6
                d=(w*fl)/p
                cv2.putText(
                img = img,
                text = f" Distance : {round(d)}",
                org = (0, 100),
                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                fontScale = 1.0,
                color = (125, 246, 55),
                thickness = 1
                )
                if d <13 :
                    move_backward()
                if d>13:
                    move_forward()

                cv2.circle(img,(int((r+l)/2),int((t+b)/2)), 3, (0,255,255), 2) #Centroid of face
                center = (int((r+l)/2),int((t+b)/2))
                if center[0] > int(width/2):
                    move_left()
                if center[0] < int(width/2):
                    move_right()
        cv2.circle(img,(int(height/2),int(width/2)), 3, (0,0,255), 5) # cross hair of Drone Point Of View
        cv2.imshow("Frame",img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
            



if __name__ == "__main__":
    d=0
    t = 0
    b = 0
    l=0
    r=0
    while(True):
        main(t,b,r,l)