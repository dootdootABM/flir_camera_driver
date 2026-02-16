// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from flir_camera_msgs:msg/CameraControl.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_H_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/CameraControl in the package flir_camera_msgs.
/**
  * camera control message
 */
typedef struct flir_camera_msgs__msg__CameraControl
{
  std_msgs__msg__Header header;
  /// set exposure time in microseconds
  uint32_t exposure_time;
  /// set gain in db
  float gain;
} flir_camera_msgs__msg__CameraControl;

// Struct for a sequence of flir_camera_msgs__msg__CameraControl.
typedef struct flir_camera_msgs__msg__CameraControl__Sequence
{
  flir_camera_msgs__msg__CameraControl * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} flir_camera_msgs__msg__CameraControl__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_H_
