// Define the GPIO pin number for the touch sensor and built-in LED
const int touchPin = 27;      // GPIO 27 (touch sensor pin)
const int ledPin = 2;         // Built-in LED pin (for many Arduino boards)

// Initialize the touch pin and LED pin
void setup() {
  // Set the touchPin as input and ledPin as output
  pinMode(touchPin, INPUT);
  pinMode(ledPin, OUTPUT);

  // Start serial communication (optional for debugging)
  Serial.begin(9600);
}

void loop() {
  // Read the state of the touch sensor pin
  int sensorState = digitalRead(touchPin);
  
  // If the touch sensor is touched (HIGH), turn on the LED
  if (sensorState == HIGH) {
    digitalWrite(ledPin, HIGH);  // Turn on the LED
    Serial.println("LED ON");
  } else {
    digitalWrite(ledPin, LOW);   // Turn off the LED
    Serial.println("LED OFF");
  }

  // Small delay for stability
  delay(100);
}