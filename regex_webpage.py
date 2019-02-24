#!/usr/bin/env python

import requests
import re as regex

def run_regex_on_webpage(regex_string, webpage_url):

    request = requests.get(webpage_url)

    request_html = request.content

    regex_result = regex.search(regex_string, request_html)

    if(regex_result):
        print("contains blocked word")

run_regex_on_webpage("coventry", "https://en.wikipedia.org/wiki/Coventry")