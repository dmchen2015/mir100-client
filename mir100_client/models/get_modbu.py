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


class GetModbu(object):
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
        'data_type': 'str',
        'description': 'str',
        'id': 'int',
        'permissions': 'str',
        'registers': 'list[object]',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'data_type': 'data_type',
        'description': 'description',
        'id': 'id',
        'permissions': 'permissions',
        'registers': 'registers',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, data_type=None, description=None, id=None, permissions=None, registers=None, title=None, type=None):  # noqa: E501
        """GetModbu - a model defined in Swagger"""  # noqa: E501
        self._data_type = None
        self._description = None
        self._id = None
        self._permissions = None
        self._registers = None
        self._title = None
        self._type = None
        self.discriminator = None
        if data_type is not None:
            self.data_type = data_type
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if permissions is not None:
            self.permissions = permissions
        if registers is not None:
            self.registers = registers
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def data_type(self):
        """Gets the data_type of this GetModbu.  # noqa: E501

        The data type needed  # noqa: E501

        :return: The data_type of this GetModbu.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this GetModbu.

        The data type needed  # noqa: E501

        :param data_type: The data_type of this GetModbu.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this GetModbu.  # noqa: E501

        A more detailed explanation of the attribute  # noqa: E501

        :return: The description of this GetModbu.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetModbu.

        A more detailed explanation of the attribute  # noqa: E501

        :param description: The description of this GetModbu.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GetModbu.  # noqa: E501

        The id of the modbus entry  # noqa: E501

        :return: The id of this GetModbu.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetModbu.

        The id of the modbus entry  # noqa: E501

        :param id: The id of this GetModbu.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def permissions(self):
        """Gets the permissions of this GetModbu.  # noqa: E501

        If it is allowed to read or write this element  # noqa: E501

        :return: The permissions of this GetModbu.  # noqa: E501
        :rtype: str
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this GetModbu.

        If it is allowed to read or write this element  # noqa: E501

        :param permissions: The permissions of this GetModbu.  # noqa: E501
        :type: str
        """

        self._permissions = permissions

    @property
    def registers(self):
        """Gets the registers of this GetModbu.  # noqa: E501

        The registers on the plc where the data will be stored  # noqa: E501

        :return: The registers of this GetModbu.  # noqa: E501
        :rtype: list[object]
        """
        return self._registers

    @registers.setter
    def registers(self, registers):
        """Sets the registers of this GetModbu.

        The registers on the plc where the data will be stored  # noqa: E501

        :param registers: The registers of this GetModbu.  # noqa: E501
        :type: list[object]
        """

        self._registers = registers

    @property
    def title(self):
        """Gets the title of this GetModbu.  # noqa: E501

        A textual description of the desired element  # noqa: E501

        :return: The title of this GetModbu.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetModbu.

        A textual description of the desired element  # noqa: E501

        :param title: The title of this GetModbu.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this GetModbu.  # noqa: E501

        The endpoint to which the element refers  # noqa: E501

        :return: The type of this GetModbu.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetModbu.

        The endpoint to which the element refers  # noqa: E501

        :param type: The type of this GetModbu.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(GetModbu, dict):
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
        if not isinstance(other, GetModbu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
