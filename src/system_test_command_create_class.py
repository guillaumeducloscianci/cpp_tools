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

from command_create_class import CommandCreateClass
from directory import Directory
from system_test import SystemTest
from system_test_class_creator import TestClassCreatorTools


class TestCommandCreateClass(TestClassCreatorTools):

    def test_execution(self):
        command = CommandCreateClass(self.class_name, self.path)
        self.assert_class_does_not_exist()
        command.execute()
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
