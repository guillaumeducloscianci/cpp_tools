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

class CommandCreateLicenseHeaderTemplate(Command):

    def __init__(self, destination_path_, project_name_, author_):
        self.destination_path = Path(destination_path_)
        self.project_name = str(project_name_)
        self.author = str(author_)
        self.commands = self.create_commands()

    def description(self):
        return "Create license header template for " + str(self.destination_path)

    def execute(self):
        for command in self.commands: command.execute()

    def create_commands(self):
        source_path = cpp_tools_resources_directory/"license_header.template"
        return [
            CommandCopyFile(source_path, self.destination_path),
            CommandSearchAndReplaceInFile(self.destination_path, "author_", self.author),
            CommandSearchAndReplaceInFile(self.destination_path, "project_name_", self.project_name)
        ]
