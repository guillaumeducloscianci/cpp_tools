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


## Create a new class

Make sure you have created a project with the `cpp_tools create project` command.
Move to your project directory.

`cpp_tools create class --name YourClassName`

Note that this command creates a header, source and tests files. The test file contains a failing test. Also the source and tests files are automatically added to your CMakeLists.txt file.

At this point you can build your project. The project should build, but the tests fail.

`cd build`
`cmake ..`
`make all test`


## Create a new interface (abstract class)

Make sure you have created a project with the `cpp_tools create project` command.
Move to your project directory.

`cpp_tools create interface --name YourInterfaceName`

Note that this commands creates an header file containing a virtual destructor and a commented pure virtual function.


## Create a new implementation

Make sure you have created a project with the `cpp_tools create project` command and an interface with the `cpp_tools create interface` command. Also make sure some pure virtual functions were added to your interface.
Move to your project directory.

`cpp_tools create implementation --name YourImplementationName --interface YourInterfaceName`

Note that this command creates a header, source and tests files. The header file contains an overriden method for each pure virtual functions of the interface. The source and tests files contain relevant commented code for each pure virtual function.
