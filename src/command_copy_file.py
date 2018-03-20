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
    def create_description_from_arguments(source_path, destination_path):
        return "Copy " + str(source_path) + " to " + str(destination_path)

    # path arguments can be either strings of Path objects from pathlib
    def __init__(self, source_path_, destination_name_):
        # arguments are converted to strings because copy does not support Path
        self.source_path = str(source_path_)
        self.destination_path = str(destination_name_)

    def description(self):
        return self.create_description_from_arguments(self.source_path, self.destination_path)

    def execute(self):
        copy(self.source_path, self.destination_path)
