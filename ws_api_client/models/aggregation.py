# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Aggregation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min': 'float',
        'max': 'float',
        'units': 'str'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'units': 'units'
    }

    def __init__(self, min=None, max=None, units=None):  # noqa: E501
        """Aggregation - a model defined in Swagger"""  # noqa: E501

        self._min = None
        self._max = None
        self._units = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if units is not None:
            self.units = units

    @property
    def min(self):
        """Gets the min of this Aggregation.  # noqa: E501

        Min aggregated value  # noqa: E501

        :return: The min of this Aggregation.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this Aggregation.

        Min aggregated value  # noqa: E501

        :param min: The min of this Aggregation.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this Aggregation.  # noqa: E501

        Max aggregated value  # noqa: E501

        :return: The max of this Aggregation.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Aggregation.

        Max aggregated value  # noqa: E501

        :param max: The max of this Aggregation.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def units(self):
        """Gets the units of this Aggregation.  # noqa: E501

        One of `mm, in, %`  # noqa: E501

        :return: The units of this Aggregation.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Aggregation.

        One of `mm, in, %`  # noqa: E501

        :param units: The units of this Aggregation.  # noqa: E501
        :type: str
        """

        self._units = units

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Aggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
