# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from file import File
from file_template import FileTemplate
from system_tools import cpp_tools_resources_directory


class ClassCreator():

    def __init__(self, class_name_, project_):
        self.class_name = class_name_
        self.project = project_ # \todo: Project directory structure should be a class

    def create_header_file(self):
        template = FileTemplate(File.read(self.project.path/".templates"/"class_header.template"))
        replacement_rules = {"class_name_": str(self.class_name), "CLASS_NAME_": str(self.class_name).upper()+"_"}
        content = self.project.create_license_header() + template.instantiate_with(replacement_rules)
        path = self.project.include_directory/(self.class_name+".h")
        File.write(path, content)

    def create_source_file(self):
        template = FileTemplate(File.read(self.project.path/".templates"/"class_source.template"))
        replacement_rules = {"class_name_": str(self.class_name)}
        content = self.project.create_license_header() + template.instantiate_with(replacement_rules)
        path = self.project.path/"src"/(self.class_name+".cpp")
        File.write(path, content)
