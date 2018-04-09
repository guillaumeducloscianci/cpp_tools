# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command import Command
from interface_creator import InterfaceCreator


class CommandCreateInterface(Command):

    def __init__(self, class_name, project_directories):
        self.interface_creator = InterfaceCreator(class_name, project_directories)

    def description(self):
        return "Create interface " + str(self.interface_creator.class_name)

    def execute(self):
        self.interface_creator.create()
