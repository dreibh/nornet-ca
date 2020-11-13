# MELODIC/NorNet Build Scripts
# Copyright (C) 2017-2020 by Thomas Dreibholz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact: dreibh@simula.no

CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
PROJECT(nornet-ca C)

SET(BUILD_MAJOR "1")
SET(BUILD_MINOR "1")
SET(BUILD_PATCH "8")
SET(BUILD_VERSION ${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH})


#############################################################################
# INSTALLATION_DIRECTORIES
#############################################################################

# See: https://cmake.org/cmake/help/v3.0/module/GNUInstallDirs.html
INCLUDE(GNUInstallDirs)


#############################################################################
# PACKAGING
#############################################################################

# NOTE: Tar/GZip build necessary for Ubuntu Precise (no support for Tar/XZ!)
SET(CPACK_SOURCE_GENERATOR "TGZ")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME
   "${CMAKE_PROJECT_NAME}-${BUILD_MAJOR}.${BUILD_MINOR}.${BUILD_PATCH}")
SET(CPACK_SOURCE_IGNORE_FILES
   "${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}-*;${PROJECT_SOURCE_DIR}/${CMAKE_PROJECT_NAME}_*;/build/;/.git/;.gitmodules$;/.gimp/;/config.log;/CMakeFiles/;CMakeCache.txt$;.cmake$;.tar.gz$;/_CPack_Packages;/Makefile$;~$;/build-deb;/clean-deb;setup.py$")
INCLUDE(CPack)

ADD_CUSTOM_TARGET(dist COMMAND ${CMAKE_MAKE_PROGRAM} clean package_source)


#############################################################################
# SOURCE DIRECTORIES
#############################################################################

ADD_SUBDIRECTORY(src)
