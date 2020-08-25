#!/usr/bin/python3
"""
Takes in an URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    url = request.Request(argv[1])
    with request.urlopen(url) as res:
        print(res.headers.get('X-Request-Id'))
