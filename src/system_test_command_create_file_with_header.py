# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from pathlib import Path

from command_create_file_with_header import CommandCreateFileWithHeader
from system_test import SystemTest
from system_tools import cpp_tools_resources_directory


class TestCommandCreateFileWithHeader(SystemTest):

    def test_execution(self):
        self.assert_file_does_not_exist(self.destination_path)
        CommandCreateFileWithHeader(self.destination_path, self.license_header_template_path).execute()
        self.assert_file_exists(self.destination_path)
        self.assert_file_contains(self.destination_path, datetime.now().year)

    def setUp(self):
        self.destination_path = Path(SystemTest.get_testing_directory())/"file_with_header.txt"
        self.license_header_template_path = cpp_tools_resources_directory/"license_header.template"
