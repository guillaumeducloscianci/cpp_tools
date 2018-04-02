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

from command_create_project import CommandCreateProject, ProjectParameters
from directory import Directory
from project import Project
from system_test import SystemTest
from system_test_project import TestProjectTools


class TestCommandCreateProject(TestProjectTools):

    def test_execution(self):
        self.assert_directory_does_not_exist(self.path)
        self.command.execute()
        self.assert_has_a_project_directory_structure()
        for file_name in self.expected_files:
            self.assert_project_directory_contains(file_name)

    def setUp(self):
        self.author = "arbitrary_author"
        self.path = Path(SystemTest.get_testing_directory())/"arbitrary_project"
        parameters = ProjectParameters(self.path, self.author)
        self.project = Project(parameters)
        self.command = CommandCreateProject(parameters)
        self.expected_files = [
            "CMakeLists.txt", "src/CMakeLists.txt", "LICENSE.TXT", "README.md", ".gitignore", 
            ".templates/license_header.template"
        ]

    def tearDown(self):
        Directory.remove(self.path)
