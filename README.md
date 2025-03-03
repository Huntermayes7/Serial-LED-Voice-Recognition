# Voice-Controlled LED System with Arduino and Python  

## Dataset  
This project does not require a traditional dataset. Instead, it relies on real-time voice commands recognized through the SpeechRecognition library. The system interprets spoken commands to control LEDs via Arduino.  

## References  
- [PySerial Documentation](https://pyserial.readthedocs.io/en/latest/)  
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)  
- [Arduino Documentation](https://www.arduino.cc/reference/en/)  

## Project Steps  

1. **Set Up the Environment**  
   - Install Python dependencies.  
   - Connect Arduino to the system.  

2. **Upload Arduino Code**  
   - Using Arduino IDE, Flash the Arduino with code that listens for serial commands to control LEDs.  

3. **Configure Python Script**  
   - Implement speech recognition to detect voice commands.  
   - Establish serial communication with Arduino.  

4. **Test the System**  
   - Ensure correct response to "L E D on," "L E D off," and "stop" commands.  
   - Adjust recognition sensitivity if necessary.  

5. **Refinement and Optimization**  
   - Improve speech recognition accuracy.  
   - Enhance system responsiveness.  
6. **Troubleshooting**  
   - **No response from Arduino:**
     - Ensure the correct **COM port** is used in the Python script.
     - MAC: "usbmodem101".
   - **LEDs not turning on/off:**
     -Verify that the Arduino is properly flashed with the latest code
     - Make sure you are speaking loud enough.  
   - **Speech recognition not working:**  
     - Check microphone permissions.  
     - Reduce background noise.  
     - Adjust sensitivity settings in the SpeechRecognition library.  
   - **Serial communication issues:**
     - Try restarting the Arduino and Python script.
     - Make sure "brew" is installed in terminal (MAC)  

## Versions Used  
- **Python:** 3.x  
- **PySerial:** 3.5  
- **SpeechRecognition:** Latest  
- **Arduino IDE:** Latest  
- **Hardware:** Arduino Mega 2560  
