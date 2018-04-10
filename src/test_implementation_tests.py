# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from implementation_tests import ImplementationTests
from license_header import LicenseHeader
from unit_test import UnitTest


class TestImplementationTests(UnitTest):

    def test_instantiate_with(self):
        source = ImplementationTests(self.fake_template, self.fake_license_header, self.fake_header)
        instance = source.instantiate_with(self.class_name)
        self.assert_string_contains(instance, "TEST_F(test_" + self.class_name + ", method1) {\n\n}\n")
        self.assert_string_contains(instance, "TEST_F(test_" + self.class_name + ", method2) {\n\n}\n")

    def setUp(self):
        self.fake_template = "class_name_\n"
        self.fake_header = "virtual void method1() = 0;\nvirtual void method2() = 0;\n"
        self.fake_license_header = LicenseHeader("arbitrary license (year_)")
        self.class_name = "arbitrary_name"
