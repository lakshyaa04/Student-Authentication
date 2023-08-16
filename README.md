# Student-Authentication
This project focuses on implementing a student authentication system that utilizes image processing and recognition techniques. 
The aim is to prevent dishonest practices such as cheating or impersonation during online exams and classes. 
The system primarily employs Aadhar numbers as the primary or unique identification keys. 
The process involves preprocessing images containing recent student photos along with their associated data, which are then compared with the current images
 captured during exams or classes.
 This approach ensures the authenticity of the student's identity and helps to curb unauthorized behavior.

 Libraries and Tools Used:

Flask: Framework for creating web applications in Python.
OpenCV: Library for computer vision tasks, used for capturing and processing images from the camera.
DeepFace: A wrapper around popular deep learning models for face recognition and verification.

About:

This Flask-based web application employs image processing and recognition techniques to authenticate students during online exams or classes.
 It captures real-time images, compares them with preprocessed images, and verifies the student's identity.
 The OpenCV library is used for camera access and image processing, while the DeepFace library is used for face verification. 
The application uses Flask's routing system to manage different functionalities, and session variables to store user information. 
The user experience includes capturing images and receiving verification results through a user-friendly interface.
