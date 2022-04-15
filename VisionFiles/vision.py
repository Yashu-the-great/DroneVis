import cv2
import face_recognition
import numpy as np

video_capture = cv2.VideoCapture(0)
width = 640
height = 480
# 640 X 480 img
video_capture.set(3,width)
video_capture.set(4,height)
Yashu_image = face_recognition.load_image_file("./VisionFiles/img.jpg")
Yashu_image_encodings = face_recognition.face_encodings(Yashu_image)[0]
known_face_encodings = [
    Yashu_image_encodings,
]
known_face_names = ["Yashu Maurya"]
face_locations = []
face_names = []

face_encodings = []
process_this_frame = True
fl = 600


def recognise(process_this_frame, fl):
    _, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings,
                                                     face_encoding)
            name = "Human"
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            process_this_frame = not process_this_frame

            for (top, right, bottom,
                 left), name in zip(face_locations, face_names):
                top *= 4
                bottom *= 4
                left *= 4
                right *= 4
                p = right - left
                w = 6
                d = (w * fl) / p
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0),
                              5)
                cv2.rectangle(frame, (left, bottom - 36), (right, bottom),
                              (0, 0, 255), cv2.FILLED)
                cv2.putText(
                    frame,
                    str(d),
                    (left + 6, bottom - 6),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.6,
                    (255, 255, 255),
                    2,
                )
                cv2.circle(
                    frame,
                    (int((right + left) / 2), int((top + bottom) / 2)),
                    3,
                    (0, 255, 255),
                    2,
                )
            cv2.circle(frame, (int(width/2),int(height/2)), 3, (0, 0, 255), 5) #center
            cv2.imshow("Only great faces are recognised", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                video_capture.release()
                cv2.destroyAllWindows()
                break
            return ((int((right + left) / 2), int((top + bottom) / 2)), d)