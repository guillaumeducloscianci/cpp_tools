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
from file import File
from interface_creator import InterfaceCreator
from implementation_creator import ImplementationCreator
from project import Project, ProjectParameters
from project_paths import ProjectPaths
from system_test import SystemTest


class TestImplementationCreatorTools(SystemTest):
    
    @classmethod
    def create_interface(cls,interface_path):
        InterfaceCreator(interface_path.stem, cls.path).create()
        interface_content = File.read(interface_path).replace("//", "")
        File.overwrite(interface_path, interface_content)

    @classmethod
    def setup_base(cls):
        cls.class_name = "arbitrary_class"
        cls.path = ProjectPaths(SystemTest.get_testing_directory()/"arbitrary_project_name")
        Project(ProjectParameters(cls.path.root, "arbitrary_author")).create()
        cls.interface_path = cls.path.to_include_directory/(cls.class_name+"_interface.h")
        cls.create_interface(cls.interface_path)
        cls.header_path = cls.path.to_include_directory/(cls.class_name+".h")
        cls.source_path = cls.path.to_source_directory/(cls.class_name+".cpp")
        cls.tests_path = cls.path.to_source_directory/(cls.class_name+"_tests.cpp")

    @classmethod
    def tear_down_base(cls):
        Directory.remove(cls.path.root)

    def assert_implementation_does_not_exist(self):
        self.assert_file_does_not_exist(self.header_path)
        self.assert_file_does_not_exist(self.source_path)
        self.assert_file_does_not_exist(self.tests_path)

    def assert_implementation_exists(self):
        self.assert_file_exists(self.header_path)
        self.assert_file_exists(self.source_path)
        self.assert_file_exists(self.tests_path)


class TestImplementationCreator(TestImplementationCreatorTools):

    def test_create(self):
        self.assert_implementation_does_not_exist()
        ImplementationCreator(self.class_name, self.path, self.interface_path.name).create()
        self.assert_implementation_exists()

    @classmethod
    def setUpClass(cls):
        cls.setup_base()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()
