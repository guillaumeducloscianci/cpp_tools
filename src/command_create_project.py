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
from command_create_directory import CommandCreateDirectory


class CommandCreateProject(Command):
    def __init__(self, project_name_):
        self.project_name = project_name_
        suffixes = ["", "/include", "/src"]
        self.directories = map(lambda suffix: self.project_name + suffix, suffixes)
        self.commands = map(lambda directory: CommandCreateDirectory(directory), self.directories)

    @staticmethod
    def create_description_from_arguments(project_name):
        return "Create project " + project_name

    def description(self):
        return self.create_description_from_arguments(self.project_name)

    def execute(self):
        for command in self.commands: # Avoid functional style (map, list comprehension) when side effects are involved.
            command.execute()
