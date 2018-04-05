# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path


class ProjectDirectories():
    
    def __init__(self, root_):
        self.root = Path(root_)

    def __truediv__(self, path):
        return self.root/path

    def __str__(self):
        return str(self.root)

    @property
    def to_class_header_template(self):
        return self.root/".templates/class_header.template"

    @property
    def to_license_header_template(self):
        return self.root/".templates/license_header.template"

    @property
    def to_include_directory(self):
        return self.root/"include"/self.root.name

    @property
    def to_source_directory(self):
        return self.root/"src"

    @property
    def to_templates_directory(self):
        return self.root/".templates"

    def list_top_down(self):
        return [self.root, self.to_templates_directory, self.to_source_directory, self.root/"include",
            self.to_include_directory]
