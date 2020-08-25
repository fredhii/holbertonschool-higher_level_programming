#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
if __name__ == "__main__":
    import requests
    res = requests.get('https://intranet.hbtn.io/status')
    text = res.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
