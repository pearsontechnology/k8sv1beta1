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


class V1Lifecycle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, postStart=None, preStop=None):
        """
        V1Lifecycle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'postStart': 'V1Handler',
            'preStop': 'V1Handler'
        }

        self.attribute_map = {
            'postStart': 'postStart',
            'preStop': 'preStop'
        }

        self._postStart = postStart
        self._preStop = preStop

    @property
    def postStart(self):
        """
        Gets the postStart of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#hook-details

        :return: The postStart of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._postStart

    @postStart.setter
    def postStart(self, postStart):
        """
        Sets the postStart of this V1Lifecycle.
        PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#hook-details

        :param postStart: The postStart of this V1Lifecycle.
        :type: V1Handler
        """

        self._postStart = postStart

    @property
    def preStop(self):
        """
        Gets the preStop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#hook-details

        :return: The preStop of this V1Lifecycle.
        :rtype: V1Handler
        """
        return self._preStop

    @preStop.setter
    def preStop(self, preStop):
        """
        Sets the preStop of this V1Lifecycle.
        PreStop is called immediately before a container is terminated. The container is terminated after the handler completes. The reason for termination is passed to the handler. Regardless of the outcome of the handler, the container is eventually terminated. Other management of the container blocks until the hook completes. More info: http://releases.k8s.io/HEAD/docs/user-guide/container-environment.md#hook-details

        :param preStop: The preStop of this V1Lifecycle.
        :type: V1Handler
        """

        self._preStop = preStop

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
