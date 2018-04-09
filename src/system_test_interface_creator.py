# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from directory import Directory
from interface_creator import InterfaceCreator
from project import Project, ProjectParameters
from project_paths import ProjectPaths
from system_test import SystemTest


class TestClassCreator(SystemTest):

    def test_create(self):
        self.assert_interface_does_not_exist()
        InterfaceCreator(self.class_name, self.path).create()
        self.assert_interface_exists()

    @classmethod
    def setUpClass(cls):
        cls.class_name = "arbitrary_class"
        cls.path = ProjectPaths(SystemTest.get_testing_directory()/"arbitrary_project_name")
        Project(ProjectParameters(cls.path.root, "arbitrary_author")).create()
        cls.header_path = cls.path.to_include_directory/(cls.class_name+".h")

    @classmethod
    def tearDownClass(cls):
        Directory.remove(cls.path.root)

    def assert_interface_does_not_exist(self):
        self.assert_file_does_not_exist(self.header_path)

    def assert_interface_exists(self):
        self.assert_file_exists(self.header_path)
