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
from command_parser import CommandParser

class TestCommandParser(unittest.TestCase):

    def setUp(self):
        self.parser = CommandParser()

    def test_is_valid_command(self):
        arguments = ["create", "project"]
        self.assertTrue(self.parser.is_valid_command(arguments))

    def test_is_valid_command_false_first_arg(self):
        arguments = ["asdf", "project"]
        self.assertFalse(self.parser.is_valid_command(arguments))

    def test_is_valid_command_false_second_arg(self):
        arguments = ["create", "asdf"]
        self.assertFalse(self.parser.is_valid_command(arguments))

    def test_command_parser_returns_a_command_create_project(self):
        project_name = "arbitrary_project_name"
        author_name = "author_name"
        arguments = ["create", "project", project_name, author_name]
        self.assertTrue(project_name, str(self.parser.parse(arguments).project_path.name))
