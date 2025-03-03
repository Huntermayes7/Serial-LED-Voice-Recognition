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
   - Flash the Arduino with code that listens for serial commands to control LEDs.  

3. **Configure Python Script**  
   - Implement speech recognition to detect voice commands.  
   - Establish serial communication with Arduino.  

4. **Test the System**  
   - Ensure correct response to "L E D on," "L E D off," and "stop" commands.  
   - Adjust recognition sensitivity if necessary.  

5. **Refinement and Optimization**  
   - Improve speech recognition accuracy.  
   - Enhance system responsiveness.  

## Versions Used  
- **Python:** 3.x  
- **PySerial:** 3.5  
- **SpeechRecognition:** Latest  
- **Arduino IDE:** Latest  
- **Hardware:** Arduino Mega 2560  
