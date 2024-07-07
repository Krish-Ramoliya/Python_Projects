import face_recognition
import cmake
import numpy as np
import csv
import cv2
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load Known faces
Krish_image = face_recognition.load_image_file("Faces/Krishj.jpeg")
krish_encoding = face_recognition.face_encodings(Krish_image)[0]
lucy_image = face_recognition.load_image_file("Faces/lucy.jpeg")
lucy_encoding = face_recognition.face_encodings(lucy_image)[0]

known_face_encodings = [krish_encoding, lucy_encoding]
known_face_names = ["Krish", "lucy"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

#  Get the current date and time

now = datetime.now()
current_date= now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize Face
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)

        name = "Unknown"
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:

            font = cv2.FONT_HERSHEY_SIMPLEX
            bottonLeftCornerOfText = (10,100)
            fontscale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            linetype = 2
            cv2.putText(frame, name + "Present" , bottonLeftCornerOfText,font,fontscale,fontColor,thickness,linetype)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()