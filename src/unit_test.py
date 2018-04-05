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


class UnitTest(unittest.TestCase):

    def assert_true(self, value):
        self.assertTrue(value)

    def assert_false(self, value):
        self.assertFalse(value)

    def assert_equals(self, lhs, rhs):
        self.assertEquals(lhs, rhs)

    def assert_is_not_empty(self, string):
        self.assertNotEquals("", string)

    def assert_string_does_not_contain(self, string, content):
        self.assertEquals(-1,string.find(str(content)))

    def assert_string_contains(self, string, content):
        self.assertNotEquals(-1,string.find(str(content)))