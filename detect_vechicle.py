import cv2

# Load the pre-trained vehicle detection model
vehicle_cascade = cv2.CascadeClassifier('cars.xml')


# Function to detect vehicles in an image
def detect_vehicles(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the image
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected vehicles
    for (x, y, w, h) in vehicles:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image


# Load the video file
video = cv2.VideoCapture('traffic.mp4')
#video = cv2.VideoCapture(0)


# Loop through each frame of the video
while True:
    # Read the current frame
    ret, frame = video.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Detect vehicles in the frame
    frame = detect_vehicles(frame)

    # Display the frame with detected vehicles
    cv2.imshow('Vehicle Detection', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
video.release()
cv2.destroyAllWindows()
