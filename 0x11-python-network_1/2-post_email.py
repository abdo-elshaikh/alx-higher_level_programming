#!/usr/bin/python3
""" Python script that takes in a URL and Email, sends a POST request"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
