# Voice-Controlled Robot Project

## Project Overview

This project focuses on developing a voice-controlled robot using offline speech recognition to perform advanced movements and communicate with the user. The system allows the robot to interpret voice commands for basic movements such as "go", "stop", "turn right", and "turn left," as well as more complex commands specifying distances and angles. The robot can also provide feedback to the user through speech, offering a more interactive experience.

## Key Achievements

- **Offline Speech Recognition**: Implemented using the Vosk model, which processes voice commands without relying on cloud-based services.
- **Command Processing**: Voice commands are converted into text, saved to a file, and processed to identify movement instructions.
- **Movement Execution**: The system uses the Tello library to control the robot's movement based on the recognized commands.
- **Advanced Commands**: The robot can handle more complex instructions like "go forward 5 meters" or "rotate left 90 degrees," interpreting distances and angles with the word2num Python library.
- **User Communication**: The pyttsx3 library was integrated to enable the robot to speak responses, such as battery level or flight time.
  
## Technologies Used

- **Vosk Model**: For offline speech recognition and converting voice commands into text.
- **Tello Library**: For controlling the Tello drone, executing commands, and retrieving information.
- **word2num Library**: To convert spoken numbers into numeric values for more specific command instructions.
- **pyttsx3 Library**: For converting text to speech, enabling the robot to provide feedback to the user.
  
## Features

### 1. **Basic Voice Commands (P-Level)**
- The robot responds to simple commands such as "go," "stop," "turn right," and "turn left."
- Commands are recognized using the Vosk voice detection model and executed using the Tello library.

### 2. **Movement Control (C-Level)**
- The robot can move based on voice commands, performing actions like turning or moving forward and backward.
  
### 3. **User Feedback (D-Level)**
- The robot provides feedback such as battery level or flight status through speech using pyttsx3.

### 4. **Advanced Command Handling (HD-Level)**
- The robot can interpret complex commands that include distances and angles, such as "go forward 5 meters" or "rotate right 90 degrees." These commands are processed using the word2num library to extract numeric values.

### Example Commands
- "Go forward"
- "Stop"
- "Turn right"
- "Rotate left 90 degrees"
- "Go forward 10 meters"

## Demo Videos
- **Basic Commands Demo**: [Watch Here](https://youtu.be/2BqnrrCUiY)
- **Movement Commands Demo**: [Watch Here](https://youtu.be/4Ya7ZfpJOPI)
- **Feedback Communication Demo**: [Watch Here](https://www.youtube.com/watch?v=WyBMXisvN4)
- **Advanced Commands Demo**: [Watch Here](https://www.youtube.com/watch?v=YsD01k3uU0c)

## Project Limitations
- **Offline Speech Recognition**: While Vosk works offline, its accuracy may not be as high as cloud-based solutions.
- **Limited Vocabulary**: The system can only recognize a fixed set of predefined commands.
- **Basic Movements**: Currently, the robot handles basic movement commands and does not support advanced navigation or perception capabilities.

## Future Enhancements
- **Natural Language Processing**: Expanding the vocabulary to support more complex natural language interactions.
- **Cloud-based Speech Recognition**: Exploring cloud services for more accurate real-time speech processing.
- **Advanced Robotics**: Incorporating additional sensors and capabilities for enhanced perception and autonomous navigation.

## Conclusion

This project successfully demonstrated the use of voice recognition for controlling a robot, with both basic and advanced movement commands. It also established two-way communication between the robot and the user, making robotics interaction more intuitive and accessible.

---
