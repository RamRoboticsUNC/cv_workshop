import cv2

# Initialize the face detector with the YuNet model
detector = cv2.FaceDetectorYN.create("model.onnx", "", (300, 300))

# Set up video capture from camera (index 1) (or index 0, you may have to try both)
cv2.namedWindow("cam")
capture = cv2.VideoCapture(0)

# Check if the camera is accessible
if capture.isOpened():
    rval, frame = capture.read()
    img_w, img_h = frame.shape[1], frame.shape[0]
    detector.setInputSize((img_w, img_h))
else:
    rval = False

# Main loop for real-time face detection
while rval:
    rval, frame = capture.read()
    if not rval:
        break

    # Detect faces in the current frame
    detections = detector.detect(frame)[1]

    if detections is not None:
        print("I detect " + str(len(detections)) + " faces")
    else
        print("I see no faces")

    # Show the video feed with detections
    cv2.imshow("cam", frame)

    # Exit loop when 'Esc' key (27) is pressed
    if cv2.waitKey(27) == 27:
        break

# Release resources
capture.release()
cv2.destroyAllWindows()