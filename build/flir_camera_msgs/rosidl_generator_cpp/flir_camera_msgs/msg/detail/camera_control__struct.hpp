// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from flir_camera_msgs:msg/CameraControl.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_HPP_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__flir_camera_msgs__msg__CameraControl __attribute__((deprecated))
#else
# define DEPRECATED__flir_camera_msgs__msg__CameraControl __declspec(deprecated)
#endif

namespace flir_camera_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CameraControl_
{
  using Type = CameraControl_<ContainerAllocator>;

  explicit CameraControl_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->exposure_time = 0ul;
      this->gain = 0.0f;
    }
  }

  explicit CameraControl_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->exposure_time = 0ul;
      this->gain = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _exposure_time_type =
    uint32_t;
  _exposure_time_type exposure_time;
  using _gain_type =
    float;
  _gain_type gain;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__exposure_time(
    const uint32_t & _arg)
  {
    this->exposure_time = _arg;
    return *this;
  }
  Type & set__gain(
    const float & _arg)
  {
    this->gain = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    flir_camera_msgs::msg::CameraControl_<ContainerAllocator> *;
  using ConstRawPtr =
    const flir_camera_msgs::msg::CameraControl_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      flir_camera_msgs::msg::CameraControl_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      flir_camera_msgs::msg::CameraControl_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__flir_camera_msgs__msg__CameraControl
    std::shared_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__flir_camera_msgs__msg__CameraControl
    std::shared_ptr<flir_camera_msgs::msg::CameraControl_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CameraControl_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->exposure_time != other.exposure_time) {
      return false;
    }
    if (this->gain != other.gain) {
      return false;
    }
    return true;
  }
  bool operator!=(const CameraControl_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CameraControl_

// alias to use template instance with default allocator
using CameraControl =
  flir_camera_msgs::msg::CameraControl_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace flir_camera_msgs

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__STRUCT_HPP_
