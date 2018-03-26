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

from command_append_file_to_file import CommandAppendFileToFile
from system_test import SystemTest
from system_tools import cpp_tools_resources_directory


class TestCommandAppendFileToFile(SystemTest):

    def test_execution(self):
        self.assert_file_does_not_contain(self.target_file, self.file_to_append_content)
        CommandAppendFileToFile(self.file_to_append, self.target_file).execute()
        self.assert_file_contains(self.target_file, self.file_to_append_content)

    @classmethod
    def setUpClass(cls):
        cls.file_to_append = Path(SystemTest.get_testing_directory())/"file_to_append.txt"
        cls.target_file = Path(SystemTest.get_testing_directory())/"target_file.txt"
        cls.create_file_to_append()
        cls.create_target_file()

    @classmethod
    def create_file_to_append(cls):
        cls.file_to_append_content = "file to append content\n"
        cls.file_to_append.open('w').write(cls.file_to_append_content)

    @classmethod
    def create_target_file(cls):
        cls.target_file_content = "target file content\n"
        cls.target_file.open('w').write(cls.target_file_content)
