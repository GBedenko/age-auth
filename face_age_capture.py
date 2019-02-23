#!/usr/bin/env python

import cv2
import requests
import json
import os

# Use Webcam camera
camera = cv2.VideoCapture(0)

# Capture frame instantly
ret, frame = camera.read()

# Save image locally
cv2.imwrite('photo.png', frame)

# Microsoft Face API required to authenticate request
headers = {'Content-Type': 'application/octet-stream', 
                    'Ocp-Apim-Subscription-Key': '871f68c8051e49b8b01435be2dd1fa35'}

# Face API endpoint to also request age
face_api_url = 'https://uksouth.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=age'
 
# Use photo just captured from webcam
data = open('photo.png', 'rb')

# Post request to Microsoft Face API endpoint with photo
face_results = requests.post(face_api_url , headers=headers, data=data)

# Output results including age
print(json.dumps(face_results.json(), indent=4, sort_keys=True))
print(json.dumps(face_results.json()[0]["faceAttributes"]["age"], indent=4, sort_keys=True))

# Delete photo after use
os.remove("photo.png")