# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

import unittest
from pathlib import Path
from system_test import SystemTest
from command_create_project import CommandCreateProject


class TestCommandCreateProject(unittest.TestCase):

    def assert_project_directory_does_not_exist(self):
        self.assertFalse(self.project_name.is_dir())

    def assert_has_a_project_directory_structure(self):
        for directory_name in CommandCreateProject.project_directories:
            self.assertTrue((self.project_name/directory_name).is_dir())

    def assert_project_directory_contains(self, file_name):
        self.assertTrue((self.project_name/file_name).is_file())

    def setUp(self):
        self.project_name = Path(SystemTest.get_testing_directory())/"arbitrary_project_name"
        self.command = CommandCreateProject(self.project_name)

    def test_execution(self):
        self.assert_project_directory_does_not_exist()
        self.command.execute()
        self.assert_has_a_project_directory_structure()
        self.assert_project_directory_contains("LICENSE.TXT")
        self.assert_project_directory_contains("README.md")
