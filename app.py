#!/usr/bin/env python

# Import Flask to host server
from flask import Flask, request, render_template

# Import modules for functionality
import scan_webpage_keywords
import face_age_capture
import json

# Create a Flask app to run as a web server to host local API
app = Flask(__name__)


# GET request for retrieving scan result
@app.route("/scan")
def scan():
    """Endpoint for requesting a regex to be scanned on the given url
       e.g. /scan?url=http://www.google.com&regex=beer
       Returns boolean whether regex found in webpage or not"""

    try:
        # Save regex query parameter
        regex = request.args.get('regex')

        # Save url query parameter
        url = request.args.get('url')

    except:
        # If unable to retrieve either parameter, return error message
        return "Incorrect query parameters"

    try:
        # Call functionality to verify if regex is contained in webpage
        scan_result = scan_webpage_keywords.contains_keyword(regex, url)
        
        # Save scan result as a dictionary
        scan_data = {"age_restricted": scan_result}

        # Convert to a json object which will be returned
        scan_json = json.dumps(scan_data)

        # Return boolean result as json object
        return scan_json

    except:
        # If fails, return error message
        return "Unable to scan webpage url provided"


# GET request for verifying user's age via a captured photo
@app.route("/confirm_age")
def confirm_age():
    """Endpoint for requesting to capture photo of user and estimate their age
       Returns age of the user predicted by age verification software"""

    # Call functionality which takes photo of user and calculates their age via facial recognition
    user_age = face_age_capture.get_user_age()

    # Save age as dictionary
    age_data = {"age": user_age}

    # Return the age as json
    return json.dumps(age_data)


# GET request for static html page explaining redirect
@app.route("/redirect_page")
def redirect_page():
    # Return html page, no templating actually used here
    return render_template('redirect_page.html')

if __name__ == "__main__":
    # Run app on localhost:8080 for testing purposes
    app.run(debug=True, host="localhost", port=8081)

