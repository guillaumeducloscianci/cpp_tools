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
from pathlib import Path
from system_test import SystemTest, is_path_a_file
from command_copy_file import CommandCopyFile


class TestCommandCopyFile(unittest.TestCase):

    def setUp(self):
        self.source_name = SystemTest.get_testing_directory() + "/arbitrary_file_to_copy" # \todo: Change + to / in all relevant files
        self.destination_name = SystemTest.get_testing_directory() + "/arbitrary_file_copied"
        Path(self.source_name).open('a').write('File containing arbitrary content.')
        self.command = CommandCopyFile(self.source_name, self.destination_name);

    def test_execution(self):
        self.assertFalse(is_path_a_file(self.destination_name))
        self.command.execute();
        self.assertTrue(is_path_a_file(self.destination_name))
