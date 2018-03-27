# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from project import Project, ProjectParameters
from system_test import SystemTest


class TestProject(SystemTest):

    def test_create_directory_structure(self):
        self.assert_directory_does_not_exist(self.path)
        Project(self.parameters).create_directory_structure()
        self.assert_has_a_project_directory_structure()

    def setUp(self):
        self.path = SystemTest.get_testing_directory()/"arbitrary_project"
        self.author = "arbitrary_author"
        self.parameters = ProjectParameters(self.path, self.author)

    def assert_has_a_project_directory_structure(self):
        for directory in Project.directories:
            self.assert_directory_exists(self.path/directory)


class TestProjectWithDirectoryStructure(SystemTest):

    def test_create_license_file(self):
        self.project.create_license_file()
        self.assert_project_directory_contains("LICENSE.TXT")

    def test_create_license_header_template(self):
        self.project.create_license_header_template()
        self.assert_project_directory_contains(".templates/license_header.template")

    def test_create_readme_file(self):
        self.project.create_readme_file()
        self.assert_project_directory_contains("README.md")

    def test_create_gitignore_file(self):
        self.project.create_gitignore_file()
        self.assert_project_directory_contains(".gitignore")

    @classmethod
    def setUpClass(cls):
        cls.setUpClassFromProjectName("arbitrary_project_with_directory_structure")

    def assert_project_directory_contains(self, file_name):
        self.assert_file_exists(self.path/file_name)

    @classmethod
    def setUpClassFromProjectName(cls, name):
        cls.path = SystemTest.get_testing_directory()/name
        cls.author = "arbitrary_author"
        cls.project = Project(ProjectParameters(cls.path, cls.author))
        cls.project.create_directory_structure()


class TestProjectWithLicenseHeaderTemplate(TestProjectWithDirectoryStructure):

    def test_create_top_level_cmakelists(self):
        self.project.create_top_level_cmakelists()
        cmakelists_path = self.path/"CMakeLists.txt"
        self.assert_project_directory_contains(cmakelists_path.name)
        self.assert_file_contains(cmakelists_path, self.path.name)
        self.assert_file_has_license_header(cmakelists_path)

    def test_create_src_cmakelists(self):
        self.project.create_src_cmakelists()
        self.assert_project_directory_contains("src/CMakeLists.txt")
        cmakelists_path = self.path/"src"/"CMakeLists.txt"
        self.assert_file_has_license_header(cmakelists_path)

    @classmethod
    def setUpClass(cls):
        cls.setUpClassFromProjectName("arbitrary_project_with_license_header")
