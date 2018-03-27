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
import subprocess

from directory import Directory
from file import File
from file_template import FileTemplate
from top_level_cmakelists import TopLevelCMakeLists
from system_tools import cpp_tools_resources_directory 


class ProjectParameters():

    def __init__(self, path_, author_):
        self.path = Path(path_)
        self.author = str(author_)


class Project():
    directories = ["", "include", "src", ".templates"]

    def __init__(self, parameters):
        self.path = parameters.path
        self.author = parameters.author

    def create(self):
        self.create_directory_structure() # Must appear first, before any file creation
        self.create_gitignore_file()
        self.create_git_repository()
        self.create_license_file()
        self.create_license_header_template() # Must appear before top level cmakelists creation
        self.create_readme_file()
        self.create_src_cmakelists()
        self.create_top_level_cmakelists()

    def create_directory_structure(self):
        for directory in self.create_directory_paths():
            Directory().create(directory)

    def create_gitignore_file(self):
        File.write(self.path/".gitignore", ".templates")

    def create_git_repository(self):
        subprocess.run(["git", "-C", str(self.path), "init"], stdout=subprocess.DEVNULL)

    def create_license_file(self):
        File.copy(cpp_tools_resources_directory/"GPL_v3.txt", self.path/"LICENSE.TXT")

    def create_license_header_template(self):
        replacement_rules = {"project_name_": self.path.name, "author_": self.author}
        license_header_template = cpp_tools_resources_directory/"license_header.template"
        content = FileTemplate(File.read(license_header_template)).instantiate_with(replacement_rules)
        File.write(self.create_license_header_path(), content)

    def create_readme_file(self):
        File.write(self.path/"README.md", "## " + self.path.name + "\n")

    def create_src_cmakelists(self):
        content = self.create_license_header() + File.read(cpp_tools_resources_directory/"src_CMakeLists.txt")
        File.write(self.path/"src"/"CMakeLists.txt", content)

    def create_top_level_cmakelists(self):
        cmakelists_path = self.path/"CMakeLists.txt"
        body = TopLevelCMakeLists.instantiate_with(self.path.name)
        File.write(cmakelists_path, self.create_license_header() + body)

    def create_directory_paths(self):
        return list(map(lambda directory: self.path/directory, self.directories))

    def create_license_header(self):
        replacement_rules = {"year_": str(datetime.now().year)}
        return FileTemplate(File.read(self.create_license_header_path())).instantiate_with(replacement_rules)

    def create_license_header_path(self):
        return self.path/".templates"/"license_header.template"
