// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__FUNCTIONS_H_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "flir_camera_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "flir_camera_msgs/msg/detail/image_meta_data__struct.h"

/// Initialize msg/ImageMetaData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * flir_camera_msgs__msg__ImageMetaData
 * )) before or use
 * flir_camera_msgs__msg__ImageMetaData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__init(flir_camera_msgs__msg__ImageMetaData * msg);

/// Finalize msg/ImageMetaData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
void
flir_camera_msgs__msg__ImageMetaData__fini(flir_camera_msgs__msg__ImageMetaData * msg);

/// Create msg/ImageMetaData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * flir_camera_msgs__msg__ImageMetaData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
flir_camera_msgs__msg__ImageMetaData *
flir_camera_msgs__msg__ImageMetaData__create();

/// Destroy msg/ImageMetaData message.
/**
 * It calls
 * flir_camera_msgs__msg__ImageMetaData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
void
flir_camera_msgs__msg__ImageMetaData__destroy(flir_camera_msgs__msg__ImageMetaData * msg);

/// Check for msg/ImageMetaData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__are_equal(const flir_camera_msgs__msg__ImageMetaData * lhs, const flir_camera_msgs__msg__ImageMetaData * rhs);

/// Copy a msg/ImageMetaData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__copy(
  const flir_camera_msgs__msg__ImageMetaData * input,
  flir_camera_msgs__msg__ImageMetaData * output);

/// Initialize array of msg/ImageMetaData messages.
/**
 * It allocates the memory for the number of elements and calls
 * flir_camera_msgs__msg__ImageMetaData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__Sequence__init(flir_camera_msgs__msg__ImageMetaData__Sequence * array, size_t size);

/// Finalize array of msg/ImageMetaData messages.
/**
 * It calls
 * flir_camera_msgs__msg__ImageMetaData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
void
flir_camera_msgs__msg__ImageMetaData__Sequence__fini(flir_camera_msgs__msg__ImageMetaData__Sequence * array);

/// Create array of msg/ImageMetaData messages.
/**
 * It allocates the memory for the array and calls
 * flir_camera_msgs__msg__ImageMetaData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
flir_camera_msgs__msg__ImageMetaData__Sequence *
flir_camera_msgs__msg__ImageMetaData__Sequence__create(size_t size);

/// Destroy array of msg/ImageMetaData messages.
/**
 * It calls
 * flir_camera_msgs__msg__ImageMetaData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
void
flir_camera_msgs__msg__ImageMetaData__Sequence__destroy(flir_camera_msgs__msg__ImageMetaData__Sequence * array);

/// Check for msg/ImageMetaData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__Sequence__are_equal(const flir_camera_msgs__msg__ImageMetaData__Sequence * lhs, const flir_camera_msgs__msg__ImageMetaData__Sequence * rhs);

/// Copy an array of msg/ImageMetaData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_flir_camera_msgs
bool
flir_camera_msgs__msg__ImageMetaData__Sequence__copy(
  const flir_camera_msgs__msg__ImageMetaData__Sequence * input,
  flir_camera_msgs__msg__ImageMetaData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__FUNCTIONS_H_
