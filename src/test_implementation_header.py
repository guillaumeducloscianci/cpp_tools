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

    def test_instantiate_with(self):
        implementation_header = ImplementationHeader(self.fake_template, self.fake_license_header, self.fake_interface)
        instance = implementation_header.instantiate_with(self.class_name, self.interface_name)
        self.assert_implementation_includes_interface(instance)
        self.assert_implementation_namespace_is_well_formatted(instance)
        self.assert_implementation_inherits_from_interface(instance)
        self.assert_implementation_contains_methods(instance)

    def setUp(self):
        self.namespace_begin = "namespace Fake {" 
        self.namespace_end = "} /* Fake */"
        self.class_name = "arbitrary_name"
        self.interface_name = "interface_name"
        self.fake_template = self.namespace_begin + " CLASS_NAME_ class_name_ { }; " + self.namespace_end
        self.fake_interface = (self.namespace_begin + "\nclass " + self.interface_name
            + " {\nvirtual void method1() = 0;\nvirtual void method2() = 0;\n};\n" + self.namespace_end)
        self.fake_raw_header = "};"
        self.fake_license_header = LicenseHeader("arbitrary license (year_)")

    def assert_implementation_contains_methods(self, instance):
        self.assert_string_contains(instance, "    void method1() override;\n    void method2() override;\n")

    def assert_implementation_includes_interface(self, instance):
        self.assert_string_contains(instance, "#include <Fake/" + self.interface_name + ".h>")

    def assert_implementation_inherits_from_interface(self, instance):
        self.assert_string_contains(instance, self.class_name + ": public " + self.interface_name + " {")

    def assert_implementation_namespace_is_well_formatted(self, instance):
        self.assert_string_contains(instance, self.namespace_begin)
        self.assert_string_contains(instance, self.namespace_end)
