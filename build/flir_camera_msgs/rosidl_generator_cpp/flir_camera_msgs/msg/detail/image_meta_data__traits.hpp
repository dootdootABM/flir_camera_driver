// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice

#ifndef FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__TRAITS_HPP_
#define FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "flir_camera_msgs/msg/detail/image_meta_data__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace flir_camera_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ImageMetaData & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: camera_time
  {
    out << "camera_time: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_time, out);
    out << ", ";
  }

  // member: brightness
  {
    out << "brightness: ";
    rosidl_generator_traits::value_to_yaml(msg.brightness, out);
    out << ", ";
  }

  // member: exposure_time
  {
    out << "exposure_time: ";
    rosidl_generator_traits::value_to_yaml(msg.exposure_time, out);
    out << ", ";
  }

  // member: max_exposure_time
  {
    out << "max_exposure_time: ";
    rosidl_generator_traits::value_to_yaml(msg.max_exposure_time, out);
    out << ", ";
  }

  // member: gain
  {
    out << "gain: ";
    rosidl_generator_traits::value_to_yaml(msg.gain, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ImageMetaData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: camera_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "camera_time: ";
    rosidl_generator_traits::value_to_yaml(msg.camera_time, out);
    out << "\n";
  }

  // member: brightness
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "brightness: ";
    rosidl_generator_traits::value_to_yaml(msg.brightness, out);
    out << "\n";
  }

  // member: exposure_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exposure_time: ";
    rosidl_generator_traits::value_to_yaml(msg.exposure_time, out);
    out << "\n";
  }

  // member: max_exposure_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_exposure_time: ";
    rosidl_generator_traits::value_to_yaml(msg.max_exposure_time, out);
    out << "\n";
  }

  // member: gain
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gain: ";
    rosidl_generator_traits::value_to_yaml(msg.gain, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ImageMetaData & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace flir_camera_msgs

namespace rosidl_generator_traits
{

[[deprecated("use flir_camera_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const flir_camera_msgs::msg::ImageMetaData & msg,
  std::ostream & out, size_t indentation = 0)
{
  flir_camera_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use flir_camera_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const flir_camera_msgs::msg::ImageMetaData & msg)
{
  return flir_camera_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<flir_camera_msgs::msg::ImageMetaData>()
{
  return "flir_camera_msgs::msg::ImageMetaData";
}

template<>
inline const char * name<flir_camera_msgs::msg::ImageMetaData>()
{
  return "flir_camera_msgs/msg/ImageMetaData";
}

template<>
struct has_fixed_size<flir_camera_msgs::msg::ImageMetaData>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<flir_camera_msgs::msg::ImageMetaData>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<flir_camera_msgs::msg::ImageMetaData>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FLIR_CAMERA_MSGS__MSG__DETAIL__IMAGE_META_DATA__TRAITS_HPP_
