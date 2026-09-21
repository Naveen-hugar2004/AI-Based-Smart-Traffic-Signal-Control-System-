# Smart Traffic Signal Control Using ESP32 and YOLOv8

A smart traffic system that automatically controls traffic signals based on the number of vehicles detected on the road.

## Overview
Camera -> Python + YOLOv8 -> Vehicle Count -> Signal Decision -> Serial -> ESP32 -> Traffic LEDs

## Features
- Real-time vehicle detection using YOLOv8
- Vehicle counting from a live camera feed
- Automatic Red/Yellow/Green signal decision
- ESP32-based traffic signal control
- Serial communication between Python and ESP32

## Structure
smart-traffic-system/
- README.md
- requirements.txt
- .gitignore
- python/vehicle_detection.py
- python/signal_logic.py
- esp32/traffic_signal.ino
- docs/architecture.md

## Setup
Install Python packages:
`pip install -r requirements.txt`

Update `SERIAL_PORT` in `python/vehicle_detection.py`, connect the ESP32, upload the Arduino sketch, then run:
`python python/vehicle_detection.py`

## Signal Logic
Prototype defaults:
- Low vehicle count -> GREEN
- Medium vehicle count -> YELLOW
- High vehicle count -> RED

The original project presentation does not specify the exact GPIO wiring, serial port, model weights, or thresholds, so these repository values are prototype defaults.

## Project Results
The project presentation reports real-time vehicle detection, automatic traffic-light changes based on vehicle count, reduced manual control, and potential reduction of congestion and waiting time.
