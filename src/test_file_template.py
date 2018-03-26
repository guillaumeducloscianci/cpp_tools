# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from file_template import FileTemplate
from unit_test import UnitTest


class TestFileTemplate(UnitTest):

    def test_instantiation(self):
        self.assert_equals(self.instance, FileTemplate(self.template).instantiate(self.token_to_value))

    def setUp(self):
        self.template = "Arbitrary text with tokens_ to replace_."
        self.instance = "Arbitrary text with replaced to tokens."
        self.token_to_value = {"tokens_": "replaced", "replace_": "tokens"}
