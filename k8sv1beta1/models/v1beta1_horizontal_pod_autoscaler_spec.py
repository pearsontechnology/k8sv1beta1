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


class V1beta1HorizontalPodAutoscalerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, scaleRef=None, minReplicas=None, maxReplicas=None, cpuUtilization=None):
        """
        V1beta1HorizontalPodAutoscalerSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'scaleRef': 'V1beta1SubresourceReference',
            'minReplicas': 'int',
            'maxReplicas': 'int',
            'cpuUtilization': 'V1beta1CPUTargetUtilization'
        }

        self.attribute_map = {
            'scaleRef': 'scaleRef',
            'minReplicas': 'minReplicas',
            'maxReplicas': 'maxReplicas',
            'cpuUtilization': 'cpuUtilization'
        }

        self._scaleRef = scaleRef
        self._minReplicas = minReplicas
        self._maxReplicas = maxReplicas
        self._cpuUtilization = cpuUtilization

    @property
    def scaleRef(self):
        """
        Gets the scaleRef of this V1beta1HorizontalPodAutoscalerSpec.
        reference to Scale subresource; horizontal pod autoscaler will learn the current resource consumption from its status, and will set the desired number of pods by modifying its spec.

        :return: The scaleRef of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: V1beta1SubresourceReference
        """
        return self._scaleRef

    @scaleRef.setter
    def scaleRef(self, scaleRef):
        """
        Sets the scaleRef of this V1beta1HorizontalPodAutoscalerSpec.
        reference to Scale subresource; horizontal pod autoscaler will learn the current resource consumption from its status, and will set the desired number of pods by modifying its spec.

        :param scaleRef: The scaleRef of this V1beta1HorizontalPodAutoscalerSpec.
        :type: V1beta1SubresourceReference
        """

        self._scaleRef = scaleRef

    @property
    def minReplicas(self):
        """
        Gets the minReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :return: The minReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._minReplicas

    @minReplicas.setter
    def minReplicas(self, minReplicas):
        """
        Sets the minReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        lower limit for the number of pods that can be set by the autoscaler, default 1.

        :param minReplicas: The minReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._minReplicas = minReplicas

    @property
    def maxReplicas(self):
        """
        Gets the maxReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :return: The maxReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: int
        """
        return self._maxReplicas

    @maxReplicas.setter
    def maxReplicas(self, maxReplicas):
        """
        Sets the maxReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.

        :param maxReplicas: The maxReplicas of this V1beta1HorizontalPodAutoscalerSpec.
        :type: int
        """

        self._maxReplicas = maxReplicas

    @property
    def cpuUtilization(self):
        """
        Gets the cpuUtilization of this V1beta1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified it defaults to the target CPU utilization at 80% of the requested resources.

        :return: The cpuUtilization of this V1beta1HorizontalPodAutoscalerSpec.
        :rtype: V1beta1CPUTargetUtilization
        """
        return self._cpuUtilization

    @cpuUtilization.setter
    def cpuUtilization(self, cpuUtilization):
        """
        Sets the cpuUtilization of this V1beta1HorizontalPodAutoscalerSpec.
        target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified it defaults to the target CPU utilization at 80% of the requested resources.

        :param cpuUtilization: The cpuUtilization of this V1beta1HorizontalPodAutoscalerSpec.
        :type: V1beta1CPUTargetUtilization
        """

        self._cpuUtilization = cpuUtilization

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
