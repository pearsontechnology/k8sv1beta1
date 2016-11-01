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


class V1FlexVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, driver=None, fsType=None, secretRef=None, readOnly=None, options=None):
        """
        V1FlexVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'driver': 'str',
            'fsType': 'str',
            'secretRef': 'V1LocalObjectReference',
            'readOnly': 'bool',
            'options': 'object'
        }

        self.attribute_map = {
            'driver': 'driver',
            'fsType': 'fsType',
            'secretRef': 'secretRef',
            'readOnly': 'readOnly',
            'options': 'options'
        }

        self._driver = driver
        self._fsType = fsType
        self._secretRef = secretRef
        self._readOnly = readOnly
        self._options = options

    @property
    def driver(self):
        """
        Gets the driver of this V1FlexVolumeSource.
        Driver is the name of the driver to use for this volume.

        :return: The driver of this V1FlexVolumeSource.
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """
        Sets the driver of this V1FlexVolumeSource.
        Driver is the name of the driver to use for this volume.

        :param driver: The driver of this V1FlexVolumeSource.
        :type: str
        """

        self._driver = driver

    @property
    def fsType(self):
        """
        Gets the fsType of this V1FlexVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". The default filesystem depends on FlexVolume script.

        :return: The fsType of this V1FlexVolumeSource.
        :rtype: str
        """
        return self._fsType

    @fsType.setter
    def fsType(self, fsType):
        """
        Sets the fsType of this V1FlexVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". The default filesystem depends on FlexVolume script.

        :param fsType: The fsType of this V1FlexVolumeSource.
        :type: str
        """

        self._fsType = fsType

    @property
    def secretRef(self):
        """
        Gets the secretRef of this V1FlexVolumeSource.
        Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.

        :return: The secretRef of this V1FlexVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secretRef

    @secretRef.setter
    def secretRef(self, secretRef):
        """
        Sets the secretRef of this V1FlexVolumeSource.
        Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.

        :param secretRef: The secretRef of this V1FlexVolumeSource.
        :type: V1LocalObjectReference
        """

        self._secretRef = secretRef

    @property
    def readOnly(self):
        """
        Gets the readOnly of this V1FlexVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :return: The readOnly of this V1FlexVolumeSource.
        :rtype: bool
        """
        return self._readOnly

    @readOnly.setter
    def readOnly(self, readOnly):
        """
        Sets the readOnly of this V1FlexVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.

        :param readOnly: The readOnly of this V1FlexVolumeSource.
        :type: bool
        """

        self._readOnly = readOnly

    @property
    def options(self):
        """
        Gets the options of this V1FlexVolumeSource.
        Optional: Extra command options if any.

        :return: The options of this V1FlexVolumeSource.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this V1FlexVolumeSource.
        Optional: Extra command options if any.

        :param options: The options of this V1FlexVolumeSource.
        :type: object
        """

        self._options = options

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
