# coding: utf-8

"""

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: extensions/v1beta1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1CephFSVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, monitors=None, path=None, user=None, secretFile=None, secretRef=None, readOnly=None):
        """
        V1CephFSVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'monitors': 'list[str]',
            'path': 'str',
            'user': 'str',
            'secretFile': 'str',
            'secretRef': 'V1LocalObjectReference',
            'readOnly': 'bool'
        }

        self.attribute_map = {
            'monitors': 'monitors',
            'path': 'path',
            'user': 'user',
            'secretFile': 'secretFile',
            'secretRef': 'secretRef',
            'readOnly': 'readOnly'
        }

        self._monitors = monitors
        self._path = path
        self._user = user
        self._secretFile = secretFile
        self._secretRef = secretRef
        self._readOnly = readOnly

    @property
    def monitors(self):
        """
        Gets the monitors of this V1CephFSVolumeSource.
        Required: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :return: The monitors of this V1CephFSVolumeSource.
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """
        Sets the monitors of this V1CephFSVolumeSource.
        Required: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :param monitors: The monitors of this V1CephFSVolumeSource.
        :type: list[str]
        """

        self._monitors = monitors

    @property
    def path(self):
        """
        Gets the path of this V1CephFSVolumeSource.
        Optional: Used as the mounted root, rather than the full Ceph tree, default is /

        :return: The path of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1CephFSVolumeSource.
        Optional: Used as the mounted root, rather than the full Ceph tree, default is /

        :param path: The path of this V1CephFSVolumeSource.
        :type: str
        """

        self._path = path

    @property
    def user(self):
        """
        Gets the user of this V1CephFSVolumeSource.
        Optional: User is the rados user name, default is admin More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :return: The user of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1CephFSVolumeSource.
        Optional: User is the rados user name, default is admin More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :param user: The user of this V1CephFSVolumeSource.
        :type: str
        """

        self._user = user

    @property
    def secretFile(self):
        """
        Gets the secretFile of this V1CephFSVolumeSource.
        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :return: The secretFile of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._secretFile

    @secretFile.setter
    def secretFile(self, secretFile):
        """
        Sets the secretFile of this V1CephFSVolumeSource.
        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :param secretFile: The secretFile of this V1CephFSVolumeSource.
        :type: str
        """

        self._secretFile = secretFile

    @property
    def secretRef(self):
        """
        Gets the secretRef of this V1CephFSVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :return: The secretRef of this V1CephFSVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secretRef

    @secretRef.setter
    def secretRef(self, secretRef):
        """
        Sets the secretRef of this V1CephFSVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :param secretRef: The secretRef of this V1CephFSVolumeSource.
        :type: V1LocalObjectReference
        """

        self._secretRef = secretRef

    @property
    def readOnly(self):
        """
        Gets the readOnly of this V1CephFSVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :return: The readOnly of this V1CephFSVolumeSource.
        :rtype: bool
        """
        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):
        """
        Sets the readOnly of this V1CephFSVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it

        :param readOnly: The readOnly of this V1CephFSVolumeSource.
        :type: bool
        """

        self._readOnly = readOnly

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
