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

from class_header_template import ClassHeaderTemplate
from class_source_template import ClassSourceTemplate
from class_tests_template import ClassTestsTemplate
from directory import Directory
from file import File
from file_template import FileTemplate
from license_header_template import LicenseHeaderTemplate
from project_directories import ProjectDirectories
from top_level_cmakelists import TopLevelCMakeLists
from system_tools import cpp_tools_resources_directory 


class ProjectParameters():

    def __init__(self, path_, author_):
        self.path = Path(path_)
        self.author = str(author_)


class Project():
    def __init__(self, parameters):
        self.name = parameters.path.name
        self.path = ProjectDirectories(parameters.path)
        self.author = parameters.author

    def create(self):
        self.create_directory_structure() # Must appear first, before any file creation
        self.create_gitignore_file()
        self.create_git_repository()
        self.create_license_file()
        self.create_class_templates()
        self.create_license_header_template() # Must appear before top level cmakelists creation
        self.create_readme_file()
        self.create_src_cmakelists()
        self.create_top_level_cmakelists()

    def create_class_templates(self):
        path = lambda suffix: self.path.to_templates_directory/("class_" + str(suffix) + ".template")
        suffixToTemplate = {"header": ClassHeaderTemplate, "source": ClassSourceTemplate, "tests": ClassTestsTemplate}
        for suffix, template in suffixToTemplate.items():
            File.write(path(suffix), template.instantiate_with(self.name))

    def create_directory_structure(self):
        for directory in self.path.list_top_down(): Directory().create(directory)

    def create_gitignore_file(self):
        File.write(self.path/".gitignore", ".templates")

    def create_git_repository(self):
        subprocess.run(["git", "-C", str(self.path), "init"], stdout=subprocess.DEVNULL)

    def create_license_file(self):
        File.copy(cpp_tools_resources_directory/"GPL_v3.txt", self.path/"LICENSE.TXT")

    def create_license_header_template(self):
        content = LicenseHeaderTemplate().instantiate_with(self.name, self.author)
        File.write(self.create_license_header_template_path(), content)

    def create_readme_file(self):
        content = "# " + self.name + "\n"
        File.write(self.path/"README.md", content)

    def create_src_cmakelists(self):
        content = self.create_license_header() + File.read(cpp_tools_resources_directory/"src_CMakeLists.txt")
        File.write(self.path.to_source_directory/"CMakeLists.txt", content)

    def create_top_level_cmakelists(self):
        content = self.create_license_header() + TopLevelCMakeLists.instantiate_with(self.name)
        File.write(self.path/"CMakeLists.txt", content)

    def create_license_header(self):
        replacement_rules = {"year_": str(datetime.now().year)}
        return FileTemplate(File.read(self.create_license_header_template_path())).instantiate_with(replacement_rules)

    def create_license_header_template_path(self):
        return self.path.to_templates_directory/"license_header.template"
