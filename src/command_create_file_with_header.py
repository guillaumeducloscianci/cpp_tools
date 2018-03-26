# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from pathlib import Path

from command import Command
from command_copy_file import CommandCopyFile
from command_search_and_replace_in_file import CommandSearchAndReplaceInFile


class CommandCreateFileWithHeader(Command):

    def __init__(self, destination_path_, license_header_template_path_):
        self.destination_path = Path(destination_path_)
        self.license_header_template_path = Path(license_header_template_path_)
        self.commands = self.create_commands()

    def description(self):
        return ("Create file " + str(self.destination_path) + " with licencse header from "
            + str(self.license_header_template_path))

    def execute(self):
        for command in self.commands: command.execute()

    def create_commands(self):
        return [CommandCopyFile(self.license_header_template_path, self.destination_path),
            CommandSearchAndReplaceInFile(self.destination_path, "year_", datetime.now().year)]
