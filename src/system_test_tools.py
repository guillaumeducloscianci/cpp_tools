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
import glob
import subprocess


class SystemTest():
    directory_name_relative_to_script = "/../testing"

    @classmethod
    def setup(cls, directory_name_relative_to_script_):
        cls.directory_name_relative_to_script = directory_name_relative_to_script_
        cls.clean_testing_directory()

    @classmethod
    def clean_testing_directory(cls):
        subprocess.run(["gvfs-trash"] + glob.glob(cls.get_testing_directory() + "/*"))

    @classmethod
    def get_testing_directory(cls):
        return get_script_directory() + cls.directory_name_relative_to_script


def is_path_a_directory(path):
    return os.path.isdir(path)

def is_path_a_file(path):
    return os.path.isfile(path)

def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))
