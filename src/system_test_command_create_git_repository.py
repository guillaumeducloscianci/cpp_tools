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
from system_test import SystemTest
from command_create_git_repository import CommandCreateGitRepository


class TestCommandCreateDirectory(unittest.TestCase):

    def setUp(self):
        self.repository_path = Path(SystemTest.get_testing_directory())

    def test_execution(self):
        self.assertFalse((self.repository_path/".git").is_dir())
        self.assertFalse((self.repository_path/".gitignore").is_file())
        CommandCreateGitRepository(self.repository_path).execute()
        self.assertTrue((self.repository_path/".git").is_dir())
        self.assertTrue((self.repository_path/".gitignore").is_file())
