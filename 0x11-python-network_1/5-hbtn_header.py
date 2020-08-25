#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    res = requests.post(argv[1], data=payload)
    print(res.text)
