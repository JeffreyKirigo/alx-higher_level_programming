#!/usr/bin/python3
"""Fetches a url"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
