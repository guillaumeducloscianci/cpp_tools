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

def add_tests_from_modules(module_names):
	for name in module_names:
		add_tests_from_module(name)

def add_tests_from_module(module_name):
	unittest.TestSuite().addTests(unittest.TestLoader().loadTestsFromModule(module_name))

def run_tests(verbosity_=3):
	unittest.TextTestRunner(verbosity=verbosity_).run(unittest.TestSuite())

if __name__ == '__main__':
	add_tests_from_modules([])
	run_tests()
