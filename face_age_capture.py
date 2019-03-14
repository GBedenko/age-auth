#!/usr/bin/env python

# Import libraries required for photo capture, file processing, etc.
import cv2
import requests
import json
import os


def capture_photo(path='photo.png'):
    """Captures a photo of the user via their main camera (usually their webcam)
       Saves the photo to a local file, default path is photo.png
       Return is void

       :param path: Optional parameter to modify path of captured photo"""

    # Use Webcam camera (or whichever is in slot 0)
    camera = cv2.VideoCapture(0)

    # Capture frame instantly
    ret, frame = camera.read()

    # Save image locally to provided path
    cv2.imwrite(path, frame)


def crop_photo(path='photo.png'):
    # Crops captured photo using existing library based on viola jones algorithm
    # Modifies the captured photo to just the face of the user

    # Command line tool for face crop python library
    os.system("autocrop --no-confirm")


def age_prediction():
    
    age_response = requests.get('http://localhost:8081/determine_age')

    age_json = age_response.json()
    
    return age_json["predicted_age"]


def placeholder_age_prediction(path='photo.png'):
    """Temporary Age Predictor placholder.
       Calls Microsoft Face API to determine the age according to the passed photo file path
       Returns the age as a float according to Microsoft's API

       :param path: File path of the photo of the user, default is photo.png"""

    # Microsoft Face API credentials required to authenticate request
    headers = {'Content-Type': 'application/octet-stream',
                        'Ocp-Apim-Subscription-Key': '871f68c8051e49b8b01435be2dd1fa35'}

    # Face API endpoint to request age
    face_api_url = 'https://uksouth.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=age'

    # Use photo at the provided path
    data = open(path, 'rb')

    # Post request to Microsoft Face API endpoint with photo
    face_results = requests.post(face_api_url , headers=headers, data=data)

    # Return only the age from json response, which will be a float
    return face_results.json()[0]["faceAttributes"]["age"]


def delete_captured_photo(path='photo.png'):
    """Deletes the captured photo at the provided path

       :param path: File path of the photo to delete, default is photo.png"""

    # Force remove file permanently
    os.remove(path)


def get_user_age():
    """Calls appropriate methods to capture photo, predict age based on it, then delete photo
       Returns estimated age of the user in a photo taken immediately
       Exception returned if any failure during the facial recognition process"""

    # Take photo of the user
    capture_photo()

    # Crop photo to just user's face
    crop_photo()

    try:

        # For now, estimate their age using placeholder, third party facial recognition API
        age = age_prediction()
        
        # Return the age as float as result
        return(age)

    except:
        # If age prediction via facial recognition fails, return error message explaining this
        raise Exception("Facial recognition failed")

    finally:
        # Delete photo after use, always run so the data is immediately deleted
        delete_captured_photo()

if __name__ == "__main__":
    get_user_age()

