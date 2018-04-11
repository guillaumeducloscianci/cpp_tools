#!/usr/bin/env python3

# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from system_test import SystemTest
from test_suite import TestSuite
import system_test_class_creator
import system_test_class_header_template
import system_test_class_source_template
import system_test_class_tests_template
import system_test_command_create_class
import system_test_command_create_interface
import system_test_command_create_implementation
import system_test_command_create_project
import system_test_directory
import system_test_file
import system_test_implementation_creator
import system_test_interface_creator
import system_test_license_header_template
import system_test_project
import system_test_top_level_cmakelists

def create_system_test_suite():
    # Order is important. It represents ascending dependencies between modules.
    modules = [
        system_test_directory,
        system_test_file
    ]
    modules += [
        system_test_class_header_template,
        system_test_class_source_template,
        system_test_class_tests_template,
        system_test_license_header_template,
        system_test_top_level_cmakelists
    ]
    modules += [ system_test_project ]
    modules += [
        system_test_implementation_creator,
        system_test_interface_creator,
        system_test_class_creator,
        system_test_command_create_project
    ]
    modules += [
        system_test_command_create_class,
        system_test_command_create_implementation,
        system_test_command_create_interface
    ]
    SystemTest.reset("testing")
    return TestSuite.create_from_modules(modules)

if __name__ == '__main__':
    test_suite = create_system_test_suite()
    test_suite.run()
