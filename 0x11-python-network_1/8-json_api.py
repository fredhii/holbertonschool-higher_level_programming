#!/usr/bin/python3
""" 
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}
    try:
        req = requests.post(url, data=data).json()
        if 'id' in req and 'name' in req:
            print("[{}] {}".format(req['id'], req['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
