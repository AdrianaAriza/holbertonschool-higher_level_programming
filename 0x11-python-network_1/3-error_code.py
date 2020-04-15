#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    import sys
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
