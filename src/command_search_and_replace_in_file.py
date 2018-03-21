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


class CommandSearchAndReplaceInFile(Command):

    @staticmethod
    def create_description_from_arguments(target_path, search_for, replace_by):
        return "Replace" + str(search_for) + " by " + str(replace_by) + " in " + str(target_path)

    def __init__(self, target_path_, search_for_, replace_by_):
        self.target_path = Path(target_path_)
        self.search_for = str(search_for_)
        self.replace_by = str(replace_by_)

    def description(self):
        return self.create_description_from_arguments(self.target_path, self.search_for, self.replace_by)

    def execute(self):
        file_content = self.target_path.open().read().replace(self.search_for, self.replace_by)
        self.target_path.open('w').write(file_content)
