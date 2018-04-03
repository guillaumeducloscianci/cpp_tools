# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from directory import Directory
from project import Project, ProjectParameters
from system_test import SystemTest


class TestProjectTools(SystemTest):

    @classmethod
    def setup_base(cls):
        cls.author = "arbitrary_author"
        cls.path = SystemTest.get_testing_directory()/"arbitrary_project"
        cls.project = Project(ProjectParameters(cls.path, cls.author))

    @classmethod
    def tear_down_base(cls):
        Directory.remove(cls.path)

    def assert_has_a_project_directory_structure(self):
        for directory in self.project.directories:
            self.assert_directory_exists(self.path/directory)

    def assert_project_directory_contains(self, file_name):
        self.assert_file_exists(self.path/file_name)


class TestProjectDirectoryStructure(TestProjectTools):

    def test_create_directory_structure(self):
        self.assert_directory_does_not_exist(self.path)
        self.project.create_directory_structure()
        self.assert_has_a_project_directory_structure()

    @classmethod
    def setUpClass(cls):
        cls.setup_base()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()


class TestProjectWithDirectoryStructure(TestProjectTools):

    def test_create_class_templates(self):
        self.project.create_class_templates()
        templates = [
            ".templates/class_header.template", ".templates/class_source.template", ".templates/class_tests.template"
        ]
        for template in templates:
            self.assert_project_directory_contains(template)

    def test_create_gitignore_file(self):
        self.project.create_gitignore_file()
        self.assert_project_directory_contains(".gitignore")

    def test_create_git_repository(self):
        self.project.create_git_repository()
        self.assert_directory_exists(self.path/".git")

    def test_create_license_file(self):
        self.project.create_license_file()
        self.assert_project_directory_contains("LICENSE.TXT")

    def test_create_license_header_template(self):
        self.project.create_license_header_template()
        self.assert_project_directory_contains(".templates/license_header.template")

    def test_create_readme_file(self):
        self.project.create_readme_file()
        self.assert_project_directory_contains("README.md")

    @classmethod
    def setUpClass(cls):
        cls.setup_base()
        cls.project.create_directory_structure()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()


class TestProjectWithLicenseHeaderTemplate(TestProjectTools):

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
        cls.setup_base()
        cls.project.create_directory_structure()
        cls.project.create_license_header_template()

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()


class TestProjectCreation(TestProjectTools):

    def test_create(self):
        self.project.create()
        self.assert_has_a_project_directory_structure()
        for file in self.expected_files:
            self.assert_project_directory_contains(file)
        for file in self.expected_files_with_header:
            self.assert_file_has_license_header(self.path/file)
        self.assert_directory_exists(self.path/".git")

    @classmethod
    def setUpClass(cls):
        cls.setup_base()
        cls.expected_files_with_header = ["CMakeLists.txt", "src/CMakeLists.txt"]
        cls.expected_files_templates = list(map(lambda name: ".templates/" + name + ".template", 
            ["license_header", "class_header", "class_source", "class_tests"]))
        cls.expected_files = (["LICENSE.TXT", "README.md", ".gitignore"]
            + cls.expected_files_with_header + cls.expected_files_templates)

    @classmethod
    def tearDownClass(cls):
        cls.tear_down_base()
