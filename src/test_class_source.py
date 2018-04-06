# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_source import ClassSource
from license_header import LicenseHeader
from unit_test import UnitTest


class TestClassSource(UnitTest):

    def test_create_replacement_rules(self):
        self.assert_equals({"class_name_": str(self.class_name)}, ClassSource.create_replacement_rules(self.class_name))

    def test_instantiate_with(self):
        self.instance = ClassSource(self.fake_template, self.fake_license_header).instantiate_with(self.class_name)
        for token, value in ClassSource.create_replacement_rules(self.class_name).items():
            self.assert_string_does_not_contain(self.instance, token)
            self.assert_string_contains(self.instance, value)
        # \todo : add test to check header formatting

    def setUp(self):
        self.fake_template = "class_name_"
        self.fake_license_header = LicenseHeader("arbitrary license (year_)").instantiate_for_cpp()
        self.class_name = "arbitrary_name"
