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
from implementation_creator import ImplementationCreator


class CommandCreateImplementation(Command):

    def __init__(self, class_name, project_paths, interface_name):
        self.implementation_creator = ImplementationCreator(class_name, project_paths, interface_name)

    def description(self):
        return ("Create implementation " + str(self.implementation_creator.class_name) + "of interface "
            + self.interface_name)

    def execute(self):
        self.implementation_creator.create()
