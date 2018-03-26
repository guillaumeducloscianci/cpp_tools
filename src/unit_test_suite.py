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
import test_command_append_file_to_file
import test_command_copy_file
import test_command_create_cmakelists
import test_command_create_directory
import test_command_create_file
import test_command_create_file_with_header
import test_command_create_git_repository
import test_command_create_license_header_template
import test_command_create_project
import test_command_search_and_replace_in_file
import test_command_parser

import test_file_template
import test_top_level_cmakelists

from command_parser import CommandParser

def create_unit_test_suite():
    modules = [
        test_command_append_file_to_file,
        test_command_copy_file,
        test_command_create_directory,
        test_command_create_file,
        test_command_search_and_replace_in_file,
        
        test_command_create_cmakelists,
        test_command_create_file_with_header,
        test_command_create_git_repository,
        test_command_create_license_header_template,
        test_command_create_project,

        test_command_parser,
        test_file_template,
        test_top_level_cmakelists,
    ]
    return TestSuite.create_from_modules(modules)

if __name__ == '__main__':
    test_suite = create_unit_test_suite()
    test_suite.run()
