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


class V1beta1DaemonSetStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currentNumberScheduled=None, numberMisscheduled=None, desiredNumberScheduled=None, numberReady=None):
        """
        V1beta1DaemonSetStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currentNumberScheduled': 'int',
            'numberMisscheduled': 'int',
            'desiredNumberScheduled': 'int',
            'numberReady': 'int'
        }

        self.attribute_map = {
            'currentNumberScheduled': 'currentNumberScheduled',
            'numberMisscheduled': 'numberMisscheduled',
            'desiredNumberScheduled': 'desiredNumberScheduled',
            'numberReady': 'numberReady'
        }

        self._currentNumberScheduled = currentNumberScheduled
        self._numberMisscheduled = numberMisscheduled
        self._desiredNumberScheduled = desiredNumberScheduled
        self._numberReady = numberReady

    @property
    def currentNumberScheduled(self):
        """
        Gets the currentNumberScheduled of this V1beta1DaemonSetStatus.
        CurrentNumberScheduled is the number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :return: The currentNumberScheduled of this V1beta1DaemonSetStatus.
        :rtype: int
        """
        return self._currentNumberScheduled

    @currentNumberScheduled.setter
    def currentNumberScheduled(self, currentNumberScheduled):
        """
        Sets the currentNumberScheduled of this V1beta1DaemonSetStatus.
        CurrentNumberScheduled is the number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :param currentNumberScheduled: The currentNumberScheduled of this V1beta1DaemonSetStatus.
        :type: int
        """

        self._currentNumberScheduled = currentNumberScheduled

    @property
    def numberMisscheduled(self):
        """
        Gets the numberMisscheduled of this V1beta1DaemonSetStatus.
        NumberMisscheduled is the number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :return: The numberMisscheduled of this V1beta1DaemonSetStatus.
        :rtype: int
        """
        return self._numberMisscheduled

    @numberMisscheduled.setter
    def numberMisscheduled(self, numberMisscheduled):
        """
        Sets the numberMisscheduled of this V1beta1DaemonSetStatus.
        NumberMisscheduled is the number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :param numberMisscheduled: The numberMisscheduled of this V1beta1DaemonSetStatus.
        :type: int
        """

        self._numberMisscheduled = numberMisscheduled

    @property
    def desiredNumberScheduled(self):
        """
        Gets the desiredNumberScheduled of this V1beta1DaemonSetStatus.
        DesiredNumberScheduled is the total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :return: The desiredNumberScheduled of this V1beta1DaemonSetStatus.
        :rtype: int
        """
        return self._desiredNumberScheduled

    @desiredNumberScheduled.setter
    def desiredNumberScheduled(self, desiredNumberScheduled):
        """
        Sets the desiredNumberScheduled of this V1beta1DaemonSetStatus.
        DesiredNumberScheduled is the total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md

        :param desiredNumberScheduled: The desiredNumberScheduled of this V1beta1DaemonSetStatus.
        :type: int
        """

        self._desiredNumberScheduled = desiredNumberScheduled

    @property
    def numberReady(self):
        """
        Gets the numberReady of this V1beta1DaemonSetStatus.
        NumberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.

        :return: The numberReady of this V1beta1DaemonSetStatus.
        :rtype: int
        """
        return self._numberReady

    @numberReady.setter
    def numberReady(self, numberReady):
        """
        Sets the numberReady of this V1beta1DaemonSetStatus.
        NumberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running and ready.

        :param numberReady: The numberReady of this V1beta1DaemonSetStatus.
        :type: int
        """

        self._numberReady = numberReady

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
