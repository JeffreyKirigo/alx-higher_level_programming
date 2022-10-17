#!/usr/bin/python3
"""Define a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Init a new student
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): Age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
