import face_recognition
import os
from cv2 import cv2
import numpy as np
from pprint import pprint


KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  


video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Returns (R, G, B) from name
# def name_to_color(name):
#     # Take 3 first letters, tolower()
#     # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
#     color = [(ord(c.lower())-97)*8 for c in name[:3]]
#     return color


print('Loading known faces...')
known_faces = []
known_names = []


for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        # Load an image
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
        encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(encoding)
        known_names.append(name)


print('Processing unknown faces...')
pprint(known_names)


while True:


    ret, image = video.read()


    locations = face_recognition.face_locations(image, model=MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    print(f', found {len(encodings)} face(s)')


    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        
        match = None
        if True in results:  # If at least one is true, get a name of first of found labels
            match = known_names[results.index(True)]
            print(f' - {match} from {results}')

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2] + 22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

    # # Show image
    # cv2.imshow(filename, image)
    # cv2.waitKey(0)
    # cv2.destroyWindow(filename)

    cv2.imshow("attendance bit", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# cv2.waitKey(0)
try:
    cv2.destroyWindow(filename)
except:
    pass
