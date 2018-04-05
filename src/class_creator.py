# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from class_header import ClassHeader
from file import File
from file_template import FileTemplate
from license_header import LicenseHeader
from project import Project, ProjectParameters
from system_tools import cpp_tools_resources_directory


class ClassCreator():

    def __init__(self, class_name_, project_directories):
        self.class_name = class_name_
        self.path = project_directories

    def create(self):
        self.create_header_file()
        self.create_source_file()
        self.create_tests_file()
        self.add_to_cmakelists()

    def add_to_cmakelists(self):
        end_of_source_files = ") # add_library"
        end_of_test_files = ") # add_tests"
        content = File.read(self.path.to_source_directory/"CMakeLists.txt")
        content = content.replace(end_of_source_files, "    "+self.class_name+".cpp\n"+end_of_source_files)
        content = content.replace(end_of_test_files, "    "+self.class_name+"_tests.cpp\n"+end_of_test_files)
        File.write(self.path.to_source_directory/"CMakeLists.txt", content)
        return content

    def create_header_file(self):
        header_template = ClassHeader(File.read(self.path.to_class_header_template), self.create_license_header())
        path = self.path.to_include_directory/(self.class_name+".h")
        File.write(path, header_template.instantiate_with(self.class_name))

    def create_source_file(self):
        template = FileTemplate(File.read(self.path.to_templates_directory/"class_source.template"))
        replacement_rules = {"class_name_": str(self.class_name)}
        content = self.create_license_header() + template.instantiate_with(replacement_rules)
        path = self.path.to_source_directory/(self.class_name+".cpp")
        File.write(path, content)

    def create_tests_file(self):
        template = FileTemplate(File.read(self.path.to_templates_directory/"class_tests.template"))
        replacement_rules = {"class_name_": str(self.class_name)}
        content = self.create_license_header() + template.instantiate_with(replacement_rules)
        path = self.path.to_source_directory/(self.class_name+"_tests.cpp")
        File.write(path, content)

    def create_license_header(self):
        return LicenseHeader(File.read(self.path.to_license_header_template)).instantiate_for_cpp()
