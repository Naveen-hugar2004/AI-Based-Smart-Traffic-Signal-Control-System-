const int RED_PIN = 25;
const int YELLOW_PIN = 26;
const int GREEN_PIN = 27;

void setSignal(bool red, bool yellow, bool green) {
  digitalWrite(RED_PIN, red ? HIGH : LOW);
  digitalWrite(YELLOW_PIN, yellow ? HIGH : LOW);
  digitalWrite(GREEN_PIN, green ? HIGH : LOW);
}

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(YELLOW_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  Serial.begin(115200);
  setSignal(false, false, true);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "RED") setSignal(true, false, false);
    else if (command == "YELLOW") setSignal(false, true, false);
    else if (command == "GREEN") setSignal(false, false, true);
  }
}
