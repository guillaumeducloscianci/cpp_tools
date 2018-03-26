# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

from command import Command


class CommandAppendFileToFile(Command):

    def __init__(self, file_to_append_, target_file_):
        self.file_to_append = Path(file_to_append_)
        self.target_file = Path(target_file_)

    def description(self):
        return ("Append file " + str(self.file_to_append) + " to file " + str(self.target_file))

    def execute(self):
        content = self.file_to_append.open().read()
        self.target_file.open('a').write(content)