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


class GetMapPaths(object):
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
        'goal_pos': 'str',
        'guid': 'str',
        'start_pos': 'str',
        'url': 'str'
    }

    attribute_map = {
        'goal_pos': 'goal_pos',
        'guid': 'guid',
        'start_pos': 'start_pos',
        'url': 'url'
    }

    def __init__(self, goal_pos=None, guid=None, start_pos=None, url=None):  # noqa: E501
        """GetMapPaths - a model defined in Swagger"""  # noqa: E501
        self._goal_pos = None
        self._guid = None
        self._start_pos = None
        self._url = None
        self.discriminator = None
        if goal_pos is not None:
            self.goal_pos = goal_pos
        if guid is not None:
            self.guid = guid
        if start_pos is not None:
            self.start_pos = start_pos
        if url is not None:
            self.url = url

    @property
    def goal_pos(self):
        """Gets the goal_pos of this GetMapPaths.  # noqa: E501

        The url to the end position of the path  # noqa: E501

        :return: The goal_pos of this GetMapPaths.  # noqa: E501
        :rtype: str
        """
        return self._goal_pos

    @goal_pos.setter
    def goal_pos(self, goal_pos):
        """Sets the goal_pos of this GetMapPaths.

        The url to the end position of the path  # noqa: E501

        :param goal_pos: The goal_pos of this GetMapPaths.  # noqa: E501
        :type: str
        """

        self._goal_pos = goal_pos

    @property
    def guid(self):
        """Gets the guid of this GetMapPaths.  # noqa: E501

        The global id unique across robots that identifies this path  # noqa: E501

        :return: The guid of this GetMapPaths.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetMapPaths.

        The global id unique across robots that identifies this path  # noqa: E501

        :param guid: The guid of this GetMapPaths.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def start_pos(self):
        """Gets the start_pos of this GetMapPaths.  # noqa: E501

        The url to the start position of the path  # noqa: E501

        :return: The start_pos of this GetMapPaths.  # noqa: E501
        :rtype: str
        """
        return self._start_pos

    @start_pos.setter
    def start_pos(self, start_pos):
        """Sets the start_pos of this GetMapPaths.

        The url to the start position of the path  # noqa: E501

        :param start_pos: The start_pos of this GetMapPaths.  # noqa: E501
        :type: str
        """

        self._start_pos = start_pos

    @property
    def url(self):
        """Gets the url of this GetMapPaths.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetMapPaths.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetMapPaths.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetMapPaths.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(GetMapPaths, dict):
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
        if not isinstance(other, GetMapPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
