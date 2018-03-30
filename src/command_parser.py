# `cpp_tools` is a set of lightweight python scripts used to facilitate and greatly speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

import argparse
import sys

from command_create_project import CommandCreateProject, ProjectParameters


class CommandParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="cpp_tools, a c++ development tool.")
        subparsers = self.parser.add_subparsers()
        self.add_create_project_parser(subparsers)

    def add_create_project_parser(self, subparsers):
        parser_create = subparsers.add_parser("create")
        subparsers_create = parser_create.add_subparsers()
        parser_create_project = subparsers_create.add_parser("project")
        parser_create_project.add_argument("--name", type=str)
        parser_create_project.add_argument("--author", type=str)
        parser_create_project.set_defaults(
            func=lambda args: CommandCreateProject(ProjectParameters(args.name, args.author)))

    def parse(self, arguments=sys.argv[1:]):
        args = self.parser.parse_args(arguments)
        return args.func(args)
