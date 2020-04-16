#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys

    from requests.auth import HTTPBasicAuth
    req = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    try:
        r = req.json()
        if r:
            print(r["id"])
    except:
        print("None")
