# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command import Command
from shutil import copy


class CommandCopyFile(Command):

    @staticmethod
    def create_description_from_arguments(source_name, destination_name):
        return "Copy " + source_name + " to " + destination_name

    def __init__(self, source_name_, destination_name_):
        self.source_name = source_name_
        self.destination_name = destination_name_

    def description(self):
        return self.create_description_from_arguments(self.source_name, self.destination_name)

    def execute(self):
        copy(self.source_name, self.destination_name)
