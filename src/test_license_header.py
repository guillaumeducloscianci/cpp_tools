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
from license_header import LicenseHeader
from unit_test import UnitTest


class TestLicenseHeader(UnitTest):

    def test_create_replacement_rules(self):
        self.assert_equals({"year_": str(datetime.now().year)}, LicenseHeader.create_replacement_rules())

    def test_instantiate(self):
        self.instance = LicenseHeader(self.fake_template).instantiate()
        for token, value in LicenseHeader.create_replacement_rules().items():
            self.assert_string_does_not_contain(self.instance, token)
            self.assert_string_contains(self.instance, value)

    def test_instantiate_for_cmakelists(self):
        self.instance = LicenseHeader(self.fake_template).instantiate_for_cmakelists()
        for line in self.instance.splitlines():
            self.assert_true(self.instance.startswith("# "))
        self.assert_true(self.instance.endswith("\n\n"))

    def test_instantiate_for_cpp(self):
        self.instance = LicenseHeader(self.fake_template).instantiate_for_cpp()
        self.assert_true(self.instance.startswith("/* "))
        self.assert_true(self.instance.endswith(" */\n\n"))

    def setUp(self):
        self.fake_template = "year_"
