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
from pathlib import Path


class CommandCreateDirectory(Command):

    @staticmethod
    def create_description_from_arguments(directory_path):
        return "Create directory " + str(directory_path)

    def __init__(self, directory_path_):
        self.directory_path = Path(directory_path_)

    def description(self):
        return self.create_description_from_arguments(self.directory_path)

    def execute(self):
        self.directory_path.mkdir()
