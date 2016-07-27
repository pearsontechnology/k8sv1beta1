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


class V1EnvVarSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, FieldRef=None, ResourceFieldRef=None, ConfigMapKeyRef=None, SecretKeyRef=None):
        """
        V1EnvVarSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'FieldRef': 'V1ObjectFieldSelector',
            'ResourceFieldRef': 'V1ResourceFieldSelector',
            'ConfigMapKeyRef': 'V1ConfigMapKeySelector',
            'SecretKeyRef': 'V1SecretKeySelector'
        }

        self.attribute_map = {
            'FieldRef': 'fieldRef',
            'ResourceFieldRef': 'resourceFieldRef',
            'ConfigMapKeyRef': 'configMapKeyRef',
            'SecretKeyRef': 'secretKeyRef'
        }

        self._FieldRef = FieldRef
        self._ResourceFieldRef = ResourceFieldRef
        self._ConfigMapKeyRef = ConfigMapKeyRef
        self._SecretKeyRef = SecretKeyRef

    @property
    def FieldRef(self):
        """
        Gets the FieldRef of this V1EnvVarSource.
        Selects a field of the pod; only name and namespace are supported.

        :return: The FieldRef of this V1EnvVarSource.
        :rtype: V1ObjectFieldSelector
        """
        return self._FieldRef

    @FieldRef.setter
    def FieldRef(self, FieldRef):
        """
        Sets the FieldRef of this V1EnvVarSource.
        Selects a field of the pod; only name and namespace are supported.

        :param FieldRef: The FieldRef of this V1EnvVarSource.
        :type: V1ObjectFieldSelector
        """

        self._FieldRef = FieldRef

    @property
    def ResourceFieldRef(self):
        """
        Gets the ResourceFieldRef of this V1EnvVarSource.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :return: The ResourceFieldRef of this V1EnvVarSource.
        :rtype: V1ResourceFieldSelector
        """
        return self._ResourceFieldRef

    @ResourceFieldRef.setter
    def ResourceFieldRef(self, ResourceFieldRef):
        """
        Sets the ResourceFieldRef of this V1EnvVarSource.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.

        :param ResourceFieldRef: The ResourceFieldRef of this V1EnvVarSource.
        :type: V1ResourceFieldSelector
        """

        self._ResourceFieldRef = ResourceFieldRef

    @property
    def ConfigMapKeyRef(self):
        """
        Gets the ConfigMapKeyRef of this V1EnvVarSource.
        Selects a key of a ConfigMap.

        :return: The ConfigMapKeyRef of this V1EnvVarSource.
        :rtype: V1ConfigMapKeySelector
        """
        return self._ConfigMapKeyRef

    @ConfigMapKeyRef.setter
    def ConfigMapKeyRef(self, ConfigMapKeyRef):
        """
        Sets the ConfigMapKeyRef of this V1EnvVarSource.
        Selects a key of a ConfigMap.

        :param ConfigMapKeyRef: The ConfigMapKeyRef of this V1EnvVarSource.
        :type: V1ConfigMapKeySelector
        """

        self._ConfigMapKeyRef = ConfigMapKeyRef

    @property
    def SecretKeyRef(self):
        """
        Gets the SecretKeyRef of this V1EnvVarSource.
        Selects a key of a secret in the pod's namespace

        :return: The SecretKeyRef of this V1EnvVarSource.
        :rtype: V1SecretKeySelector
        """
        return self._SecretKeyRef

    @SecretKeyRef.setter
    def SecretKeyRef(self, SecretKeyRef):
        """
        Sets the SecretKeyRef of this V1EnvVarSource.
        Selects a key of a secret in the pod's namespace

        :param SecretKeyRef: The SecretKeyRef of this V1EnvVarSource.
        :type: V1SecretKeySelector
        """

        self._SecretKeyRef = SecretKeyRef

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
