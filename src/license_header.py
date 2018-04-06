# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from file import File
from file_template import FileTemplate
from system_tools import cpp_tools_resources_directory


class LicenseHeader():
    
    def __init__(self, template_):
        self.template = FileTemplate(template_)

    def instantiate(self):
        return self.template.instantiate_with(self.create_replacement_rules())

    def instantiate_for_cmakelists(self):
        instance = ""
        for line in self.instantiate().splitlines():
            instance += ("# " + line + "\n")
        return instance + "\n"

    def instantiate_for_cpp(self):
        instance = self.instantiate()
        if instance[-1] == "\n": instance = instance[:-1]
        return "/* " + instance + " */\n\n"

    @staticmethod
    def create_replacement_rules():
        return {"year_": str(datetime.now().year)}
