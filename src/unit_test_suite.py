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

from test_suite import TestSuite
import test_command_copy_file
import test_command_create_directory
import test_command_create_project
import test_command_parser

if __name__ == '__main__':
    modules = [test_command_copy_file, test_command_create_project, test_command_create_directory, test_command_parser]
    test_suite = TestSuite.create_from_modules(modules)
    test_suite.run()
