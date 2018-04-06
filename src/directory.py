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

def remove_path(path_):
    path = Path(path_)
    if path.is_symlink() or path.is_file(): # is_symlink must appear before is_dir
        path.unlink()
    elif path.is_dir():
        Directory.remove(path)
    else:
        return


class Directory():

    @staticmethod
    def create(path):
        Path(path).mkdir()

    @staticmethod
    def remove(path):
        if not Path(path).exists(): return
        for p in Path(path).iterdir():
            remove_path(p)
        Path(path).rmdir()
