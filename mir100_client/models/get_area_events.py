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


class GetAreaEvents(object):
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
        'guid': 'str',
        'map': 'str',
        'name': 'str',
        'type_id': 'int',
        'url': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'map': 'map',
        'name': 'name',
        'type_id': 'type_id',
        'url': 'url'
    }

    def __init__(self, guid=None, map=None, name=None, type_id=None, url=None):  # noqa: E501
        """GetAreaEvents - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._map = None
        self._name = None
        self._type_id = None
        self._url = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if map is not None:
            self.map = map
        if name is not None:
            self.name = name
        if type_id is not None:
            self.type_id = type_id
        if url is not None:
            self.url = url

    @property
    def guid(self):
        """Gets the guid of this GetAreaEvents.  # noqa: E501

        The global id unique across robots that identifies this area  # noqa: E501

        :return: The guid of this GetAreaEvents.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetAreaEvents.

        The global id unique across robots that identifies this area  # noqa: E501

        :param guid: The guid of this GetAreaEvents.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def map(self):
        """Gets the map of this GetAreaEvents.  # noqa: E501

        The url to the map this area belongs to  # noqa: E501

        :return: The map of this GetAreaEvents.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this GetAreaEvents.

        The url to the map this area belongs to  # noqa: E501

        :param map: The map of this GetAreaEvents.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def name(self):
        """Gets the name of this GetAreaEvents.  # noqa: E501

        A name associated with this area  # noqa: E501

        :return: The name of this GetAreaEvents.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAreaEvents.

        A name associated with this area  # noqa: E501

        :param name: The name of this GetAreaEvents.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type_id(self):
        """Gets the type_id of this GetAreaEvents.  # noqa: E501

        The type of area  # noqa: E501

        :return: The type_id of this GetAreaEvents.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetAreaEvents.

        The type of area  # noqa: E501

        :param type_id: The type_id of this GetAreaEvents.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def url(self):
        """Gets the url of this GetAreaEvents.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetAreaEvents.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetAreaEvents.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetAreaEvents.  # noqa: E501
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
        if issubclass(GetAreaEvents, dict):
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
        if not isinstance(other, GetAreaEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other