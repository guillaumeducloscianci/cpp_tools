# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

import os

# \todo: Refactor as a class SystemTools with class methods that support strings (os lib style) and Path objects
#       (pathlib style)

def is_path_a_directory(path):
    return os.path.isdir(path)

def is_path_a_file(path):
    return os.path.isfile(path)

def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))

def get_project_directory():
    return os.path.dirname(os.path.realpath(__file__)) + "/.."
