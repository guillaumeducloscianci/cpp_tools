#!/usr/bin/env python3

# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from system_test import SystemTest
from test_suite import TestSuite
from system_test_suite import create_system_test_suite
from unit_test_suite import create_unit_test_suite

if __name__ == '__main__':
    system_test_suite = create_system_test_suite()
    unit_test_suite = create_unit_test_suite()
    system_test_suite.run()
    unit_test_suite.run()