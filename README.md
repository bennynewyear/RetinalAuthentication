# RetinalAuthentication
This is a capstone project for CSEC-490 Capstone in Computing Security, for CSEC students at Rochester Institute of Technology. The goal of this project was to implement biometrics in the form of retinal authentication for a mobile device, which can be readily accessible for the general consumer to use. It does so by engaging the camera on certain speciality phones, particularly ones with a built-in IR camera, to detect the user's eyes and retinas. The user is then prompted to visually draw a pattern on the phone's screen using their eyes, similar to the swiping pattern on Android devices. If the pattern is correct, the user is authenticated into the device if they are a valid authorized user. 

### Installation
Pre-requisites:
* Python 3.7+
* Android Studio
* Mobile device with IR camera (ie. Galaxy S7)

### Setup
Push the application from Android Studio onto a supported phone with a built-in IR camera.

OR

Download the Python script onto any directory on your computer and run the script from IDLE or any Python IDE.

### Issues
* Current iteration does not accurately detect retinas 

### Future works
* Integrate all applications into one singular application
* Fine-tune retinal detection capabilities
* Implement a database to store previously authenticated users
* Create a GUI for all available capabilities on the application 

### Acknowledgements
Utilizes OpenCV as an open source library for a majority of the application functions and Android Studio as the primary IDE.

Special thanks to our sponsor IPPSec and our faculty advisor Bo Yuan.

### Authors
Jhony Alavez, Computing Security, jia2707@rit.edu

Nicholas Laufer, Computing Security, nxl6264@rit.edu

Nicholas Kurland, Computing Security, ntk1002@rit.edu

Benny Tan, Computing Security, bt4168@rit.edu
