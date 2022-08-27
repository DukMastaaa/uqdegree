#!uqdegree-app/venv/scripts python
# -*- coding: utf-8 -*-

__author__ = "Armando Liebenberg, Adriel Efendy"
__email__ = "armandoliebeneberg@gmail.com"

"""
A bunch of OOP turning our web scraped data into usable input
defines Course, Course module, program module
"""

"""
Container for course modules, holds (and inforces?) information about
number of units needed from each module. Holds all additional requir-
ments. I.e (at most 24 units of lvl 1 courses) 
"""
class program():
    def __init__(self):
        self.modules = {}

    def add_module(self, module:course_module, units:tuple):
        self.modules.update({module:units})
        

"""
Container for courses and other course modules. Holds information abo-
ut number of units needed for module, as well as options for sub modu-
les.
"""
class course_module():
    def __init__(self, name, units):
        self.name = name
        self.units = units
        self.submodules = []

    # Add a submodule to our list of modules
    def add_submodule(self, name, units):
        self.submodule.append(course_module(name, units))
        self.unit_checking()

    # Checks if our submodules don't break module unit limits
    def unit_checking(self):
        module_unit_sum = 0

        module:course_module
        for module in self.submodules:
            module_unit_sum += module.get_units_lower_bound()

        if module_unit_sum < self.units:
            return
        else:
            raise Exception("Sum of minimum submodule units larger than module units")

    # Returns the maximum number of units we can take in a module
    def get_units_upper_bound(self):
        return self.units[1]

    # Returns the minumum number of units we must take in a module
    def get_units_lower_bound(self):
        return self.units[0]



"""
Contains course code, number of units, course name, as well as what 
semester the course is offered in
"""
class course():
    def __init__(self, courseCode, units, courseName, courseSite):
        self.courseCode = courseCode
        self.courseName = courseName
        self.units = units
        self.courseSite = courseSite

        self.semester = self.find_semester()
        

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

    

