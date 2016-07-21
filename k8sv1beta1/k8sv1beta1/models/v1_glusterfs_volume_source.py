# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1GlusterfsVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1GlusterfsVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'endpoints': 'str',
            'path': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'endpoints': 'endpoints',
            'path': 'path',
            'read_only': 'readOnly'
        }

        self._endpoints = None
        self._path = None
        self._read_only = None

    @property
    def endpoints(self):
        """
        Gets the endpoints of this V1GlusterfsVolumeSource.
        EndpointsName is the endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The endpoints of this V1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this V1GlusterfsVolumeSource.
        EndpointsName is the endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param endpoints: The endpoints of this V1GlusterfsVolumeSource.
        :type: str
        """
        self._endpoints = endpoints

    @property
    def path(self):
        """
        Gets the path of this V1GlusterfsVolumeSource.
        Path is the Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The path of this V1GlusterfsVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1GlusterfsVolumeSource.
        Path is the Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param path: The path of this V1GlusterfsVolumeSource.
        :type: str
        """
        self._path = path

    @property
    def read_only(self):
        """
        Gets the read_only of this V1GlusterfsVolumeSource.
        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :return: The read_only of this V1GlusterfsVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1GlusterfsVolumeSource.
        ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod

        :param read_only: The read_only of this V1GlusterfsVolumeSource.
        :type: bool
        """
        self._read_only = read_only

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

