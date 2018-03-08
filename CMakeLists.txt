project(irrxml)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set( IrrXML_SRCS
  sources/src/CXMLReaderImpl.h
  sources/src/heapsort.h
  sources/src/irrArray.h
  sources/src/irrString.h
  sources/src/irrTypes.h
  sources/src/irrXML.cpp
  sources/src/irrXML.h
)

if ( MSVC )
  ADD_DEFINITIONS( -D_SCL_SECURE_NO_WARNINGS )
  ADD_DEFINITIONS( -D_CRT_SECURE_NO_WARNINGS )
endif ( MSVC )

add_library(IrrXML ${IrrXML_SRCS})
