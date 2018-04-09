# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from interface_header import InterfaceHeader
from file import File
from license_header import LicenseHeader
from project import Project, ProjectParameters


class InterfaceCreator():

    def __init__(self, class_name_, project_paths):
        self.class_name = class_name_
        self.path = project_paths

    def create(self):
        path = self.path.to_include_directory/(self.class_name+".h")
        template = InterfaceHeader(File.read(self.path.to_class_header_template), self.create_license_header())
        File.write(self.path.to_include_directory/(self.class_name+".h"), template.instantiate_with(self.class_name))

    def create_license_header(self):
        return LicenseHeader(File.read(self.path.to_license_header_template))
