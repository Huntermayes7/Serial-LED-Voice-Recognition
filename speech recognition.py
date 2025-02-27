import serial
import speech_recognition as sr
import time

# Set up the serial connection (update the COM port based on your system)
arduino = serial.Serial(port='/dev/tty.usbmodem101', baudrate=9600, timeout=1)  # Update with the correct port
time.sleep(2)  # Wait for the connection to establish

# Initialize speech recognizer
recognizer = sr.Recognizer()

def recognize_command():
    with sr.Microphone() as source:
        print("Say 'L E D on', 'L E D off', or 'stop' to exit...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()  # Convert to lowercase
            print(f"Recognized command: {command}")
            
            # Split the recognized command into individual words
            words = command.split()

            # Check for the individual letters "L", "E", "D"
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
        arduino.write(b'1')  # Send '1' to turn all LEDs on
        print("All LEDs turned ON")
    elif command == "led off":
        arduino.write(b'0')  # Send '0' to turn all LEDs off
        print("All LEDs turned OFF")
    elif command in ["stop", "exit"]:
        print("Stopping the program...")
        return False  # Signal to stop the loop
    else:
        print("Invalid command, say 'L E D on', 'L E D off', or 'stop'.")
    return True  # Continue running

if __name__ == "__main__":
    running = True
    while running:
        voice_command = recognize_command()
        if voice_command:
            running = send_command_to_arduino(voice_command)