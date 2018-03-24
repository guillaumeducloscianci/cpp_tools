# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

import sys

from command_create_project import CommandCreateProject


class CommandParser:
    def is_valid_command(self, arguments):
        if (len(arguments) < 2):
            return False
        if (arguments[0:2] != ["create", "project"]):
            return False
        return True

    def parse(self, arguments):
        if not self.is_valid_command(arguments):
            print("Invalid syntax")
            sys.exit(1)
        return CommandCreateProject(arguments[2], arguments[3])
