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

    def add_content_to(self, header, class_name, interface_name):
        header = self.add_interface_header(header, self.interface)
        header = self.add_inheritance(header, class_name, interface_name)
        header = self.add_methods(header, self.interface)
        return header

    @staticmethod
    def add_inheritance(header, class_name, interface_name):
        inheritance = ": public " + interface_name
        return header.replace(class_name + " {", class_name + inheritance + " {")

    @staticmethod
    def add_interface_header(header, interface):
        project_name = InterfaceHeader.extract_project_name(interface)
        interface_name = InterfaceHeader.extract_interface_name(interface)
        include = "#include <" + project_name + "/" + interface_name + ".h>\n"
        return header.replace("namespace", include + "\nnamespace")

    @staticmethod
    def add_methods(header, interface):
        class_end = "};"
        for method in InterfaceHeader.extract_methods(interface):
            header = header.replace(class_end, ImplementationHeader.create_signature(method) + class_end)
        return header

    @staticmethod
    def create_signature(method):
        return "    " + method + " override;\n"
