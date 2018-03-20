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


class CommandCreateFile(Command):

    @staticmethod
    def create_description_from_arguments(file_path):
        return "Create file " + str(file_path)

    def __init__(self, file_path_, file_content_):
        self.file_path = Path(file_path_)
        self.file_content = str(file_content_)

    def description(self):
        return self.create_description_from_arguments(self.file_path)

    def execute(self):
        self.file_path.open(mode='w').write(self.file_content)
