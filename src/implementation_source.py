# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_source import ClassSource


class ImplementationSource():
    
    def __init__(self, template, license_header, header):
        self.bare_source = ClassSource(template, license_header)
        self.header = header

    def instantiate_with(self, class_name):
        return self.add_content_to(self.bare_source.instantiate_with(class_name), class_name)

    def add_content_to(self, bare_source, class_name):
        for method in self.extract_methods(self.header):
            bare_source += self.create_method_implementation(method, class_name)
        return bare_source

    @staticmethod
    def create_method_implementation(signature, class_name):
        name = signature.split()[1]
        return signature.replace(name, class_name+"::"+ name) + " {\n\n}\n\n"

    @staticmethod
    def extract_methods(header):
        method_token = " override;"
        methods = []
        for line in header.splitlines():
            if not line.find(method_token) == -1:
                methods.append(line.replace("virtual ", "").replace(method_token, ""));
        return methods
