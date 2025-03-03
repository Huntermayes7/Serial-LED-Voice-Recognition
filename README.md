Voice-Controlled LED System with Arduino and Python

Overview

This project implements a voice-controlled LED system using Python and Arduino. A speech recognition model allows users to turn LEDs on, off, or stop the program using voice commands. The system communicates via serial connection using the PySerial and SpeechRecognition libraries.

Features

Voice Recognition: Users can say "L E D on," "L E D off," or "stop" to control the LEDs.
Arduino Communication: Python sends serial signals to the Arduino to turn LEDs on/off.
Speech Recognition Handling: Uses Google Speech Recognition to interpret commands.
Technologies Used

Python 3
Arduino Mega 2560
PySerial 3.5 (for serial communication)
SpeechRecognition (for voice command processing)
Arduino IDE
Setup and Installation

1. Install Python Dependencies
pip install pyserial speechrecognition
2. Upload the Arduino Code
Load the following code into the Arduino IDE and upload it to the board:

const int ledPin1 = 6;
const int ledPin2 = 4;
const int ledPin3 = 3;

void setup() {
    pinMode(ledPin1, OUTPUT);
    pinMode(ledPin2, OUTPUT);
    pinMode(ledPin3, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char command = Serial.read();
        if (command == '1') {  
            digitalWrite(ledPin1, HIGH);
            digitalWrite(ledPin2, HIGH);
            digitalWrite(ledPin3, HIGH);
            Serial.println("All LEDs ON");
        } 
        else if (command == '0') {  
            digitalWrite(ledPin1, LOW);
            digitalWrite(ledPin2, LOW);
            digitalWrite(ledPin3, LOW);
            Serial.println("All LEDs OFF");
        }
    }
}
3. Run the Python Script
Use the following Python script to enable voice recognition and control the LEDs:

import serial
import speech_recognition as sr
import time

arduino = serial.Serial(port='/dev/tty.usbmodem101', baudrate=9600, timeout=1)
time.sleep(2)

recognizer = sr.Recognizer()

def recognize_command():
    with sr.Microphone() as source:
        print("Say 'L E D on', 'L E D off', or 'stop' to exit...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized command: {command}")

            words = command.split()
            if "l" in words and "e" in words and "d" in words:
                if "on" in words:
                    return "led on"
                elif "off" in words:
                    return "led off"
            
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Speech Recognition service is unavailable")
        return None

def send_command_to_arduino(command):
    if command == "led on":
        arduino.write(b'1')
        print("All LEDs turned ON")
    elif command == "led off":
        arduino.write(b'0')
        print("All LEDs turned OFF")
    elif command in ["stop", "exit"]:
        print("Stopping the program...")
        return False
    else:
        print("Invalid command, say 'L E D on', 'L E D off', or 'stop'.")
    return True

if __name__ == "__main__":
    running = True
    while running:
        voice_command = recognize_command()
        if voice_command:
            running = send_command_to_arduino(voice_command)
How It Works

The Python script listens for a voice command.
Recognized commands are converted into text.
If the command is "LED on" or "LED off," a signal is sent to the Arduino.
The Arduino processes the signal and turns LEDs on/off accordingly.
Saying "stop" ends the program and turns off all LEDs.
Future Enhancements

Improve recognition accuracy by fine-tuning speech model settings.
Add more LED control options, such as brightness adjustment.
Expand compatibility with different Arduino models.
License

This project is open-source and available under the MIT License.
