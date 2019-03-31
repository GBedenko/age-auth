// Main script of the Chrome extension, is run everytime the user navigates to a new webpage

// Regex of keywords to scan for
regex = "vodka|whiskey|whisky|lager|cider|skyrim"

// Obtain current url but remove any suffix string start with a '&'
let current_url = window.location.toString().split('&', 1)

// Request local API to confirm if this webpage contains age restricted keywords
let scan_request = 'http://localhost:8080/scan?url=' + current_url + '&regex=' + regex

// Parse the result JSON from the request's response
// let scan_response = httpGet(scan_request)

fetch(scan_request)
    .then(response => response.text())
    .then(text => {
        return text
    })
    .then(isAgeRestricted => {
        
        // If webpage is age restricted
        if (isAgeRestricted == "True") {

            // Ask user if they're happy to use age verification
            let confirmation = confirm('This page is age-restricted. Use facial age verification?')
            
            // If user accepts facial recognition age verification
            if(confirmation) {
                
                // Send a request to obtain age of the user
                fetch('http://localhost:8080/confirm_age')
                    .then(response => {
                        return(response.text())
                    })
                    .then(age => {
                        
                        if(age >= 18) {
                            // If 18 or over, confirm they passed age verification
                            alert('Facial Recognition determines you are ' + age + ' years old. Please continue browsing.')
                            
                        } else {
                            // If under 18, redirect user to an information page
                            window.location = "http://localhost:8080/redirect_page";
                        }
                    })
                
            } else {

                // If user refuses age verification, redirect user to an information page
                window.location = "http://localhost:8080/redirect_page";
            }
        }
    })

