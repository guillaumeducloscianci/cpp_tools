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
from command_create_license_header_template import CommandCreateLicenseHeaderTemplate


class TestCommandCreateLicenseHeaderTemplate(unittest.TestCase):

    def assert_license_header_contains(self, should_contain):
        self.assertTrue(-1, self.destination_path.open().read().find(should_contain))

    def assert_license_header_does_not_contain(self, should_not_contain):
        self.assertEqual(-1, self.destination_path.open().read().find(should_not_contain))

    def setUp(self):
        self.author = "arbitrary_author"
        self.project_path = Path(SystemTest.get_testing_directory())
        self.destination_path = self.project_path/"license_header.template"

    def test_execution(self):
        self.assertFalse(self.destination_path.is_file())
        CommandCreateLicenseHeaderTemplate(self.destination_path, self.project_path.name, self.author).execute()
        self.assertTrue(self.destination_path.is_file(), msg=str(self.destination_path))
        self.assert_license_header_does_not_contain("author_")
        self.assert_license_header_does_not_contain("project_name_")
        self.assert_license_header_contains(self.author)
        self.assert_license_header_contains(self.project_path.name)
