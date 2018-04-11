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


class InterfaceHeader():
    
    def __init__(self, template, license_header):
        self.bare_header = ClassHeader(template, license_header)

    def instantiate_with(self, class_name):
        return self.add_content_to(self.bare_header.instantiate_with(class_name), class_name)

    @staticmethod
    def add_content_to(bare_header, class_name):
        virtual_destructor = "    virtual ~" + class_name + "() {}\n"
        method_template = "    //virtual return_type_ method_name_(input_type_) = 0;\n"
        token = "};"
        return bare_header.replace(token, virtual_destructor + "\n" + method_template + token)
        
    @staticmethod
    def extract_methods(header):
        method_token = " = 0;"
        methods = []
        for line in header.splitlines():
            if not line.find(method_token) == -1:
                methods.append(line.lstrip().replace("virtual ", "").replace(method_token, ""));
        return methods
