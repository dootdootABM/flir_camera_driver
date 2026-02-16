// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from flir_camera_msgs:msg/CameraControl.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__BUILDER_HPP_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "flir_camera_msgs/msg/detail/camera_control__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace flir_camera_msgs
{

namespace msg
{

namespace builder
{

class Init_CameraControl_gain
{
public:
  explicit Init_CameraControl_gain(::flir_camera_msgs::msg::CameraControl & msg)
  : msg_(msg)
  {}
  ::flir_camera_msgs::msg::CameraControl gain(::flir_camera_msgs::msg::CameraControl::_gain_type arg)
  {
    msg_.gain = std::move(arg);
    return std::move(msg_);
  }

private:
  ::flir_camera_msgs::msg::CameraControl msg_;
};

class Init_CameraControl_exposure_time
{
public:
  explicit Init_CameraControl_exposure_time(::flir_camera_msgs::msg::CameraControl & msg)
  : msg_(msg)
  {}
  Init_CameraControl_gain exposure_time(::flir_camera_msgs::msg::CameraControl::_exposure_time_type arg)
  {
    msg_.exposure_time = std::move(arg);
    return Init_CameraControl_gain(msg_);
  }

private:
  ::flir_camera_msgs::msg::CameraControl msg_;
};

class Init_CameraControl_header
{
public:
  Init_CameraControl_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CameraControl_exposure_time header(::flir_camera_msgs::msg::CameraControl::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_CameraControl_exposure_time(msg_);
  }

private:
  ::flir_camera_msgs::msg::CameraControl msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::flir_camera_msgs::msg::CameraControl>()
{
  return flir_camera_msgs::msg::builder::Init_CameraControl_header();
}

}  // namespace flir_camera_msgs

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__CAMERA_CONTROL__BUILDER_HPP_
