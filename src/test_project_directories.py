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

from project_directories import ProjectDirectories
from unit_test import UnitTest


class TestProjectDirectories(UnitTest):

    def test_root_variable(self):
        self.assert_equals(self.raw_path, self.path.root)

    def test_root_concatenation_with_string(self):
        self.assert_equals(self.raw_path/"arbitrary_string", self.path/"arbitrary_string")

    def test_root_concatenation_with_path(self):
        self.assert_equals(self.raw_path/Path("arbitrary"), self.path/Path("arbitrary"))

    def test_converstion_to_string(self):
        self.assert_equals(str(self.raw_path), str(self.path))

    def test_path_to_class_header_template(self):
        self.assert_equals(self.raw_path/".templates/class_header.template", self.path.to_class_header_template)

    def test_path_to_class_source_template(self):
        self.assert_equals(self.raw_path/".templates/class_source.template", self.path.to_class_source_template)

    def test_path_to_class_tests_template(self):
        self.assert_equals(self.raw_path/".templates/class_tests.template", self.path.to_class_tests_template)

    def test_path_to_license_header_template(self):
        self.assert_equals(self.raw_path/".templates/license_header.template", self.path.to_license_header_template)

    def test_path_to_include_directory(self):
        self.assert_equals(self.raw_path/"include"/self.raw_path.name, self.path.to_include_directory)

    def test_path_to_source_directory(self):
        self.assert_equals(self.raw_path/"src", self.path.to_source_directory)

    def test_path_to_templates_directory(self):
        self.assert_equals(self.raw_path/".templates", self.path.to_templates_directory)

    def test_list_top_down(self):
        expected = [
            self.raw_path,
            self.path.to_templates_directory, self.path.to_source_directory, self.raw_path/"include",
            self.path.to_include_directory
        ]
        self.assert_equals(expected, self.path.list_top_down())

    def setUp(self):
        self.raw_path = Path("arbitrary_path")
        self.path = ProjectDirectories(self.raw_path)
