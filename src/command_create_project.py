# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from command import Command
from command_copy_file import CommandCopyFile
from command_create_directory import CommandCreateDirectory
from command_create_file import CommandCreateFile
from system_tools import get_project_directory

class CommandCreateProject(Command):
    project_directories = ["", "/include", "/src"]

    def __init__(self, project_name_):
        self.project_name = project_name_
        self.directories = map(lambda suffix: self.project_name + suffix, self.project_directories)
        self.commands = self.create_commands()

    @staticmethod
    def create_description_from_arguments(project_name):
        return "Create project " + project_name

    def create_commands(self):
        commands = self.create_directory_structure_commands()
        commands.append(self.create_license_command())
        commands.append(self.create_readme_command())
        return commands

    def description(self):
        return self.create_description_from_arguments(self.project_name)

    def execute(self):
        for command in self.commands: # Avoid functional style (map, list comprehension) when side effects are involved.
            command.execute()

    def create_directory_structure_commands(self):
        return list(map(lambda directory: CommandCreateDirectory(directory), self.directories))

    def create_license_command(self):
        return CommandCopyFile(get_project_directory()+"/LICENSE.TXT", self.project_name+"/LICENSE.TXT")

    def create_readme_command(self):
        return CommandCreateFile(self.project_name + "/README.md", "## " + self.project_name + "\n")
