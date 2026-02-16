// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__STRUCT_H_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__STRUCT_H_

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

/// Struct defined in msg/ImageMetaData in the package flir_camera_msgs.
/**
  * meta data messages for camera images
 */
typedef struct flir_camera_msgs__msg__ImageMetaData
{
  std_msgs__msg__Header header;
  /// time stamp produced by camera, interpretation depends on camera model
  uint64_t camera_time;
  /// computed brightness, either 0...255 (valid) or -1 (invalid)
  int16_t brightness;
  /// exposure time in microseconds
  uint32_t exposure_time;
  /// max allowed exposure time in microseconds
  uint32_t max_exposure_time;
  /// gain in db
  float gain;
} flir_camera_msgs__msg__ImageMetaData;

// Struct for a sequence of flir_camera_msgs__msg__ImageMetaData.
typedef struct flir_camera_msgs__msg__ImageMetaData__Sequence
{
  flir_camera_msgs__msg__ImageMetaData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} flir_camera_msgs__msg__ImageMetaData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__STRUCT_H_
