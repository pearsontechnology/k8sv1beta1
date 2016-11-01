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


class V1GCEPersistentDiskVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pdName=None, fsType=None, partition=None, readOnly=None):
        """
        V1GCEPersistentDiskVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pdName': 'str',
            'fsType': 'str',
            'partition': 'int',
            'readOnly': 'bool'
        }

        self.attribute_map = {
            'pdName': 'pdName',
            'fsType': 'fsType',
            'partition': 'partition',
            'readOnly': 'readOnly'
        }

        self._pdName = pdName
        self._fsType = fsType
        self._partition = partition
        self._readOnly = readOnly

    @property
    def pdName(self):
        """
        Gets the pdName of this V1GCEPersistentDiskVolumeSource.
        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The pdName of this V1GCEPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._pdName

    @pdName.setter
    def pdName(self, pdName):
        """
        Sets the pdName of this V1GCEPersistentDiskVolumeSource.
        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param pdName: The pdName of this V1GCEPersistentDiskVolumeSource.
        :type: str
        """

        self._pdName = pdName

    @property
    def fsType(self):
        """
        Gets the fsType of this V1GCEPersistentDiskVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The fsType of this V1GCEPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._fsType

    @fsType.setter
    def fsType(self, fsType):
        """
        Sets the fsType of this V1GCEPersistentDiskVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param fsType: The fsType of this V1GCEPersistentDiskVolumeSource.
        :type: str
        """

        self._fsType = fsType

    @property
    def partition(self):
        """
        Gets the partition of this V1GCEPersistentDiskVolumeSource.
        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The partition of this V1GCEPersistentDiskVolumeSource.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this V1GCEPersistentDiskVolumeSource.
        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param partition: The partition of this V1GCEPersistentDiskVolumeSource.
        :type: int
        """

        self._partition = partition

    @property
    def readOnly(self):
        """
        Gets the readOnly of this V1GCEPersistentDiskVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The readOnly of this V1GCEPersistentDiskVolumeSource.
        :rtype: bool
        """
        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):
        """
        Sets the readOnly of this V1GCEPersistentDiskVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param readOnly: The readOnly of this V1GCEPersistentDiskVolumeSource.
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
