#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request as urllib

url = "https://alx-intranet.hbtn.io/status"

with urllib.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
