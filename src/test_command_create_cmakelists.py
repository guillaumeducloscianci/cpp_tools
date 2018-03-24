# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command_create_cmakelists import CommandCreateCMakeLists
from unit_test import UnitTest


class TestCommandCreateCMakeLists(UnitTest):

    def test_variables(self):
        self.assertEquals(self.project_path, str(self.command.project_path))

    def test_description(self):
        self.assertIsNotEmpty(self.command.description())

    def setUp(self):
        self.project_path = "/arbitrary/project/path"
        self.command = CommandCreateCMakeLists(self.project_path)
