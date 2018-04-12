# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_header import ClassHeader
from interface_header import InterfaceHeader

class ImplementationHeader():
    
    def __init__(self, template, license_header, interface):
        self.bare_header = ClassHeader(template, license_header)
        self.interface = interface

    def instantiate_with(self, class_name, interface_name):
        return self.add_content_to(self.bare_header.instantiate_with(class_name), class_name, interface_name)

    def add_content_to(self, bare_header, class_name, interface_name):
        class_end = "};"
        inheritance = ": public " + interface_name
        bare_header = bare_header.replace(class_name, class_name + inheritance)
        for method in InterfaceHeader.extract_methods(self.interface):
            bare_header = bare_header.replace(class_end, self.create_signature(method) + class_end)
        return bare_header

    @staticmethod
    def create_signature(method):
        return "    " + method + " override;\n"
