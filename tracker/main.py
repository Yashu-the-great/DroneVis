import cv2
import face_rec

    
cap = cv2.VideoCapture(0)

tracker = cv2.legacy_TrackerCSRT.create()
success, img = cap.read()
for i in range(50):
    bbox = face_rec.recognise()
print(bbox)
#    0     1    2     3
# (left, top, right,bottom)
bbox = (bbox[0], bbox[1], (bbox[2]-bbox[0]), (bbox[3]-bbox[1]))
# bbox = cv2.selectROI(img)
tracker.init(img, bbox)



def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    
    success, bbox = tracker.update(img)
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Loss", (75, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        for i in range(50):
            bbox = face_rec.recognise()
        print(bbox)
        #    0     1    2     3
        # (left, top, right,bottom)
        if bbox != None:
            bbox = (bbox[0], bbox[1], (bbox[2]-bbox[0]), (bbox[3]-bbox[1]))
            print(bbox)
            tracker = cv2.legacy_TrackerCSRT.create()
            tracker.init(img, bbox)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (75, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
