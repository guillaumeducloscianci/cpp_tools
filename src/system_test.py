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
import glob
import subprocess
from unit_test import UnitTest

from system_tools import cpp_tools_directory


class SystemTest(UnitTest):
    directory_name = "testing"

    @classmethod
    def reset(cls, directory_name_):
        cls.directory_name = directory_name_
        cls.clean_testing_directory()

    @classmethod
    def clean_testing_directory(cls):
        #subprocess does not support Path objects.
        directory = str(cls.get_testing_directory())
        subprocess.run(["gvfs-trash"] + glob.glob(directory+"/*") + glob.glob(directory+"/.*")) # \todo: use pathlib directly?

    @classmethod
    def get_testing_directory(cls):
        return cpp_tools_directory/cls.directory_name

    def assert_directory_does_not_exist(self, directory_path):
        self.assertFalse(Path(directory_path).is_dir())

    def assert_directory_exists(self, directory_path):
        self.assertTrue(Path(directory_path).is_dir())

    def assert_file_does_not_contain(self, file_path, content):
        self.assertEquals(-1,Path(file_path).open().read().find(str(content)))

    def assert_file_does_not_exist(self, file_path):
        self.assertFalse(Path(file_path).is_file())

    def assert_file_contains(self, file_path, content):
        self.assertNotEquals(-1,Path(file_path).open().read().find(str(content)))

    def assert_file_exists(self, file_path):
        self.assertTrue(Path(file_path).is_file())

    def assert_file_has_license_header(self, file_path):
        self.assertNotEquals(-1,Path(file_path).open().read().find("free software"))
