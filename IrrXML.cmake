set(IrrXML_LIBRARY_NAME IrrXML)

set(SOURCES
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

if(NOT CMAKE_DEBUG_POSTFIX)
  set(CMAKE_DEBUG_POSTFIX d)
endif()

add_library(${IrrXML_LIBRARY_NAME} ${SOURCES})

set_target_properties(${IrrXML_LIBRARY_NAME} PROPERTIES
    PUBLIC_HEADER sources/src/irrXML.h)

install(TARGETS ${IrrXML_LIBRARY_NAME}
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
    PUBLIC_HEADER DESTINATION include)
