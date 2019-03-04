#!/usr/bin/env python

# Imports for http requests and regular expressions libraries
import requests
import re as regex

def contains_keyword(regex_string, webpage_url):
    """This class docstring shows how to use sphinx and rst syntax

        :param regex_string: Regular Expression string to run over the webpage url's content
        :param webpage_url: URL for the webpage to scan, must include http:// or https:// prefix"""

    # GET request on the provided webpage url
    request = requests.get(webpage_url)

    # Save just the response body
    request_html = request.content

    # Execute the regex on the webpage response body
    regex_result = regex.search(regex_string, request_html)

    # If the regex is in the content, return true
    if(regex_result):
        return True

    # Return false if regex didn't find keywords
    return False
