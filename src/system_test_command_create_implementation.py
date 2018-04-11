# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

from command_create_implementation import CommandCreateImplementation
from directory import Directory
from system_test import SystemTest
from system_test_implementation_creator import TestImplementationCreatorTools


class TestCommandCreateImplementation(TestImplementationCreatorTools):

    def test_execution(self):
        command = CommandCreateImplementation(self.class_name, self.path, self.interface_path.stem)
        self.assert_implementation_does_not_exist()
        command.execute()
        self.assert_implementation_exists()

    @classmethod
    def setUpClass(cls):
        cls.setup_base()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()
