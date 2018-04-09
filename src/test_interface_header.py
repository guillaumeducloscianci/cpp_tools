# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from interface_header import InterfaceHeader
from license_header import LicenseHeader
from unit_test import UnitTest


class TestInterfaceHeader(UnitTest):

    def test_instantiate_with(self):
        instance = InterfaceHeader(self.fake_template, self.fake_license_header).instantiate_with(self.class_name)
        self.assert_string_contains(instance, "virtual ~" + self.class_name + "() {}")
        self.assert_string_contains(instance, "//virtual return_type_ method_name_(input_type_) = 0;")

    def setUp(self):
        self.fake_template = "CLASS_NAME_ class_name_ { };"
        self.class_name = "arbitrary_name"
        self.fake_raw_header = "};"
        self.fake_license_header = LicenseHeader("arbitrary license (year_)")
        self.interface_header = InterfaceHeader(self.fake_template, self.fake_license_header)
