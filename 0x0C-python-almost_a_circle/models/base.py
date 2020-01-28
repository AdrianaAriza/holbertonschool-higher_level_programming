#!/usr/bin/python3
"""
this module have the base class
"""

import json
import os
import csv


class Base:
    """
    base
    """

    __nb_objects = 1

    def __init__(self, id=None):
        """
        init
        """

        if id is None:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file
        """

        file_n = "{}.json".format(cls.__name__)
        li = []
        if list_objs not None:
            for i in list_objs:
                li.append(i.__dict__)
        with open(file_n, 'w') as file:
            json.dump(li, file)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        cretate
        """

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        load
        """

        file_n = "{}.json".format(cls.__name__)
        if not os.path.exists(file_n):
            return []
        with open(file_n, 'r') as file:
            json_string = file.read()
        new_list = cls.from_json_string(json_string)
        final_list = []
        for obj in new_list:
            final_list.append(cls.create(**obj))
        return final_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save
        """

        file_n = "{}.csv".format(cls.__name__)
        with open(file_n, 'w') as file:
            for obj in list_objs:
                for k, v in obj.__dict__.items():
                    file.write("{}:{},".format(k, v))

    @classmethod
    def load_from_file_csv(cls):
        """
        load
        """

        file_n = "{}.csv".format(cls.__name__)
        with open(file_n, 'w') as file:
            list_csv = csv.reader(file, delimiter=",")
