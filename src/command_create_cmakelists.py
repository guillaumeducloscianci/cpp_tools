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
from system_tools import cpp_tools_resources_directory

class CommandCreateCMakeLists(Command):

    @staticmethod
    def create_description_from_arguments(project_path):
        return "Create CMakeLists.txt for " + str(project_path)

    def __init__(self, project_path_):
        self.project_path = Path(project_path_)

    def description(self):
        return self.create_description_from_arguments(self.project_path)

    def execute(self):
        source_path = cpp_tools_resources_directory/"CMakeLists.template"
        destination_path = self.project_path/"CMakeLists.txt"
        CommandCopyFile(source_path,destination_path).execute()
        file_content = destination_path.open().read().replace("project_name_", self.project_path.name)
        destination_path.open('w').write(file_content)
