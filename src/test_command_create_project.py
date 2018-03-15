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
from command_create_project import CommandCreateProject

class TestCommandCreateProject(unittest.TestCase):

    def setUp(self):
        self.project_name = "abitrary_name"
        self.command = CommandCreateProject(self.project_name);

    def test_command_stored_arguments(self):
        self.assertTrue(self.project_name == self.command.project_name)

    def test_command_as_string(self):
        self.expected = CommandCreateProject.create_directory_command + " " + self.project_name
        self.assertTrue(self.expected == self.command.command_as_string)
        