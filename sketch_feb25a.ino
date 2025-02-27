const int ledPin1 = 6;  // First LED on Pin 6
const int ledPin2 = 4;  // Second LED on Pin 4
const int ledPin3 = 3;  // Third LED on Pin 3

void setup() {
    pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
    pinMode(ledPin3, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read();  // Read command from Python
        
        if (command == '1') {  // Turn all LEDs ON
            digitalWrite(ledPin1, HIGH);
            digitalWrite(ledPin2, HIGH);
            digitalWrite(ledPin3, HIGH);
            Serial.println("All LEDs ON");
        } 
        else if (command == '0') {  // Turn all LEDs OFF
            digitalWrite(ledPin1, LOW);
            digitalWrite(ledPin2, LOW);
            digitalWrite(ledPin3, LOW);
            Serial.println("All LEDs OFF");
        }
    }
}