# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command_search_and_replace_in_file import CommandSearchAndReplaceInFile
from unit_test import UnitTest


class TestCommandSearchAndReplaceInFile(UnitTest):

    def test_variables(self):
        self.assertEquals(self.target_path, str(self.command.target_path))

    def test_description(self):
        self.assert_is_not_empty(self.command.description())

    def setUp(self):
        self.target_path = "/arbitrary/file/path"
        self.search_for = "search for"
        self.replace_by = "replace by"
        self.command = CommandSearchAndReplaceInFile(self.target_path, self.search_for, self.replace_by)
