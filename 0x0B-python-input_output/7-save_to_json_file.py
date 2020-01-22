#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
