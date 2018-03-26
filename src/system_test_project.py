# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from project import Project, Parameters
from system_test import SystemTest


class TestProject(SystemTest):

    def test_create_directory_structure(self):
        self.assert_directory_does_not_exist(self.path)
        Project(self.parameters).create_directory_structure()
        self.assert_has_a_project_directory_structure()

    def setUp(self):
        self.path = SystemTest.get_testing_directory()/"arbitrary_project"
        self.author = "arbitrary_author"
        self.parameters = Parameters(self.path, self.author)

    def assert_has_a_project_directory_structure(self):
        for directory in Project.directories:
            self.assert_directory_exists(self.path/directory)

class TestProjectWithDirectoryStructure(SystemTest):            

    def test_create_license_file(self):
        self.project.create_license_file()
        self.assert_project_directory_contains(["LICENSE.TXT"])

    @classmethod
    def setUpClass(cls):
        cls.path = SystemTest.get_testing_directory()/"arbitrary_project_with_directory_structure"
        cls.author = "arbitrary_author"
        cls.project = Project(Parameters(cls.path, cls.author))
        cls.project.create_directory_structure()

    def assert_project_directory_contains(self, file_names):
        for file_name in file_names:
            self.assert_file_exists(self.path/file_name)