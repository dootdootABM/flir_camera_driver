#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "spinnaker_camera_driver::camera_driver" for configuration "RelWithDebInfo"
set_property(TARGET spinnaker_camera_driver::camera_driver APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(spinnaker_camera_driver::camera_driver PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libcamera_driver.so"
  IMPORTED_SONAME_RELWITHDEBINFO "libcamera_driver.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS spinnaker_camera_driver::camera_driver )
list(APPEND _IMPORT_CHECK_FILES_FOR_spinnaker_camera_driver::camera_driver "${_IMPORT_PREFIX}/lib/libcamera_driver.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
