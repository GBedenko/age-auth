#!/usr/bin/env python

from flask import Flask, request
import scan_webpage_keywords

# Create a Flask app to run as a web server to host local API
app = Flask(__name__)

# GET request for retrieving scan result
@app.route("/scan")
def scan():

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
        
        # Return boolean result as a string
        return str(scan_result)

    except:
        # If fails, return error message
        return "Unable to scan webpage url provided"

if __name__ == "__main__":
    # Run app on localhost:8080 for testing purposes
    app.run(debug=True, host="0.0.0.0", port=8080)
