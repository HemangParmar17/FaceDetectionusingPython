import cv2

#Trained Haarcascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Webcame
webcam = cv2.VideoCapture(0)

#Iterte forever over frames
while True:

   #Read the current frame
   successful_frame_read,frame = webcam.read()

   #Must convert to grayscale
   grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   #Detect Faces
   face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

   #Draw a rectangle
   for (x, y, w, h) in face_coordinates:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

   #Display the image
   cv2.imshow('Face Detector', frame)
   key = cv2.waitKey(1)

   #Stop if Q key is pressed
   if key == 81 or key == 113:
      break

#Release the VideoCapture Object
webcam.release()

# #Detect Faces
# face_coordinates = trained_face_data.detectMultiScale(grayscale_img)
# #print(face_coordinates)
#
# #Draw rectangle around the faces
# for (x, y, w, h) in face_coordinates:
#   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#
# #Display the Image
# cv2.imshow('Face Detector', img)
# cv2.waitKey()

print("Face_Detection")