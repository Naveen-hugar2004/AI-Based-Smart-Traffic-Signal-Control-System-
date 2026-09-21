import cv2
import serial
from ultralytics import YOLO
from signal_logic import decide_signal

MODEL_PATH = "yolov8n.pt"
SERIAL_PORT = "COM3"  # Change for your computer
BAUD_RATE = 115200

VEHICLE_CLASSES = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck",
}

def main():
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Could not open camera")

    esp32 = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, verbose=False)
            vehicle_count = 0

            for result in results:
                for box in result.boxes:
                    class_id = int(box.cls[0])
                    if class_id in VEHICLE_CLASSES:
                        vehicle_count += 1
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        label = VEHICLE_CLASSES[class_id]
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x1, max(y1 - 10, 20)),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            signal = decide_signal(vehicle_count)
            esp32.write((signal + "\n").encode())

            cv2.putText(frame, f"Vehicles: {vehicle_count}  Signal: {signal}",
                        (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 255), 2)

            cv2.imshow("Smart Traffic Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        esp32.close()

if __name__ == "__main__":
    main()
