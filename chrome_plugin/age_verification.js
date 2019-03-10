// Regex of keywords to scan for
regex = "vodka|whiskey|whisky|lager|cider|skyrim"

// Obtain current url but remove any suffix string start with a '&'
let current_url = window.location.toString().split('&', 1)

// Request local API to confirm if this webpage contains age restricted keywords
let scan_request = 'http://localhost:8081/scan?url=' + current_url + '&regex=' + regex

// Parse the result JSON from the request's response
let scan_json_response = JSON.parse(httpGet(scan_request))

// Boolean result of if the page is age-restricted or not
let isAgeRestricted = scan_json_response.age_restricted

// If webpage is age restricted
if (isAgeRestricted) {

    // Ask user if they're happy to use age verification
    let confirmation = confirm('This page is age-restricted. Use facial age verification?')
    
    // If user accepts facial recognition age verification
    if(confirmation) {
        
        // Send a request to obtain age of the user
        let age_request = 'http://localhost:8081/confirm_age'
    
        // Parse the result of the age request
        let age_json_response = JSON.parse(httpGet(age_request))

        if(age_json_response.age >= 18) {
            // If 18 or over, confirm they passed age verification
            alert('Facial Recognition determines you are ' + age_json_response.age + ' years old. Please continue browsing.')
        } else {
            // If under 18, redirect user to an information page
            window.location = "http://localhost:8081/redirect_page";
        }
        
    } else {

        // If user refuses age verification, redirect user to an information page
        window.location = "http://localhost:8081/redirect_page";
    }
}

// Function to make a GET request for the provided url and returns response object
function httpGet(url) {
    var xmlHttp = new XMLHttpRequest()
    xmlHttp.open( "GET", url, false )
    xmlHttp.send( null )
    return xmlHttp.responseText
}