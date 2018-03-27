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

from directory import Directory
from file import File
from file_template import FileTemplate
from top_level_cmakelists import TopLevelCMakeLists
from system_tools import cpp_tools_resources_directory 


class Parameters():

    def __init__(self, path_, author_):
        self.path = Path(path_)
        self.author = str(author_)


class Project():
    directories = ["", "include", "src", ".templates"]

    def __init__(self, parameters_):
        self.parameters = parameters_

    def create_directory_structure(self):
        for directory in self.create_directory_paths():
            Directory().create(directory)

    def create_license_file(self):
        File.copy(cpp_tools_resources_directory/"GPL_v3.txt", self.parameters.path/"LICENSE.TXT")

    def create_license_header_template(self):
        replacement_rules = {"project_name_": self.parameters.path.name, "author_": self.parameters.author}
        destination_path = self.parameters.path/".templates"/"license_header.template"
        content = FileTemplate(File.read(self.create_license_header_path())).instantiate_with(replacement_rules)
        File.write(destination_path, content)

    def create_top_level_cmakelists(self):
        cmakelists_path = self.parameters.path/"CMakeLists.txt"
        body = TopLevelCMakeLists.instantiate_with(self.parameters.path.name)
        File.write(cmakelists_path, self.create_license_header() + body)

    def create_src_cmakelists(self):
        File.copy(cpp_tools_resources_directory/"src_CMakeLists.txt", self.parameters.path/"src"/"CMakeLists.txt")

    def create_directory_paths(self):
        return list(map(lambda directory: self.parameters.path/directory, self.directories))

    def create_license_header(self):
        replacement_rules = {"year_": str(datetime.now().year)}
        return FileTemplate(File.read(self.create_license_header_path())).instantiate_with(replacement_rules)

    def create_license_header_path(self):
        return cpp_tools_resources_directory/"license_header.template"
