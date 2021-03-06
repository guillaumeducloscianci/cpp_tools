# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_creator import ClassCreator
from directory import Directory
from project import Project, ProjectParameters
from project_paths import ProjectPaths
from system_test import SystemTest


class TestClassCreatorTools(SystemTest):
    
    @classmethod
    def setup_base(cls):
        cls.class_name = "arbitrary_class"
        cls.path = ProjectPaths(SystemTest.get_testing_directory()/"arbitrary_project_name")
        Project(ProjectParameters(cls.path.root, "arbitrary_author")).create()
        cls.classCreator = ClassCreator(cls.class_name, cls.path)

    @classmethod
    def tear_down_base(cls):
        Directory.remove(cls.path.root)

    def assert_header_is_properly_formatted(self, header_path):
        self.assert_file_exists(header_path)
        self.assert_file_has_license_header(header_path)
        should_contain = [self.class_name, self.class_name.upper()+"_"]
        should_not_contain = ["class_name_", "CLASS_NAME_"]
        for content in should_contain:
            self.assert_file_contains(header_path, content)
        for content in should_not_contain:
            self.assert_file_does_not_contain(header_path, content)

    def assert_source_is_properly_formatted(self, source_path):
        self.assert_file_exists(source_path)
        self.assert_file_has_license_header(source_path)
        self.assert_file_contains(source_path, self.class_name)
        self.assert_file_does_not_contain(source_path, "class_name_")

    def assert_tests_is_properly_formatted(self, tests_path):
        self.assert_source_is_properly_formatted(tests_path)

    def assert_class_does_not_exist(self):
        self.assert_file_does_not_exist(self.header_path)
        self.assert_file_does_not_exist(self.source_path)
        self.assert_file_does_not_exist(self.tests_path)
        for file_name in self.file_names: self.assert_file_does_not_contain(self.src_cmakelist_path, file_name)

    def assert_class_exists(self):
        self.assert_header_is_properly_formatted(self.header_path)
        self.assert_source_is_properly_formatted(self.source_path)
        self.assert_tests_is_properly_formatted(self.tests_path)
        for file_name in self.file_names: self.assert_file_contains(self.src_cmakelist_path, file_name)


class TestClassCreator(TestClassCreatorTools):

    def test_variables(self):
        self.assert_equals(self.classCreator.class_name, self.class_name)
        self.assert_equals(self.classCreator.path, self.path)

    def test_create_license_header(self):
        license_header = self.classCreator.create_license_header().instantiate_for_cpp()
        self.assert_string_does_not_contain(license_header, "#")
        for delimiter in ["/* ", " */"]:
            self.assert_string_contains(license_header, delimiter)

    def test_create_class_header(self):
        header_path = self.path.to_include_directory/(self.class_name+".h")
        self.assert_file_does_not_exist(header_path)
        self.classCreator.create_header_file()
        self.assert_header_is_properly_formatted(header_path)

    def test_create_class_source(self):
        source_path = self.path.to_source_directory/(self.class_name+".cpp")
        self.assert_file_does_not_exist(source_path)
        self.classCreator.create_source_file()
        self.assert_source_is_properly_formatted(source_path)

    def test_create_class_tests(self):
        tests_path = self.path.to_source_directory/(self.class_name+"_tests.cpp")
        self.assert_file_does_not_exist(tests_path)
        self.classCreator.create_tests_file()
        self.assert_tests_is_properly_formatted(tests_path)

    def test_add_to_cmakelists(self):
        src_cmakelist_path = self.path.to_source_directory/"CMakeLists.txt"
        file_names = [ self.class_name+".cpp", self.class_name+"_tests.cpp" ]
        for file_name in file_names: self.assert_file_does_not_contain(src_cmakelist_path, file_name)
        self.classCreator.add_to_cmakelists()
        for file_name in file_names: self.assert_file_contains(src_cmakelist_path, file_name)

    @classmethod
    def setUpClass(cls):
        cls.setup_base()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()


class TestClassCreatorCreate(TestClassCreatorTools):

    def test_create(self):
        self.assert_class_does_not_exist()
        self.classCreator.create()
        self.assert_class_exists()

    @classmethod
    def setUpClass(cls):
        cls.setup_base()
        cls.header_path = cls.path.to_include_directory/(cls.class_name+".h")
        cls.source_path = cls.path.to_source_directory/(cls.class_name+".cpp")
        cls.tests_path = cls.path.to_source_directory/(cls.class_name+"_tests.cpp")
        cls.src_cmakelist_path = cls.path.to_source_directory/"CMakeLists.txt"
        cls.file_names = [ cls.class_name+".cpp", cls.class_name+"_tests.cpp" ]

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()
