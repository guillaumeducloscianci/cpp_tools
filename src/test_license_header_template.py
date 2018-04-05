# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from license_header_template import LicenseHeaderTemplate
from unit_test import UnitTest


class TestLicenseHeaderTemplate(UnitTest):

    def test_create_replacement_rules(self):
        self.assert_equals({"project_name_": self.project_name, "author_": self.author},
            LicenseHeaderTemplate.create_replacement_rules(self.project_name, self.author))

    def setUp(self):
        self.author = "arbitrary_author"
        self.project_name = "arbitrary_name"
        