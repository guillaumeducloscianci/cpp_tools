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


class TestSuite:

    @staticmethod
    def create_from_modules(modules):
        test_suite = TestSuite()
        test_suite.add_from_modules(modules)
        return test_suite

    def __init__(self):
        self.test_suite = unittest.TestSuite()

    def add_from_modules(self, modules):
        for module in modules:
            self.add_from_module(module)

    def add_from_module(self, module):
        self.test_suite.addTests(unittest.TestLoader().loadTestsFromModule(module))

    def run(self, verbosity_=3):
        unittest.TextTestRunner(verbosity=verbosity_).run(self.test_suite)
