# Find LibIrrXML headers and library
#
#   IRRXML_INCLUDE_DIR    - Headers location
#   IRRXML_LIBRARY        - IrrXML main library

find_path(IRRXML_INCLUDE_DIR irrXML.h)
find_library(IRRXML_LIBRARY NAMES IrrXML IrrXMLd)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(IrrXML REQUIRED_VARS IRRXML_INCLUDE_DIR IRRXML_LIBRARY)

mark_as_advanced(IRRXML_INCLUDE_DIR IRRXML_LIBRARY)