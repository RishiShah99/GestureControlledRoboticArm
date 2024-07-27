# Gesture Controlled Robotic Arm

This repository contains the implementation of a robotic arm controlled by hand gestures. The project leverages machine learning techniques and Arduino to interpret gestures and control the movements of the robotic arm accordingly.

## Table of Contents

- [Project Description](#project-description)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Gesture Recognition](#gesture-recognition)
- [Robotic Arm Control](#robotic-arm-control)
- [Modules](#modules)
- [Usage](#usage)
- [License](#license)

## Project Description

The goal of this project is to develop a robotic arm that can be controlled using hand gestures. The system uses a combination of hardware and software to capture, process, and interpret gestures, which are then translated into commands for the robotic arm.

## Hardware Components

- **Robotic Arm**: A custom-designed robotic arm created using CAD software, with multiple servos to control the fingers.
- **Microcontroller**: An Arduino microcontroller to interface with the robotic arm and receive commands.
- **Sensors**: A Leap Motion sensor or other gesture recognition hardware to capture hand movements.

## Software Components

- **Python**: Used for gesture recognition and communication with the Arduino.
- **Arduino IDE**: Used for programming the microcontroller to control the robotic arm.

## Gesture Recognition

The system uses the MediaPipe library to capture and recognize hand gestures. The gestures are processed to determine the position of each finger, and the results are sent to the Arduino to control the servos.

### gesture_recognition.py

This script captures video input, processes the frames to recognize hand gestures using MediaPipe, and sends the recognized finger positions to the Arduino via serial communication.

## Robotic Arm Control

The Arduino receives the finger positions from the gesture recognition script and controls the corresponding servos to mimic the gestures.

### main.cpp

This script runs on the Arduino and receives the finger position data via serial communication, controlling the servos to move the robotic arm's fingers.

## Modules

To run the code, you need the following modules:

```bash
# Install the required modules using pip
pip install opencv-python
pip install mediapipe
pip install pyserial
```

## Usage 
1. Clone the repo and navigate to project directory
```bash
git clone https://github.com/RishiShah99/GestureControlledRoboticArm.git
cd GestureControlledRoboticArm
```
2. Upload the arduino code
3. Run gesture_recognition.py
