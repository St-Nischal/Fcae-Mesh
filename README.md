Face Mesh Detection with OpenCV and MediaPipe

This application uses MediaPipe's Face Mesh solution to detect facial landmarks in real-time via webcam. It draws the face mesh overlay and displays the frame rate (FPS) live.
📦 Features

    Real-time face mesh detection from webcam

    Draws facial landmarks (face oval)

    Displays frame rate (FPS)

    Configurable detection settings (e.g., max number of faces)

🛠️ Requirements

    Python 3.7+

    OpenCV (cv2)

    MediaPipe

📥 Installation

First, clone the repository or download the script. Then install the required libraries:

pip install opencv-python mediapipe

🚀 Usage

Run the application with:

python face_mesh_app.py

Press q to quit the application window.
🧠 How It Works

    Initializes a webcam feed using OpenCV.

    Processes each frame using MediaPipe's Face Mesh detector.

    Draws the detected face landmarks on the frame.

    Prints the number of detected faces and shows FPS.

🧩 Configuration

You can adjust parameters in the FaceMeshDetector class:

detector = FaceMeshDetector(
    staticMode=False,
    maxFaces=1,
    refine_landmarks=False,
    minDetectionConfidence=0.5,
    minTrackingConfidence=0.5
)

    staticMode: Set True for static images (no tracking).

    maxFaces: Number of faces to detect.

    refine_landmarks: If True, includes more refined landmarks.

    minDetectionConfidence: Minimum confidence for face detection.

    minTrackingConfidence: Minimum confidence for landmark tracking.

📸 Example Output

    A window displaying your webcam feed with face landmarks drawn.

    Console will print number of detected faces per frame.
