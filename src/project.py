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

from directory import Directory


class Parameters():

    def __init__(self, path_, author_):
        self.path = Path(path_)
        self.author = str(author_)


class Project():
    directories = ["", "include", "src", ".templates"]

    def __init__(self, parameters_):
        self.parameters = parameters_

    def create_directory_structure(self):
        for directory in self.create_directory_paths():
            Directory().create(directory)

    def create_directory_paths(self):
        return list(map(lambda directory: self.parameters.path/directory, self.directories))
