#!/usr/bin/env python3

# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.


import unittest # See https://docs.python.org/3.5/library/unittest.html for details
from system_test_tools import clean_testing_directory
import system_test_command_create_project

_test_suite = unittest.TestSuite()

def add_tests_from_modules(modules):
    for module in modules:
        add_tests_from_module(module)

def add_tests_from_module(module):
    _test_suite.addTests(unittest.TestLoader().loadTestsFromModule(module))

def run_tests(verbosity_=3):
    unittest.TextTestRunner(verbosity=verbosity_).run(_test_suite)


if __name__ == '__main__':
    clean_testing_directory()
    modules = [system_test_command_create_project]
    add_tests_from_modules(modules)
    run_tests()
