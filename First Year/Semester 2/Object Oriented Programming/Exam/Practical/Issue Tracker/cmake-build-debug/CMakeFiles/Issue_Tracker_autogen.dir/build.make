# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker\cmake-build-debug"

# Utility rule file for Issue_Tracker_autogen.

# Include the progress variables for this target.
include CMakeFiles/Issue_Tracker_autogen.dir/progress.make

CMakeFiles/Issue_Tracker_autogen:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir="D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC and UIC for target Issue_Tracker"
	"D:\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe" -E cmake_autogen "D:/Desktop Folders/Facultate/Sem 2/Object Oriented Programming/Exam/Practical/Issue Tracker/cmake-build-debug/CMakeFiles/Issue_Tracker_autogen.dir/AutogenInfo.json" Debug

Issue_Tracker_autogen: CMakeFiles/Issue_Tracker_autogen
Issue_Tracker_autogen: CMakeFiles/Issue_Tracker_autogen.dir/build.make

.PHONY : Issue_Tracker_autogen

# Rule to build all files generated by this target.
CMakeFiles/Issue_Tracker_autogen.dir/build: Issue_Tracker_autogen

.PHONY : CMakeFiles/Issue_Tracker_autogen.dir/build

CMakeFiles/Issue_Tracker_autogen.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Issue_Tracker_autogen.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Issue_Tracker_autogen.dir/clean

CMakeFiles/Issue_Tracker_autogen.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker" "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker" "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker\cmake-build-debug" "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker\cmake-build-debug" "D:\Desktop Folders\Facultate\Sem 2\Object Oriented Programming\Exam\Practical\Issue Tracker\cmake-build-debug\CMakeFiles\Issue_Tracker_autogen.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Issue_Tracker_autogen.dir/depend
