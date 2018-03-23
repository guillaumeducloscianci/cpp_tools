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
from command_create_directory import CommandCreateDirectory
from command_create_file import CommandCreateFile
from command_create_cmakelists import CommandCreateCMakeLists
from command_create_git_repository import CommandCreateGitRepository
from command_create_license_header_template import CommandCreateLicenseHeaderTemplate
from command_search_and_replace_in_file import CommandSearchAndReplaceInFile
from system_tools import cpp_tools_resources_directory 


class CommandCreateProject(Command):
    project_directories = ["", "include", "src", ".templates"]

    def __init__(self, project_path_):
        self.project_path = Path(project_path_)
        self.directories = map(lambda directory: self.project_path/directory, self.project_directories)
        self.commands = self.create_commands()

    @staticmethod
    def create_description_from_arguments(project_path):
        return "Create project " + str(project_path)

    def create_commands(self):
        commands = self.create_directory_structure_commands()
        commands += [
            self.create_license_command(),
            self.create_license_template_command(),
            self.create_readme_command(),
            CommandCreateGitRepository(self.project_path),
            CommandCreateCMakeLists(self.project_path)
        ]
        return commands

    def description(self):
        return self.create_description_from_arguments(self.project_path)

    def execute(self):
        for command in self.commands: # Avoid functional style (map, list comprehension) when side effects are involved.
            command.execute()

    def create_directory_structure_commands(self):
        return list(map(lambda directory: CommandCreateDirectory(directory), self.directories))

    def create_license_command(self):
        return CommandCopyFile(cpp_tools_resources_directory/"GPL_v3.txt", self.project_path/"LICENSE.TXT")

    def create_readme_command(self):
        return CommandCreateFile(self.project_path/"README.md", "## " + self.project_path.name + "\n")

    def create_license_template_command(self):
        destination_path = Path(self.project_path/".templates/license_header.template")
        return CommandCreateLicenseHeaderTemplate(destination_path, self.project_path.name)
