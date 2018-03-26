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
from command_copy_file import CommandCopyFile
from command_search_and_replace_in_file import CommandSearchAndReplaceInFile
from system_tools import cpp_tools_resources_directory


class CommandCreateCMakeLists(Command):

    def __init__(self, project_path_):
        self.project_path = Path(project_path_)
        self.commands = self.create_commands()

    def description(self):
        return "Create CMakeLists.txt for " + str(self.project_path)

    def execute(self):
        for command in self.commands: command.execute()

    def create_commands(self):
        source_path = cpp_tools_resources_directory/"CMakeLists.template"
        destination_path = self.project_path/"CMakeLists.txt"
        return [CommandCopyFile(source_path, destination_path),
            CommandSearchAndReplaceInFile(destination_path, "project_name_", self.project_path.name)]
