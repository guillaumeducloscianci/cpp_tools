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
import subprocess

from command import Command
from command_create_file import CommandCreateFile


class CommandCreateGitRepository(Command):

    def __init__(self, repository_path_):
        self.repository_path = Path(repository_path_)

    def description(self):
        return "Create git repository in " + str(self.repository_path)

    def execute(self):
        subprocess.run(["git", "-C", str(self.repository_path), "init"], stdout=subprocess.DEVNULL)
        CommandCreateFile(self.repository_path/".gitignore", "").execute()
