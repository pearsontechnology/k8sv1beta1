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
    def __init__(self, PdName=None, FsType=None, Partition=None, ReadOnly=None):
        """
        V1GCEPersistentDiskVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'PdName': 'str',
            'FsType': 'str',
            'Partition': 'int',
            'ReadOnly': 'bool'
        }

        self.attribute_map = {
            'PdName': 'pdName',
            'FsType': 'fsType',
            'Partition': 'partition',
            'ReadOnly': 'readOnly'
        }

        self._PdName = PdName
        self._FsType = FsType
        self._Partition = Partition
        self._ReadOnly = ReadOnly

    @property
    def PdName(self):
        """
        Gets the PdName of this V1GCEPersistentDiskVolumeSource.
        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The PdName of this V1GCEPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._PdName

    @PdName.setter
    def PdName(self, PdName):
        """
        Sets the PdName of this V1GCEPersistentDiskVolumeSource.
        Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param PdName: The PdName of this V1GCEPersistentDiskVolumeSource.
        :type: str
        """

        self._PdName = PdName

    @property
    def FsType(self):
        """
        Gets the FsType of this V1GCEPersistentDiskVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The FsType of this V1GCEPersistentDiskVolumeSource.
        :rtype: str
        """
        return self._FsType

    @FsType.setter
    def FsType(self, FsType):
        """
        Sets the FsType of this V1GCEPersistentDiskVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param FsType: The FsType of this V1GCEPersistentDiskVolumeSource.
        :type: str
        """

        self._FsType = FsType

    @property
    def Partition(self):
        """
        Gets the Partition of this V1GCEPersistentDiskVolumeSource.
        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The Partition of this V1GCEPersistentDiskVolumeSource.
        :rtype: int
        """
        return self._Partition

    @Partition.setter
    def Partition(self, Partition):
        """
        Sets the Partition of this V1GCEPersistentDiskVolumeSource.
        The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as \"1\". Similarly, the volume partition for /dev/sda is \"0\" (or you can leave the property empty). More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param Partition: The Partition of this V1GCEPersistentDiskVolumeSource.
        :type: int
        """

        self._Partition = Partition

    @property
    def ReadOnly(self):
        """
        Gets the ReadOnly of this V1GCEPersistentDiskVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :return: The ReadOnly of this V1GCEPersistentDiskVolumeSource.
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        """
        Sets the ReadOnly of this V1GCEPersistentDiskVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md#gcepersistentdisk

        :param ReadOnly: The ReadOnly of this V1GCEPersistentDiskVolumeSource.
        :type: bool
        """

        self._ReadOnly = ReadOnly

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
