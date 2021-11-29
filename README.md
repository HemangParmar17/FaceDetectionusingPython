# FaceDetectionusingPython
Face Detection using haar-cascade algorithm and open-cv in python

#Important Links

haarcascade xml file -> https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Steps:

Load Images(Front Faces) or Capture video using webcame.
Convert images into grayscale(Black & White).
Train the algorithm to detect Faces.
opencv -> OpenCV is a library of programming functions mainly aimed at real-time computer vision. haarcascade -> Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier.

#Install opencv pip install opencv-python

#Create a file namely Face_Detector.py

#Import images with front face as we use haarcascade algorithm with front face trained data

#Read the image Image = cv2.imread('img file name')

#Convert image to grayscale cv2.cvtColor()

#Detect faces trained_face_data.detectMultiScale()

#Draw a rectangle cv2.rectangle()

#Display the image cv2.imshow('Face Detector', Image)

#Delay to show the image cv2.waitkey()

#For webcame webcame = cv2.VideoCapture(0)

#Read the frame webcame.read()

#Release the VideoCapture Object webcam.release()
