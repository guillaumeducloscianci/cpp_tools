#!/usr/bin/env python3

# `cpp_tools` is a set of lightweight python scripts used to facilitate and speed up development in C++.
# Copyright (C) 2018 Guillaume Duclos-Cianci

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with this program.
# If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path
import os
import subprocess

from file import File
from system_test import SystemTest

cpp_tools = str(Path(__file__).resolve().with_name("cpp_tools.py"))

def main():
    SystemTest.clean_testing_directory()
    os.chdir(str(Path(__file__).resolve().parents[1]/"testing"))
    subprocess.run(
        [cpp_tools, "create", "project", "--name", "ToricCodeDecoder", "--author", "Guillaume Duclos-Cianci"])
    os.chdir(str(Path(".").resolve()/"ToricCodeDecoder"))
    subprocess.run([cpp_tools, "create", "class", "--name", "Syndrome"])
    create_interface()
    subprocess.run([cpp_tools, "create", "implementation", "--name", "UnitCell2X2", "--interface", "UnitCell"])

def create_interface():
    subprocess.run([cpp_tools, "create", "interface", "--name", "UnitCell"])
    path = Path(".").resolve()/"include/ToricCodeDecoder/UnitCell.h"
    content = File.read(path)
    content = content.replace("//virtual return_type_ method_name_(input_type_) = 0;",
        "double computeMarginalProbability(const unsigned qubitIndex);")
    File.overwrite(path, content)

if __name__ == '__main__':
    main()