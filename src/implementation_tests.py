# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_tests import ClassTests
from interface_header import InterfaceHeader


class ImplementationTests():
    
    def __init__(self, template, license_header, header):
        self.bare_tests = ClassTests(template, license_header)
        self.header = header

    def instantiate_with(self, class_name):
        return self.add_content_to(self.bare_tests.instantiate_with(class_name), class_name)

    def add_content_to(self, bare_tests, class_name):
        for method in InterfaceHeader.extract_methods(self.header):
            bare_tests += self.create_test_case(method, class_name)
        return bare_tests

    @staticmethod
    def create_test_case(method, class_name):
        name = method.split()[1].split('(')[0]
        return "TEST_F(test_" + class_name + ", " + name + ") {\n\n}\n"
