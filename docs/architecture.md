# System Architecture 

```text
+------------------+
| Camera / Webcam  |
+--------+---------+
         |
         v
+-------------------------+
| Python + YOLOv8         |
| Vehicle Detection       |
+-----------+-------------+
            |
            v
+-------------------------+
| Vehicle Count           |
+-----------+-------------+
            |
            v
+-------------------------+
| Signal Decision Logic   |
| RED / YELLOW / GREEN    |
+-----------+-------------+
            |
            | Serial
            v
+-------------------------+
| ESP32                   |
| Traffic Signal Control  |
+-----+---------+---------+
      |         |         |
      v         v         v
    RED LED  YELLOW LED  GREEN LED
```

## Workflow
1. Capture live video.
2. Run YOLOv8 detection.
3. Identify vehicle classes.
4. Count vehicles.
5. Apply signal decision logic.
6. Send the selected command over serial.
7. ESP32 changes the corresponding traffic-light output.
