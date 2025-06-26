import cv2
import mediapipe as mp

import time

class FaceMeshDetector():


    def __init__(self, staticMode=False,
               maxFaces=1,
               refine_landmarks=False,
               minDetectionConfidence=0.5,
               minTrackingConfidence=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.refine_landmarks = refine_landmarks
        self.minDetectionConfidence = minDetectionConfidence
        self.minTrackingConfidence = minTrackingConfidence



        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,self.refine_landmarks,self.minDetectionConfidence, self.minTrackingConfidence)
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness=1, circle_radius=2)

    def findFaceMesh(self, img, draw = True):

        facesLms = []
        self.imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRgb)
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_FACE_OVAL, self.drawSpecs,
                                           self.drawSpecs)

                face = []
                for id, lm in enumerate(faceLms.landmark):
                    # print(lm)

                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)

                    #print(id, x, y)
                    face.append([x,y])
                facesLms.append(face)

        return img, facesLms






def main():
    cap = cv2.VideoCapture(0)
    pTime = 0

    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(len(faces))

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 200, 10), 2)
        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()