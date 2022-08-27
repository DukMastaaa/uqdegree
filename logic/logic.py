#!uqdegree-app/venv/scripts python
# -*- coding: utf-8 -*-

__author__ = "Armando Liebenberg, Adriel Efendy"
__email__ = "armandoliebeneberg@gmail.com"

"""
A bunch of OOP turning our web scraped data into usable input
defines Course, Course module, program module
"""

from typing import Union


"""
Contains course code, number of units, course name, as well as what 
semester the course is offered in
"""
class Course():
    def __init__(self, courseCode: str, units: int, courseName: str, courseSite: str):
        self.courseCode = courseCode
        self.courseName = courseName
        self.units = units
        self.courseSite = courseSite

        self.semester = self.find_semester()

        self.active = False

    def find_semester(self):
        # Call beautifulsoup on course site, extract semester date
        pass

    def get_courseCode(self):
        return self.courseCode

    def get_courseName(self):
        return self.courseName

    def get_units(self):
        return self.units

    def get_semester(self):
        return self.semester

    def is_active(self) -> bool:
        return self.active


class JoinedCourse:
    def __init__(self, courses: list[Course] = None):
        if courses is None:
            self.courses = []
        else:
            self.courses = courses
        
    def add_course(self, course: Course) -> None:
        self.courses.append(course)
    
    def has_multiple(self) -> bool:
        return len(self.courses) > 1

    def get_active_units(self) -> int:
        return sum(int(c.is_active()) for c in self.courses)
    
    def is_valid(self) -> bool:
        return self.get_active_units() <= 1


class And:
    def __init__(self, min: int, max: int, module_list):
        self.min = min
        self.max = max
        self.ll = module_list

class Or:
    def __init__(self, module_list):
        self.ll = module_list

class Leaf:
    def __init__(self, min: int, max: int, joined_course_list: list[JoinedCourse]):
        self.min = min
        self.max = max
        self.ll = joined_course_list


class Module:
    def __init__(self, name: str, rec: Union[And, Or, Leaf]):
        self.name = name
        self.rec = rec
    
    def get_active_units(self) -> int:
        # this works due to dynamic typing
        # will raise AttributeError if something went wrong
        return sum(thing.get_active_units() for thing in self.rec.ll)

    def is_valid(self) -> bool:
        if type(self.rec) == Leaf:
            return all(jc.is_valid() for jc in self.rec.ll) \
                and self.min <= sum(jc.get_active_units() for jc in self.rec.ll) <= self.max
        elif type(self.rec) == And:
            return all(m.is_valid() for m in self.rec.ll) \
                and self.min <= self.rec.get_active_units() <= self.max
        elif type(self.rec) == Or:
            return any(m.is_valid() for m in self.rec.ll)


# """
# Container for courses and other course modules. Holds information abo-
# ut number of units needed for module, as well as options for sub modu-
# les.
# """
# class CourseModule():
#     def __init__(self, name, upper, lower):
#         self.name = name
#         self.unit_upper_bound = upper
#         self.unit_lower_bound = lower
#         self.submodules = []

#     # Add a submodule to our list of modules
#     def add_submodule(self, module):
#         self.submodule.append(module)
#         # self.unit_checking()

#     # Checks if our submodules don't break module unit limits
#     def unit_checking(self):
#         module_unit_sum = 0

#         module: CourseModule
#         for module in self.submodules:
#             module_unit_sum += module.get_units_lower_bound()

#         if module_unit_sum < self.units:
#             return
#         else:
#             raise Exception("Sum of minimum submodule units larger than module units")

#     # Returns the maximum number of units we can take in a module
#     def get_units_upper_bound(self):
#         return self.unit_upper_bound

#     # Returns the minumum number of units we must take in a module
#     def get_units_lower_bound(self):
#         return self.unit_lower_bound