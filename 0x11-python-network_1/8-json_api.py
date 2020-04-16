#!/usr/bin/python3
if __name__ == "__main__":
    import requests
    import sys

    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]
    payload = {'q': q}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = req.json()
        if res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
