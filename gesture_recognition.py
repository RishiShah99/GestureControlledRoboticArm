# This code will be functionized for main.py

# This code will use media pipe to recognize hand gestures
import cv2 as cv
import mediapipe as mp
import serial

# Initialize the serial connection
ser = serial.Serial('COM3', 9600)  

# Drawing the lines in between landmarks
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Track the hands in real time
mphands = mp.solutions.hands

def run_gesture_recognition():
    # Access the webcam
    cap = cv.VideoCapture(0)   
    hands = mphands.Hands()

    # Loop to capture the video
    while True:
        data, img = cap.read()
        # Flip the image
        img = cv.cvtColor(cv.flip(img, 1), cv.COLOR_BGR2RGB)
        # Storing  the results
        results = hands.process(img)
        # Drawing the landmarks
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)

        # If there are multiple hands
        if results.multi_hand_landmarks:
            # Select the first hand only
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_drawing.draw_landmarks(img, hand_landmarks, mphands.HAND_CONNECTIONS)

            # Get the bounding box coordinates
            x_min, y_min, x_max, y_max = get_bounding_box(hand_landmarks)

            # Draw the bounding box
            cv.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Get the number of fingers that are up
            fingers = get_fingers_up(hand_landmarks)
            # Display the number of fingers that are up
            # print(fingers)

            # Call the send_fingers_to_arduino function inside the while loop
            send_fingers_to_arduino(fingers)

        # Display the image 
        cv.imshow('Hand Gesture Recognition', img)

        # Break the loop
        if cv.waitKey(1) & 0xFF == 27:
            break
    # Release the webcam
    cap.release()
    cv.destroyAllWindows()


def send_fingers_to_arduino(fingers):
    # Convert the fingers list to a string
    fingers_str = ''.join(map(str, fingers))

    # Send the fingers data to Arduino
    ser.write(fingers_str.encode())

# Function to get the bounding box
def get_bounding_box(hand_landmarks):
    x = []
    y = []
    for landmark in hand_landmarks.landmark:
        x.append(landmark.x)
        y.append(landmark.y)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    return int(x_min * 640), int(y_min * 480), int(x_max * 640), int(y_max * 480)

# Function to get the number of fingers that are up
def get_fingers_up(hand_landmarks):
    fingers = [0, 0, 0, 0, 0]
    # Thumb
    if hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y:
        fingers[0] = 1
    # Index
    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
        fingers[1] = 1
    # Middle
    if hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y:
        fingers[2] = 1
    # Ring
    if hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y:
        fingers[3] = 1
    # Pinky
    if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y:
        fingers[4] = 1
    return fingers

