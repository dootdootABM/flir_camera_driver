// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from flir_camera_msgs:msg/ImageMetaData.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "flir_camera_msgs/msg/detail/image_meta_data__struct.h"
#include "flir_camera_msgs/msg/detail/image_meta_data__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool flir_camera_msgs__msg__image_meta_data__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[52];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("flir_camera_msgs.msg._image_meta_data.ImageMetaData", full_classname_dest, 51) == 0);
  }
  flir_camera_msgs__msg__ImageMetaData * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // camera_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "camera_time");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->camera_time = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // brightness
    PyObject * field = PyObject_GetAttrString(_pymsg, "brightness");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->brightness = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // exposure_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "exposure_time");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->exposure_time = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // max_exposure_time
    PyObject * field = PyObject_GetAttrString(_pymsg, "max_exposure_time");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->max_exposure_time = PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // gain
    PyObject * field = PyObject_GetAttrString(_pymsg, "gain");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->gain = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * flir_camera_msgs__msg__image_meta_data__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ImageMetaData */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("flir_camera_msgs.msg._image_meta_data");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ImageMetaData");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  flir_camera_msgs__msg__ImageMetaData * ros_message = (flir_camera_msgs__msg__ImageMetaData *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // camera_time
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->camera_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "camera_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // brightness
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->brightness);
    {
      int rc = PyObject_SetAttrString(_pymessage, "brightness", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exposure_time
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->exposure_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exposure_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // max_exposure_time
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->max_exposure_time);
    {
      int rc = PyObject_SetAttrString(_pymessage, "max_exposure_time", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // gain
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->gain);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gain", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
