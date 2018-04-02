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
import test_class_header_template
import test_class_source_template
import test_class_tests_template
import test_command_create_project
import test_command_parser
import test_file_template
import test_top_level_cmakelists

from command_parser import CommandParser

def create_unit_test_suite():
    # Order is important. It represents ascending dependencies between modules.
    modules = [ test_file_template ]
    modules += [
        test_class_header_template,
        test_class_source_template,
        test_class_tests_template,
        test_top_level_cmakelists
    ]
    modules += [ test_command_create_project ]
    modules += [ test_command_parser ]
    return TestSuite.create_from_modules(modules)

if __name__ == '__main__':
    test_suite = create_unit_test_suite()
    test_suite.run()
