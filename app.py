#!/usr/bin/env python

# Import Flask to host server
from flask import Flask, request, render_template

# Import modules for functionality
import scan_webpage_keywords
import face_age_capture
import json
import time

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

        # Convert to a json object which will be returned
        scan_json = json.dumps({'age_restricted': scan_result})

        # Return boolean result as json object
        return str(scan_result)

    except:
        # If fails, return error message
        return "Unable to scan webpage url provided"


# GET request for verifying user's age via a captured photo
@app.route("/confirm_age")
def confirm_age():
    """Endpoint for requesting to capture photo of user and estimate their age
       Returns age of the user predicted by age verification software"""

    # Timestamp before calculating age of user
    start_time = time.time()

    # Call functionality which takes photo of user and calculates their age via facial recognition
    user_age = face_age_capture.get_user_age()

    # Save age as dictionary
    age_data = {"age": user_age}

    # Timestamp after age of user determined
    end_time = time.time()

    # Time duration to determine the user's age
    time_taken = end_time - start_time

    # Append time taken to log file
    with open("./experiments/time_taken.txt", "a") as timings:
        timings.write(str(time_taken) + "\n")

    # Return the age as json
    return str(user_age)


# GET request for static html page explaining redirect
@app.route("/redirect_page")
def redirect_page():
    """Endpoint for static html page explaining why user was redirected"""

    # Return html page, no templating actually used here
    return render_template('redirect_page.html')

if __name__ == "__main__":
    # Run app on localhost:8080 for testing purposes
    app.run(debug=True, host="localhost", port=8080)

