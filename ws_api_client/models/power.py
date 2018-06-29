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


class Power(object):
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
        'ps': 'float',
        'hp': 'float',
        'k_w': 'float'
    }

    attribute_map = {
        'ps': 'PS',
        'hp': 'hp',
        'k_w': 'kW'
    }

    def __init__(self, ps=None, hp=None, k_w=None):  # noqa: E501
        """Power - a model defined in Swagger"""  # noqa: E501

        self._ps = None
        self._hp = None
        self._k_w = None
        self.discriminator = None

        if ps is not None:
            self.ps = ps
        if hp is not None:
            self.hp = hp
        if k_w is not None:
            self.k_w = k_w

    @property
    def ps(self):
        """Gets the ps of this Power.  # noqa: E501

        Power, PS (e.g. `169`)  # noqa: E501

        :return: The ps of this Power.  # noqa: E501
        :rtype: float
        """
        return self._ps

    @ps.setter
    def ps(self, ps):
        """Sets the ps of this Power.

        Power, PS (e.g. `169`)  # noqa: E501

        :param ps: The ps of this Power.  # noqa: E501
        :type: float
        """

        self._ps = ps

    @property
    def hp(self):
        """Gets the hp of this Power.  # noqa: E501

        Power, hp (e.g. `166`)  # noqa: E501

        :return: The hp of this Power.  # noqa: E501
        :rtype: float
        """
        return self._hp

    @hp.setter
    def hp(self, hp):
        """Sets the hp of this Power.

        Power, hp (e.g. `166`)  # noqa: E501

        :param hp: The hp of this Power.  # noqa: E501
        :type: float
        """

        self._hp = hp

    @property
    def k_w(self):
        """Gets the k_w of this Power.  # noqa: E501

        Power, kW (e.g. `124`)  # noqa: E501

        :return: The k_w of this Power.  # noqa: E501
        :rtype: float
        """
        return self._k_w

    @k_w.setter
    def k_w(self, k_w):
        """Sets the k_w of this Power.

        Power, kW (e.g. `124`)  # noqa: E501

        :param k_w: The k_w of this Power.  # noqa: E501
        :type: float
        """

        self._k_w = k_w

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
        if not isinstance(other, Power):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
