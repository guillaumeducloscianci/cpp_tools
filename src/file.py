# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
from shutil import copy

class File():

    @staticmethod
    def copy(source_path, destination_path):
        # arguments are converted to strings because shutil.copy does not support Path objects
        copy(str(source_path), str(destination_path))

    @staticmethod
    def remove(path):
        Path(path).unlink()

    @staticmethod
    def read(path):
        return Path(path).open().read()

    @staticmethod
    def write(path, content):
        return Path(path).open('w').write(content)
