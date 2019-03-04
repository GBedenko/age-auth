from flask import Flask, request
import scan_webpage_keywords

app = Flask(__name__)

@app.route("/scan")
def scan():

    try:

        regex = request.args.get('regex')
        print(regex)

        url = request.args.get('url')
        print(url)

        scan_result = scan_webpage_keywords.contains_keyword(regex, url)
        
        return str(scan_result)

    except:

        return "Incorrect query parameters"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    