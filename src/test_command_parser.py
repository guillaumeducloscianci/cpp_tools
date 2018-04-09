# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command_parser import CommandParser
from unit_test import UnitTest


class TestCommandParser(UnitTest):

    def setUp(self):
        self.parser = CommandParser()

    def test_command_parser_returns_a_command_create_class(self):
        class_name = "class_name"
        arguments = ["create", "class", "--name", class_name]
        self.assert_equals(class_name, str(self.parser.parse(arguments).class_creator.class_name))

    def test_command_parser_returns_a_command_create_interface(self):
        class_name = "class_name"
        arguments = ["create", "interface", "--name", class_name]
        self.assert_equals(class_name, str(self.parser.parse(arguments).interface_creator.class_name))

    def test_command_parser_returns_a_command_create_project(self):
        project_name = "arbitrary_project_name"
        author_name = "author_name"
        arguments = ["create", "project", "--name", project_name, "--author", author_name]
        self.assert_equals(project_name, str(self.parser.parse(arguments).project.name))

