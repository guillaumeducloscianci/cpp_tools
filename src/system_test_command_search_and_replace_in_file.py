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

from command_search_and_replace_in_file import CommandSearchAndReplaceInFile
from system_test import SystemTest


class TestCommandSearchAndReplaceInFile(SystemTest):

    def test_execution(self):
        self.assert_file_exists(self.target_path)
        self.assert_file_does_not_contain(self.target_path, self.replace_by)
        CommandSearchAndReplaceInFile(self.target_path, self.search_for, self.replace_by).execute()
        self.assert_file_contains(self.target_path, self.replace_by)

    @classmethod
    def setUpClass(cls):
        cls.target_path = Path(SystemTest.get_testing_directory())/"arbitrary_file_to_search_and_replace"
        cls.search_for = "search for"
        cls.replace_by = "replace_by"
        cls.create_target_file()

    @classmethod
    def create_target_file(cls):
        cls.target_path.open('w').write(cls.search_for)
