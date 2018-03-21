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
from command_create_cmakelists import CommandCreateCMakeLists
from command_create_directory import CommandCreateDirectory


class TestCommandCreateCMakeLists(unittest.TestCase):

    def create_source_dir(self):
        CommandCreateDirectory(self.project_path/"src").execute()

    def setUp(self):
        self.project_path = Path(SystemTest.get_testing_directory())
        self.create_source_dir()

    def test_execution(self):
        self.assertFalse((self.project_path/"CMakeLists.txt").is_file())
        CommandCreateCMakeLists(self.project_path).execute()
        self.assertTrue((self.project_path/"CMakeLists.txt").is_file())
        self.assertNotEqual(-1, (self.project_path/"CMakeLists.txt").open().read().find(self.project_path.name))
