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


class V1beta1SubresourceReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Kind=None, Name=None, ApiVersion=None, Subresource=None):
        """
        V1beta1SubresourceReference - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Kind': 'str',
            'Name': 'str',
            'ApiVersion': 'str',
            'Subresource': 'str'
        }

        self.attribute_map = {
            'Kind': 'kind',
            'Name': 'name',
            'ApiVersion': 'apiVersion',
            'Subresource': 'subresource'
        }

        self._Kind = Kind
        self._Name = Name
        self._ApiVersion = ApiVersion
        self._Subresource = Subresource

    @property
    def Kind(self):
        """
        Gets the Kind of this V1beta1SubresourceReference.
        Kind of the referent; More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The Kind of this V1beta1SubresourceReference.
        :rtype: str
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        """
        Sets the Kind of this V1beta1SubresourceReference.
        Kind of the referent; More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param Kind: The Kind of this V1beta1SubresourceReference.
        :type: str
        """

        self._Kind = Kind

    @property
    def Name(self):
        """
        Gets the Name of this V1beta1SubresourceReference.
        Name of the referent; More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :return: The Name of this V1beta1SubresourceReference.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        """
        Sets the Name of this V1beta1SubresourceReference.
        Name of the referent; More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :param Name: The Name of this V1beta1SubresourceReference.
        :type: str
        """

        self._Name = Name

    @property
    def ApiVersion(self):
        """
        Gets the ApiVersion of this V1beta1SubresourceReference.
        API version of the referent

        :return: The ApiVersion of this V1beta1SubresourceReference.
        :rtype: str
        """
        return self._ApiVersion

    @ApiVersion.setter
    def ApiVersion(self, ApiVersion):
        """
        Sets the ApiVersion of this V1beta1SubresourceReference.
        API version of the referent

        :param ApiVersion: The ApiVersion of this V1beta1SubresourceReference.
        :type: str
        """

        self._ApiVersion = ApiVersion

    @property
    def Subresource(self):
        """
        Gets the Subresource of this V1beta1SubresourceReference.
        Subresource name of the referent

        :return: The Subresource of this V1beta1SubresourceReference.
        :rtype: str
        """
        return self._Subresource

    @Subresource.setter
    def Subresource(self, Subresource):
        """
        Sets the Subresource of this V1beta1SubresourceReference.
        Subresource name of the referent

        :param Subresource: The Subresource of this V1beta1SubresourceReference.
        :type: str
        """

        self._Subresource = Subresource

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
