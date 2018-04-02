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


class ClassTestsTemplate():
    file_template = FileTemplate(File.read(cpp_tools_resources_directory/"class_tests.template"))

    @classmethod
    def instantiate_with(cls, project_name):
        return cls.file_template.instantiate_with(cls.create_replacement_rules(project_name))

    @staticmethod
    def create_replacement_rules(project_name):
        return {"project_name_": str(project_name)}
