#!/usr/bin/env python

import requests
import re as regex

def contains_keyword(regex_string, webpage_url):

    request = requests.get(webpage_url)

    request_html = request.content

    regex_result = regex.search(regex_string, request_html)

    if(regex_result):
        return True

    return False
