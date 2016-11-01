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


class V1beta1ReplicaSetCondition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, status=None, lastTransitionTime=None, reason=None, message=None):
        """
        V1beta1ReplicaSetCondition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'status': 'str',
            'lastTransitionTime': 'datetime',
            'reason': 'str',
            'message': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'status': 'status',
            'lastTransitionTime': 'lastTransitionTime',
            'reason': 'reason',
            'message': 'message'
        }

        self._type = type
        self._status = status
        self._lastTransitionTime = lastTransitionTime
        self._reason = reason
        self._message = message

    @property
    def type(self):
        """
        Gets the type of this V1beta1ReplicaSetCondition.
        Type of replica set condition.

        :return: The type of this V1beta1ReplicaSetCondition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1beta1ReplicaSetCondition.
        Type of replica set condition.

        :param type: The type of this V1beta1ReplicaSetCondition.
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this V1beta1ReplicaSetCondition.
        Status of the condition, one of True, False, Unknown.

        :return: The status of this V1beta1ReplicaSetCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1beta1ReplicaSetCondition.
        Status of the condition, one of True, False, Unknown.

        :param status: The status of this V1beta1ReplicaSetCondition.
        :type: str
        """

        self._status = status

    @property
    def lastTransitionTime(self):
        """
        Gets the lastTransitionTime of this V1beta1ReplicaSetCondition.
        The last time the condition transitioned from one status to another.

        :return: The lastTransitionTime of this V1beta1ReplicaSetCondition.
        :rtype: datetime
        """
        return self._lastTransitionTime

    @lastTransitionTime.setter
    def lastTransitionTime(self, lastTransitionTime):
        """
        Sets the lastTransitionTime of this V1beta1ReplicaSetCondition.
        The last time the condition transitioned from one status to another.

        :param lastTransitionTime: The lastTransitionTime of this V1beta1ReplicaSetCondition.
        :type: datetime
        """

        self._lastTransitionTime = lastTransitionTime

    @property
    def reason(self):
        """
        Gets the reason of this V1beta1ReplicaSetCondition.
        The reason for the condition's last transition.

        :return: The reason of this V1beta1ReplicaSetCondition.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1beta1ReplicaSetCondition.
        The reason for the condition's last transition.

        :param reason: The reason of this V1beta1ReplicaSetCondition.
        :type: str
        """

        self._reason = reason

    @property
    def message(self):
        """
        Gets the message of this V1beta1ReplicaSetCondition.
        A human readable message indicating details about the transition.

        :return: The message of this V1beta1ReplicaSetCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1beta1ReplicaSetCondition.
        A human readable message indicating details about the transition.

        :param message: The message of this V1beta1ReplicaSetCondition.
        :type: str
        """

        self._message = message

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
