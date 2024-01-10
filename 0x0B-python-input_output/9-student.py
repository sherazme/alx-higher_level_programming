#!/usr/bin/python3
""" Student Class """


class Student:
    """ Define class student """
    def __init__(self, first_name, last_name, age):
        """ Initialize new instance of student class

        Args:
          fisr_name: fisrt name
          last_name: last name
          age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return dictionary representation of Student instance """
        return (self.__dict__)
