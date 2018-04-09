# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from implementation_header import ImplementationHeader
from license_header import LicenseHeader
from unit_test import UnitTest


class TestImplementationHeader(UnitTest):

    def test_extract_methods(self):
        self.assert_equals(ImplementationHeader.extract_methods(self.fake_interface),
            ["virtual void method1() override;", "virtual void method2() override;"])

    def test_instantiate_with(self):
        implementation_header = ImplementationHeader(self.fake_template, self.fake_license_header, self.fake_interface)
        instance = implementation_header.instantiate_with(self.class_name, self.interface_name)
        self.assert_string_contains(instance, self.class_name + ": public " + self.interface_name + " {")
        self.assert_string_contains(instance, "virtual void method1() override;\nvirtual void method2() override;\n")

    def setUp(self):
        self.fake_template = "CLASS_NAME_ class_name_ { };"
        self.fake_interface = "virtual void method1() = 0;\nvirtual void method2() = 0;\n"
        self.class_name = "arbitrary_name"
        self.interface_name = "interface_name"
        self.fake_raw_header = "};"
        self.fake_license_header = LicenseHeader("arbitrary license (year_)")
