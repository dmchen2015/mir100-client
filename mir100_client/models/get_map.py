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


class GetMap(object):
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
        'created_by': 'str',
        'created_by_id': 'str',
        'guid': 'str',
        'map': 'str',
        'metadata': 'str',
        'name': 'str',
        'one_way_map': 'str',
        'origin_theta': 'float',
        'origin_x': 'float',
        'origin_y': 'float',
        'path_guides': 'str',
        'paths': 'str',
        'positions': 'str',
        'resolution': 'float',
        'session_id': 'str'
    }

    attribute_map = {
        'created_by': 'created_by',
        'created_by_id': 'created_by_id',
        'guid': 'guid',
        'map': 'map',
        'metadata': 'metadata',
        'name': 'name',
        'one_way_map': 'one_way_map',
        'origin_theta': 'origin_theta',
        'origin_x': 'origin_x',
        'origin_y': 'origin_y',
        'path_guides': 'path_guides',
        'paths': 'paths',
        'positions': 'positions',
        'resolution': 'resolution',
        'session_id': 'session_id'
    }

    def __init__(self, created_by=None, created_by_id=None, guid=None, map=None, metadata=None, name=None, one_way_map=None, origin_theta=None, origin_x=None, origin_y=None, path_guides=None, paths=None, positions=None, resolution=None, session_id=None):  # noqa: E501
        """GetMap - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_by_id = None
        self._guid = None
        self._map = None
        self._metadata = None
        self._name = None
        self._one_way_map = None
        self._origin_theta = None
        self._origin_x = None
        self._origin_y = None
        self._path_guides = None
        self._paths = None
        self._positions = None
        self._resolution = None
        self._session_id = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if guid is not None:
            self.guid = guid
        if map is not None:
            self.map = map
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if one_way_map is not None:
            self.one_way_map = one_way_map
        if origin_theta is not None:
            self.origin_theta = origin_theta
        if origin_x is not None:
            self.origin_x = origin_x
        if origin_y is not None:
            self.origin_y = origin_y
        if path_guides is not None:
            self.path_guides = path_guides
        if paths is not None:
            self.paths = paths
        if positions is not None:
            self.positions = positions
        if resolution is not None:
            self.resolution = resolution
        if session_id is not None:
            self.session_id = session_id

    @property
    def created_by(self):
        """Gets the created_by of this GetMap.  # noqa: E501

        The url to the description of the type of this position  # noqa: E501

        :return: The created_by of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetMap.

        The url to the description of the type of this position  # noqa: E501

        :param created_by: The created_by of this GetMap.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetMap.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetMap.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetMap.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this GetMap.  # noqa: E501

        The global id unique across robots that identifies this map  # noqa: E501

        :return: The guid of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetMap.

        The global id unique across robots that identifies this map  # noqa: E501

        :param guid: The guid of this GetMap.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def map(self):
        """Gets the map of this GetMap.  # noqa: E501

        If this map is navigation map or not  # noqa: E501

        :return: The map of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this GetMap.

        If this map is navigation map or not  # noqa: E501

        :param map: The map of this GetMap.  # noqa: E501
        :type: str
        """

        self._map = map

    @property
    def metadata(self):
        """Gets the metadata of this GetMap.  # noqa: E501

        If this map is a web map or not  # noqa: E501

        :return: The metadata of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this GetMap.

        If this map is a web map or not  # noqa: E501

        :param metadata: The metadata of this GetMap.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this GetMap.  # noqa: E501

        The name of the map  # noqa: E501

        :return: The name of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetMap.

        The name of the map  # noqa: E501

        :param name: The name of this GetMap.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def one_way_map(self):
        """Gets the one_way_map of this GetMap.  # noqa: E501

        If this map is navigation map or not  # noqa: E501

        :return: The one_way_map of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._one_way_map

    @one_way_map.setter
    def one_way_map(self, one_way_map):
        """Sets the one_way_map of this GetMap.

        If this map is navigation map or not  # noqa: E501

        :param one_way_map: The one_way_map of this GetMap.  # noqa: E501
        :type: str
        """

        self._one_way_map = one_way_map

    @property
    def origin_theta(self):
        """Gets the origin_theta of this GetMap.  # noqa: E501

        The angle in the map of the center of the map relative to the robots position  # noqa: E501

        :return: The origin_theta of this GetMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_theta

    @origin_theta.setter
    def origin_theta(self, origin_theta):
        """Sets the origin_theta of this GetMap.

        The angle in the map of the center of the map relative to the robots position  # noqa: E501

        :param origin_theta: The origin_theta of this GetMap.  # noqa: E501
        :type: float
        """

        self._origin_theta = origin_theta

    @property
    def origin_x(self):
        """Gets the origin_x of this GetMap.  # noqa: E501

        The x-coordinate in the map of the center of the map relative to the robots position  # noqa: E501

        :return: The origin_x of this GetMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_x

    @origin_x.setter
    def origin_x(self, origin_x):
        """Sets the origin_x of this GetMap.

        The x-coordinate in the map of the center of the map relative to the robots position  # noqa: E501

        :param origin_x: The origin_x of this GetMap.  # noqa: E501
        :type: float
        """

        self._origin_x = origin_x

    @property
    def origin_y(self):
        """Gets the origin_y of this GetMap.  # noqa: E501

        The y-coordinate in the map of the center of the map relative to the robots position  # noqa: E501

        :return: The origin_y of this GetMap.  # noqa: E501
        :rtype: float
        """
        return self._origin_y

    @origin_y.setter
    def origin_y(self, origin_y):
        """Sets the origin_y of this GetMap.

        The y-coordinate in the map of the center of the map relative to the robots position  # noqa: E501

        :param origin_y: The origin_y of this GetMap.  # noqa: E501
        :type: float
        """

        self._origin_y = origin_y

    @property
    def path_guides(self):
        """Gets the path_guides of this GetMap.  # noqa: E501

        The url to the list of path guides in this map  # noqa: E501

        :return: The path_guides of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._path_guides

    @path_guides.setter
    def path_guides(self, path_guides):
        """Sets the path_guides of this GetMap.

        The url to the list of path guides in this map  # noqa: E501

        :param path_guides: The path_guides of this GetMap.  # noqa: E501
        :type: str
        """

        self._path_guides = path_guides

    @property
    def paths(self):
        """Gets the paths of this GetMap.  # noqa: E501

        The url to the list of paths in this map  # noqa: E501

        :return: The paths of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this GetMap.

        The url to the list of paths in this map  # noqa: E501

        :param paths: The paths of this GetMap.  # noqa: E501
        :type: str
        """

        self._paths = paths

    @property
    def positions(self):
        """Gets the positions of this GetMap.  # noqa: E501

        The url to the list of positions in this map  # noqa: E501

        :return: The positions of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this GetMap.

        The url to the list of positions in this map  # noqa: E501

        :param positions: The positions of this GetMap.  # noqa: E501
        :type: str
        """

        self._positions = positions

    @property
    def resolution(self):
        """Gets the resolution of this GetMap.  # noqa: E501

        The resolution of the map  # noqa: E501

        :return: The resolution of this GetMap.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this GetMap.

        The resolution of the map  # noqa: E501

        :param resolution: The resolution of this GetMap.  # noqa: E501
        :type: float
        """

        self._resolution = resolution

    @property
    def session_id(self):
        """Gets the session_id of this GetMap.  # noqa: E501

        The global id unique across robots of the area containing this map  # noqa: E501

        :return: The session_id of this GetMap.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this GetMap.

        The global id unique across robots of the area containing this map  # noqa: E501

        :param session_id: The session_id of this GetMap.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

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
        if issubclass(GetMap, dict):
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
        if not isinstance(other, GetMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
