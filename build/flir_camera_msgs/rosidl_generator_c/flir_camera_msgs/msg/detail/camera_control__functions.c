// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from flir_camera_msgs:msg/CameraControl.idl
// generated code does not contain a copyright notice
#include "flir_camera_msgs/msg/detail/camera_control__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
flir_camera_msgs__msg__CameraControl__init(flir_camera_msgs__msg__CameraControl * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    flir_camera_msgs__msg__CameraControl__fini(msg);
    return false;
  }
  // exposure_time
  // gain
  return true;
}

void
flir_camera_msgs__msg__CameraControl__fini(flir_camera_msgs__msg__CameraControl * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // exposure_time
  // gain
}

bool
flir_camera_msgs__msg__CameraControl__are_equal(const flir_camera_msgs__msg__CameraControl * lhs, const flir_camera_msgs__msg__CameraControl * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // exposure_time
  if (lhs->exposure_time != rhs->exposure_time) {
    return false;
  }
  // gain
  if (lhs->gain != rhs->gain) {
    return false;
  }
  return true;
}

bool
flir_camera_msgs__msg__CameraControl__copy(
  const flir_camera_msgs__msg__CameraControl * input,
  flir_camera_msgs__msg__CameraControl * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // exposure_time
  output->exposure_time = input->exposure_time;
  // gain
  output->gain = input->gain;
  return true;
}

flir_camera_msgs__msg__CameraControl *
flir_camera_msgs__msg__CameraControl__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  flir_camera_msgs__msg__CameraControl * msg = (flir_camera_msgs__msg__CameraControl *)allocator.allocate(sizeof(flir_camera_msgs__msg__CameraControl), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(flir_camera_msgs__msg__CameraControl));
  bool success = flir_camera_msgs__msg__CameraControl__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
flir_camera_msgs__msg__CameraControl__destroy(flir_camera_msgs__msg__CameraControl * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    flir_camera_msgs__msg__CameraControl__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
flir_camera_msgs__msg__CameraControl__Sequence__init(flir_camera_msgs__msg__CameraControl__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  flir_camera_msgs__msg__CameraControl * data = NULL;

  if (size) {
    data = (flir_camera_msgs__msg__CameraControl *)allocator.zero_allocate(size, sizeof(flir_camera_msgs__msg__CameraControl), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = flir_camera_msgs__msg__CameraControl__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        flir_camera_msgs__msg__CameraControl__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
flir_camera_msgs__msg__CameraControl__Sequence__fini(flir_camera_msgs__msg__CameraControl__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      flir_camera_msgs__msg__CameraControl__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

flir_camera_msgs__msg__CameraControl__Sequence *
flir_camera_msgs__msg__CameraControl__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  flir_camera_msgs__msg__CameraControl__Sequence * array = (flir_camera_msgs__msg__CameraControl__Sequence *)allocator.allocate(sizeof(flir_camera_msgs__msg__CameraControl__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = flir_camera_msgs__msg__CameraControl__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
flir_camera_msgs__msg__CameraControl__Sequence__destroy(flir_camera_msgs__msg__CameraControl__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    flir_camera_msgs__msg__CameraControl__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
flir_camera_msgs__msg__CameraControl__Sequence__are_equal(const flir_camera_msgs__msg__CameraControl__Sequence * lhs, const flir_camera_msgs__msg__CameraControl__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!flir_camera_msgs__msg__CameraControl__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
flir_camera_msgs__msg__CameraControl__Sequence__copy(
  const flir_camera_msgs__msg__CameraControl__Sequence * input,
  flir_camera_msgs__msg__CameraControl__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(flir_camera_msgs__msg__CameraControl);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    flir_camera_msgs__msg__CameraControl * data =
      (flir_camera_msgs__msg__CameraControl *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!flir_camera_msgs__msg__CameraControl__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          flir_camera_msgs__msg__CameraControl__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!flir_camera_msgs__msg__CameraControl__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
