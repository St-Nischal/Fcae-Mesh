import cv2
import mediapipe as mp

import time

from FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)
pTime = 0

detector = FaceMeshDetector()

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    if len(faces) != 0:
        print(faces[0])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 200, 10), 2)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()