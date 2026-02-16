// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "flir_camera_msgs/msg/detail/image_meta_data__rosidl_typesupport_introspection_c.h"
#include "flir_camera_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "flir_camera_msgs/msg/detail/image_meta_data__functions.h"
#include "flir_camera_msgs/msg/detail/image_meta_data__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  flir_camera_msgs__msg__ImageMetaData__init(message_memory);
}

void flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_fini_function(void * message_memory)
{
  flir_camera_msgs__msg__ImageMetaData__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_member_array[6] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "camera_time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, camera_time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "brightness",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, brightness),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "exposure_time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, exposure_time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "max_exposure_time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, max_exposure_time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "gain",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(flir_camera_msgs__msg__ImageMetaData, gain),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_members = {
  "flir_camera_msgs__msg",  // message namespace
  "ImageMetaData",  // message name
  6,  // number of fields
  sizeof(flir_camera_msgs__msg__ImageMetaData),
  flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_member_array,  // message members
  flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_init_function,  // function to initialize message memory (memory has to be allocated)
  flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_type_support_handle = {
  0,
  &flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_flir_camera_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, flir_camera_msgs, msg, ImageMetaData)() {
  flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_type_support_handle.typesupport_identifier) {
    flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &flir_camera_msgs__msg__ImageMetaData__rosidl_typesupport_introspection_c__ImageMetaData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
