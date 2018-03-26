# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from file import File
from system_test import SystemTest


class TestFile(SystemTest):

    def test_read_and_write(self):
        File.write(self.path, self.content)
        self.assert_equals(self.content, File.read(self.path))

    def test_copy(self):
        copy_path = self.path.parent/"arbitrary_file.copy"
        File.write(self.path, self.content)
        self.assert_file_does_not_exist(copy_path)
        File.copy(self.path, copy_path)
        self.assert_file_exists(copy_path)

    def setUp(self):
        self.path = SystemTest.get_testing_directory()/"arbitrary_file"
        self.content = "Arbitrary content."
