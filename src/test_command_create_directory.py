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
from command_create_directory import CommandCreateDirectory

class TestCommandCreateDirectory(unittest.TestCase):

    def setUp(self):
        self.directory_name = "abitrary_name"
        self.command = CommandCreateDirectory(self.directory_name);

    def test_command_stored_arguments(self):
        self.assertTrue(self.directory_name == self.command.directory_name)

    def test_command_converts_to_string(self):
        self.expected = CommandCreateDirectory.unix_create_directory_command + " " + self.directory_name
        self.assertTrue(self.expected == self.command.to_string())
