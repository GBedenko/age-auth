let current_url = window.location.toString().split('&', 1)

let scan_request = 'http://localhost:8081/scan?url=' + current_url + '&regex=vodka'

let json_response = JSON.parse(httpGet(scan_request))

let isAgeRestricted = json_response.age_restricted

if (isAgeRestricted) {
    chrome.runtime.sendMessage('This page is age-restricted')
} else { 
    chrome.runtime.sendMessage('This page is not age-restricted')
}


function httpGet(url)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}