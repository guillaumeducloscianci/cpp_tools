# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

from system_test import SystemTest
from command_create_project import CommandCreateProject


class TestCommandCreateProject(SystemTest):

    def test_execution(self):
        self.assert_directory_does_not_exist(self.project_path)
        self.command.execute()
        self.assert_has_a_project_directory_structure()
        self.assert_project_directory_contains([
            "CMakeLists.txt", "src/CMakeLists.txt", "LICENSE.TXT", "README.md", ".gitignore", 
            ".templates/license_header.template"
        ])

    def setUp(self):
        self.author = "arbitrary_author"
        self.project_path = Path(SystemTest.get_testing_directory())/"arbitrary_project_name"
        self.command = CommandCreateProject(self.project_path, self.author)

    def assert_has_a_project_directory_structure(self):
        for directory_name in CommandCreateProject.project_directories:
            self.assert_directory_exists(self.project_path/directory_name)

    def assert_project_directory_contains(self, file_names):
        for file_name in file_names:
            self.assert_file_exists(self.project_path/file_name)
