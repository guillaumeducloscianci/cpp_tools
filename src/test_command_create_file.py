# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

import unittest
from command_create_file import CommandCreateFile


class TestCommandCreateFile(unittest.TestCase):

    def setUp(self):
        self.file_path = "/arbitrary/file/path"
        self.file_content = "arbitrary content"
        self.command = CommandCreateFile(self.file_path, self.file_content)

    def test_command_stored_arguments(self):
        self.assertEquals(self.file_path, str(self.command.file_path))

    def test_command_converts_to_string(self):
        self.expected = CommandCreateFile.create_description_from_arguments(self.file_path)
        self.assertEquals(self.expected, self.command.description())
