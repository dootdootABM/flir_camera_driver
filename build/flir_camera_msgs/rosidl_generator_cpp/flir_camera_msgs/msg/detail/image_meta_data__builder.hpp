// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__BUILDER_HPP_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "flir_camera_msgs/msg/detail/image_meta_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace flir_camera_msgs
{

namespace msg
{

namespace builder
{

class Init_ImageMetaData_gain
{
public:
  explicit Init_ImageMetaData_gain(::flir_camera_msgs::msg::ImageMetaData & msg)
  : msg_(msg)
  {}
  ::flir_camera_msgs::msg::ImageMetaData gain(::flir_camera_msgs::msg::ImageMetaData::_gain_type arg)
  {
    msg_.gain = std::move(arg);
    return std::move(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

class Init_ImageMetaData_max_exposure_time
{
public:
  explicit Init_ImageMetaData_max_exposure_time(::flir_camera_msgs::msg::ImageMetaData & msg)
  : msg_(msg)
  {}
  Init_ImageMetaData_gain max_exposure_time(::flir_camera_msgs::msg::ImageMetaData::_max_exposure_time_type arg)
  {
    msg_.max_exposure_time = std::move(arg);
    return Init_ImageMetaData_gain(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

class Init_ImageMetaData_exposure_time
{
public:
  explicit Init_ImageMetaData_exposure_time(::flir_camera_msgs::msg::ImageMetaData & msg)
  : msg_(msg)
  {}
  Init_ImageMetaData_max_exposure_time exposure_time(::flir_camera_msgs::msg::ImageMetaData::_exposure_time_type arg)
  {
    msg_.exposure_time = std::move(arg);
    return Init_ImageMetaData_max_exposure_time(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

class Init_ImageMetaData_brightness
{
public:
  explicit Init_ImageMetaData_brightness(::flir_camera_msgs::msg::ImageMetaData & msg)
  : msg_(msg)
  {}
  Init_ImageMetaData_exposure_time brightness(::flir_camera_msgs::msg::ImageMetaData::_brightness_type arg)
  {
    msg_.brightness = std::move(arg);
    return Init_ImageMetaData_exposure_time(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

class Init_ImageMetaData_camera_time
{
public:
  explicit Init_ImageMetaData_camera_time(::flir_camera_msgs::msg::ImageMetaData & msg)
  : msg_(msg)
  {}
  Init_ImageMetaData_brightness camera_time(::flir_camera_msgs::msg::ImageMetaData::_camera_time_type arg)
  {
    msg_.camera_time = std::move(arg);
    return Init_ImageMetaData_brightness(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

class Init_ImageMetaData_header
{
public:
  Init_ImageMetaData_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImageMetaData_camera_time header(::flir_camera_msgs::msg::ImageMetaData::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ImageMetaData_camera_time(msg_);
  }

private:
  ::flir_camera_msgs::msg::ImageMetaData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::flir_camera_msgs::msg::ImageMetaData>()
{
  return flir_camera_msgs::msg::builder::Init_ImageMetaData_header();
}

}  // namespace flir_camera_msgs

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__BUILDER_HPP_
