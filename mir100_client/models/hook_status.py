# coding: utf-8

"""
    MIR100 Rest Interface

    Automatically converted from v270 pdf  # noqa: E501

    OpenAPI spec version: 2.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from mir100_client.models.cart import Cart  # noqa: F401,E501


class HookStatus(object):
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
        'angle': 'float',
        'available': 'bool',
        'braked': 'bool',
        'cart': 'Cart',
        'cart_attached': 'bool',
        'height': 'float',
        'length': 'float'
    }

    attribute_map = {
        'angle': 'angle',
        'available': 'available',
        'braked': 'braked',
        'cart': 'cart',
        'cart_attached': 'cart_attached',
        'height': 'height',
        'length': 'length'
    }

    def __init__(self, angle=None, available=None, braked=None, cart=None, cart_attached=None, height=None, length=None):  # noqa: E501
        """HookStatus - a model defined in Swagger"""  # noqa: E501
        self._angle = None
        self._available = None
        self._braked = None
        self._cart = None
        self._cart_attached = None
        self._height = None
        self._length = None
        self.discriminator = None
        if angle is not None:
            self.angle = angle
        if available is not None:
            self.available = available
        if braked is not None:
            self.braked = braked
        if cart is not None:
            self.cart = cart
        if cart_attached is not None:
            self.cart_attached = cart_attached
        if height is not None:
            self.height = height
        if length is not None:
            self.length = length

    @property
    def angle(self):
        """Gets the angle of this HookStatus.  # noqa: E501

        The current angle of the hook  # noqa: E501

        :return: The angle of this HookStatus.  # noqa: E501
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this HookStatus.

        The current angle of the hook  # noqa: E501

        :param angle: The angle of this HookStatus.  # noqa: E501
        :type: float
        """

        self._angle = angle

    @property
    def available(self):
        """Gets the available of this HookStatus.  # noqa: E501

        Boolean indicating if the hook available on this robot  # noqa: E501

        :return: The available of this HookStatus.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this HookStatus.

        Boolean indicating if the hook available on this robot  # noqa: E501

        :param available: The available of this HookStatus.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def braked(self):
        """Gets the braked of this HookStatus.  # noqa: E501

        Boolean indicating if the hook brake is activated  # noqa: E501

        :return: The braked of this HookStatus.  # noqa: E501
        :rtype: bool
        """
        return self._braked

    @braked.setter
    def braked(self, braked):
        """Sets the braked of this HookStatus.

        Boolean indicating if the hook brake is activated  # noqa: E501

        :param braked: The braked of this HookStatus.  # noqa: E501
        :type: bool
        """

        self._braked = braked

    @property
    def cart(self):
        """Gets the cart of this HookStatus.  # noqa: E501


        :return: The cart of this HookStatus.  # noqa: E501
        :rtype: Cart
        """
        return self._cart

    @cart.setter
    def cart(self, cart):
        """Sets the cart of this HookStatus.


        :param cart: The cart of this HookStatus.  # noqa: E501
        :type: Cart
        """

        self._cart = cart

    @property
    def cart_attached(self):
        """Gets the cart_attached of this HookStatus.  # noqa: E501

        Boolean indicating if a trolley is currently attached  # noqa: E501

        :return: The cart_attached of this HookStatus.  # noqa: E501
        :rtype: bool
        """
        return self._cart_attached

    @cart_attached.setter
    def cart_attached(self, cart_attached):
        """Sets the cart_attached of this HookStatus.

        Boolean indicating if a trolley is currently attached  # noqa: E501

        :param cart_attached: The cart_attached of this HookStatus.  # noqa: E501
        :type: bool
        """

        self._cart_attached = cart_attached

    @property
    def height(self):
        """Gets the height of this HookStatus.  # noqa: E501

        The current height of the hook  # noqa: E501

        :return: The height of this HookStatus.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this HookStatus.

        The current height of the hook  # noqa: E501

        :param height: The height of this HookStatus.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def length(self):
        """Gets the length of this HookStatus.  # noqa: E501

        The length of the hook  # noqa: E501

        :return: The length of this HookStatus.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this HookStatus.

        The length of the hook  # noqa: E501

        :param length: The length of this HookStatus.  # noqa: E501
        :type: float
        """

        self._length = length

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
        if issubclass(HookStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HookStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other