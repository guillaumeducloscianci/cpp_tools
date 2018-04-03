# cpp_tools

`cpp_tools` is a lightweight Python program used to facilitate and speed up development in C++. The syntax of commands is git-like, using sub-commands. Examples follow. It is intended to be especially useful for kata practice.


## Installation

The main script is `src/cpp_tools.py`. There are two simple ways to install this project.

First, clone the repository to your machine.

`git clone https://github.com/guillaumeducloscianci/cpp_tools.git`

Second, either create a symbolic link named `cpp_tools` in a directory that is part of your $PATH variable

`ln -s /ClonedRepositoryPath/cpp_tools/src/cpp_tools.py cpp_tools`

or either create an alias in your `.bashrc` file by adding the following line to `~/.bashrc`

`alias cpp_tools=/ClonedRepositoryPath/cpp_tools/src/cpp_tools.py`


## Create a new project

*cpp_tools* enables the automatic creation of a C++ project with a given directory structure, initializing a *git* repository, a *CMake* build system and *GPL_v3* license header.

`cpp_tools create project --name YourProjectName --author 'Your Name'`

Note: The project will be created in your current directory. However, you can specificy an absolute path and the project name will be deduced from the last directory entry.

`cpp_tools create project --name /absolute/path/YourProjectName --author 'Your Name'`
