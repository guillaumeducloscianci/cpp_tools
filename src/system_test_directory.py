# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
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
from system_test import SystemTest


class TestDirectory(SystemTest):

    def test_create(self):
        self.assert_directory_does_not_exist(self.path)
        Directory.create(self.path)
        self.assert_directory_exists(self.path)

    def setUp(self):
        self.path = SystemTest.get_testing_directory()/"arbitrary_directory"

    def tearDown(self):
        self.path.rmdir()


class TestDirectoryActingOnExistingDirectoy(SystemTest):

    def test_remove_empty_directory(self):
        Directory.remove(self.path)
        self.assert_directory_does_not_exist(self.path)

    def test_remove_directory_not_empty(self):
        File.write(self.path/"file_in_directory", "arbitrary content")
        Directory.remove(self.path)
        self.assert_directory_does_not_exist(self.path)

    def test_remove_nested_directory(self):
        Directory.create(self.path/"nested")
        Directory.remove(self.path)
        self.assert_directory_does_not_exist(self.path)

    def setUp(self):
        self.path = SystemTest.get_testing_directory()/"arbitrary_directory"
        Directory.create(self.path)
