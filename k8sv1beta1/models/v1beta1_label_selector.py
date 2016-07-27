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


class V1beta1LabelSelector(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, matchLabels=None, matchExpressions=None):
        """
        V1beta1LabelSelector - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'matchLabels': 'object',
            'matchExpressions': 'list[V1beta1LabelSelectorRequirement]'
        }

        self.attribute_map = {
            'matchLabels': 'matchLabels',
            'matchExpressions': 'matchExpressions'
        }

        self._matchLabels = matchLabels
        self._matchExpressions = matchExpressions

    @property
    def matchLabels(self):
        """
        Gets the matchLabels of this V1beta1LabelSelector.
        matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.

        :return: The matchLabels of this V1beta1LabelSelector.
        :rtype: object
        """
        return self._matchLabels

    @matchLabels.setter
    def matchLabels(self, matchLabels):
        """
        Sets the matchLabels of this V1beta1LabelSelector.
        matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.

        :param matchLabels: The matchLabels of this V1beta1LabelSelector.
        :type: object
        """

        self._matchLabels = matchLabels

    @property
    def matchExpressions(self):
        """
        Gets the matchExpressions of this V1beta1LabelSelector.
        matchExpressions is a list of label selector requirements. The requirements are ANDed.

        :return: The matchExpressions of this V1beta1LabelSelector.
        :rtype: list[V1beta1LabelSelectorRequirement]
        """
        return self._matchExpressions

    @matchExpressions.setter
    def matchExpressions(self, matchExpressions):
        """
        Sets the matchExpressions of this V1beta1LabelSelector.
        matchExpressions is a list of label selector requirements. The requirements are ANDed.

        :param matchExpressions: The matchExpressions of this V1beta1LabelSelector.
        :type: list[V1beta1LabelSelectorRequirement]
        """

        self._matchExpressions = matchExpressions

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
