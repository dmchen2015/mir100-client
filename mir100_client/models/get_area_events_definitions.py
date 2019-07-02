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


class GetAreaEventsDefinitions(object):
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
        'actions': 'str',
        'color': 'str',
        'id': 'int',
        'image': 'str',
        'legacy_name': 'str',
        'name': 'str'
    }

    attribute_map = {
        'actions': 'actions',
        'color': 'color',
        'id': 'id',
        'image': 'image',
        'legacy_name': 'legacyName',
        'name': 'name'
    }

    def __init__(self, actions=None, color=None, id=None, image=None, legacy_name=None, name=None):  # noqa: E501
        """GetAreaEventsDefinitions - a model defined in Swagger"""  # noqa: E501
        self._actions = None
        self._color = None
        self._id = None
        self._image = None
        self._legacy_name = None
        self._name = None
        self.discriminator = None
        if actions is not None:
            self.actions = actions
        if color is not None:
            self.color = color
        if id is not None:
            self.id = id
        if image is not None:
            self.image = image
        if legacy_name is not None:
            self.legacy_name = legacy_name
        if name is not None:
            self.name = name

    @property
    def actions(self):
        """Gets the actions of this GetAreaEventsDefinitions.  # noqa: E501


        :return: The actions of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this GetAreaEventsDefinitions.


        :param actions: The actions of this GetAreaEventsDefinitions.  # noqa: E501
        :type: str
        """

        self._actions = actions

    @property
    def color(self):
        """Gets the color of this GetAreaEventsDefinitions.  # noqa: E501

        The color associated with this area  # noqa: E501

        :return: The color of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this GetAreaEventsDefinitions.

        The color associated with this area  # noqa: E501

        :param color: The color of this GetAreaEventsDefinitions.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def id(self):
        """Gets the id of this GetAreaEventsDefinitions.  # noqa: E501

        The type of area  # noqa: E501

        :return: The id of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAreaEventsDefinitions.

        The type of area  # noqa: E501

        :param id: The id of this GetAreaEventsDefinitions.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this GetAreaEventsDefinitions.  # noqa: E501


        :return: The image of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this GetAreaEventsDefinitions.


        :param image: The image of this GetAreaEventsDefinitions.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def legacy_name(self):
        """Gets the legacy_name of this GetAreaEventsDefinitions.  # noqa: E501


        :return: The legacy_name of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._legacy_name

    @legacy_name.setter
    def legacy_name(self, legacy_name):
        """Sets the legacy_name of this GetAreaEventsDefinitions.


        :param legacy_name: The legacy_name of this GetAreaEventsDefinitions.  # noqa: E501
        :type: str
        """

        self._legacy_name = legacy_name

    @property
    def name(self):
        """Gets the name of this GetAreaEventsDefinitions.  # noqa: E501

        A nice name associated with this area action  # noqa: E501

        :return: The name of this GetAreaEventsDefinitions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAreaEventsDefinitions.

        A nice name associated with this area action  # noqa: E501

        :param name: The name of this GetAreaEventsDefinitions.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GetAreaEventsDefinitions, dict):
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
        if not isinstance(other, GetAreaEventsDefinitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other