# generated from rosidl_generator_py/resource/_idl.py.em
# with input from flir_camera_msgs:msg/ImageMetaData.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ImageMetaData(type):
    """Metaclass of message 'ImageMetaData'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('flir_camera_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'flir_camera_msgs.msg.ImageMetaData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__image_meta_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__image_meta_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__image_meta_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__image_meta_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__image_meta_data

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ImageMetaData(metaclass=Metaclass_ImageMetaData):
    """Message class 'ImageMetaData'."""

    __slots__ = [
        '_header',
        '_camera_time',
        '_brightness',
        '_exposure_time',
        '_max_exposure_time',
        '_gain',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'camera_time': 'uint64',
        'brightness': 'int16',
        'exposure_time': 'uint32',
        'max_exposure_time': 'uint32',
        'gain': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.camera_time = kwargs.get('camera_time', int())
        self.brightness = kwargs.get('brightness', int())
        self.exposure_time = kwargs.get('exposure_time', int())
        self.max_exposure_time = kwargs.get('max_exposure_time', int())
        self.gain = kwargs.get('gain', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.header != other.header:
            return False
        if self.camera_time != other.camera_time:
            return False
        if self.brightness != other.brightness:
            return False
        if self.exposure_time != other.exposure_time:
            return False
        if self.max_exposure_time != other.max_exposure_time:
            return False
        if self.gain != other.gain:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def camera_time(self):
        """Message field 'camera_time'."""
        return self._camera_time

    @camera_time.setter
    def camera_time(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'camera_time' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'camera_time' field must be an unsigned integer in [0, 18446744073709551615]"
        self._camera_time = value

    @builtins.property
    def brightness(self):
        """Message field 'brightness'."""
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'brightness' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'brightness' field must be an integer in [-32768, 32767]"
        self._brightness = value

    @builtins.property
    def exposure_time(self):
        """Message field 'exposure_time'."""
        return self._exposure_time

    @exposure_time.setter
    def exposure_time(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'exposure_time' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'exposure_time' field must be an unsigned integer in [0, 4294967295]"
        self._exposure_time = value

    @builtins.property
    def max_exposure_time(self):
        """Message field 'max_exposure_time'."""
        return self._max_exposure_time

    @max_exposure_time.setter
    def max_exposure_time(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'max_exposure_time' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'max_exposure_time' field must be an unsigned integer in [0, 4294967295]"
        self._max_exposure_time = value

    @builtins.property
    def gain(self):
        """Message field 'gain'."""
        return self._gain

    @gain.setter
    def gain(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'gain' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'gain' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._gain = value
