import cv2

# Path to your video file
video_path = r"D:\Minor project\Car Traffic 2\Car_Parking_Space_Detector_YOLOv8\input_video\parking_space2.mp4"  # Replace with your actual video path

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Read the first frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if ret:
        cv2.imwrite("frame2.png", frame)  # Save the first frame as 'frame.png'
        print("Frame saved as 'frame.png'")
    else:
        print("Error: Could not read frame from video.")

    cap.release()  # Release the video capture object
