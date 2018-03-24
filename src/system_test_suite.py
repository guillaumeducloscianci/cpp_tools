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

from system_test import SystemTest
from test_suite import TestSuite
import system_test_command_copy_file
import system_test_command_create_cmakelists
import system_test_command_create_directory
import system_test_command_create_file
import system_test_command_create_git_repository
import system_test_command_create_license_header_template
import system_test_command_create_project
import system_test_command_search_and_replace_in_file

from pathlib import Path
from command_create_project import CommandCreateProject

def create_system_test_suite():
    SystemTest.reset("testing")
    modules = [
        system_test_command_copy_file, system_test_command_create_cmakelists, system_test_command_create_directory,
        system_test_command_create_file, system_test_command_create_git_repository,
        system_test_command_create_license_header_template, system_test_command_create_project,
        system_test_command_search_and_replace_in_file
    ]
    return TestSuite.create_from_modules(modules)

if __name__ == '__main__':
    test_suite = create_system_test_suite()
    test_suite.run()
