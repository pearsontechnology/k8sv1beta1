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


class V1ObjectMeta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Name=None, GenerateName=None, Namespace=None, SelfLink=None, Uid=None, ResourceVersion=None, Generation=None, CreationTimestamp=None, DeletionTimestamp=None, DeletionGracePeriodSeconds=None, Labels=None, Annotations=None, OwnerReferences=None, Finalizers=None):
        """
        V1ObjectMeta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Name': 'str',
            'GenerateName': 'str',
            'Namespace': 'str',
            'SelfLink': 'str',
            'Uid': 'str',
            'ResourceVersion': 'str',
            'Generation': 'int',
            'CreationTimestamp': 'datetime',
            'DeletionTimestamp': 'datetime',
            'DeletionGracePeriodSeconds': 'int',
            'Labels': 'object',
            'Annotations': 'object',
            'OwnerReferences': 'list[V1OwnerReference]',
            'Finalizers': 'list[str]'
        }

        self.attribute_map = {
            'Name': 'name',
            'GenerateName': 'generateName',
            'Namespace': 'namespace',
            'SelfLink': 'selfLink',
            'Uid': 'uid',
            'ResourceVersion': 'resourceVersion',
            'Generation': 'generation',
            'CreationTimestamp': 'creationTimestamp',
            'DeletionTimestamp': 'deletionTimestamp',
            'DeletionGracePeriodSeconds': 'deletionGracePeriodSeconds',
            'Labels': 'labels',
            'Annotations': 'annotations',
            'OwnerReferences': 'ownerReferences',
            'Finalizers': 'finalizers'
        }

        self._Name = Name
        self._GenerateName = GenerateName
        self._Namespace = Namespace
        self._SelfLink = SelfLink
        self._Uid = Uid
        self._ResourceVersion = ResourceVersion
        self._Generation = Generation
        self._CreationTimestamp = CreationTimestamp
        self._DeletionTimestamp = DeletionTimestamp
        self._DeletionGracePeriodSeconds = DeletionGracePeriodSeconds
        self._Labels = Labels
        self._Annotations = Annotations
        self._OwnerReferences = OwnerReferences
        self._Finalizers = Finalizers

    @property
    def Name(self):
        """
        Gets the Name of this V1ObjectMeta.
        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :return: The Name of this V1ObjectMeta.
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        """
        Sets the Name of this V1ObjectMeta.
        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#names

        :param Name: The Name of this V1ObjectMeta.
        :type: str
        """

        self._Name = Name

    @property
    def GenerateName(self):
        """
        Gets the GenerateName of this V1ObjectMeta.
        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#idempotency

        :return: The GenerateName of this V1ObjectMeta.
        :rtype: str
        """
        return self._GenerateName

    @GenerateName.setter
    def GenerateName(self, GenerateName):
        """
        Sets the GenerateName of this V1ObjectMeta.
        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#idempotency

        :param GenerateName: The GenerateName of this V1ObjectMeta.
        :type: str
        """

        self._GenerateName = GenerateName

    @property
    def Namespace(self):
        """
        Gets the Namespace of this V1ObjectMeta.
        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/namespaces.md

        :return: The Namespace of this V1ObjectMeta.
        :rtype: str
        """
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        """
        Sets the Namespace of this V1ObjectMeta.
        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/namespaces.md

        :param Namespace: The Namespace of this V1ObjectMeta.
        :type: str
        """

        self._Namespace = Namespace

    @property
    def SelfLink(self):
        """
        Gets the SelfLink of this V1ObjectMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :return: The SelfLink of this V1ObjectMeta.
        :rtype: str
        """
        return self._SelfLink

    @SelfLink.setter
    def SelfLink(self, SelfLink):
        """
        Sets the SelfLink of this V1ObjectMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :param SelfLink: The SelfLink of this V1ObjectMeta.
        :type: str
        """

        self._SelfLink = SelfLink

    @property
    def Uid(self):
        """
        Gets the Uid of this V1ObjectMeta.
        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :return: The Uid of this V1ObjectMeta.
        :rtype: str
        """
        return self._Uid

    @Uid.setter
    def Uid(self, Uid):
        """
        Sets the Uid of this V1ObjectMeta.
        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/user-guide/identifiers.md#uids

        :param Uid: The Uid of this V1ObjectMeta.
        :type: str
        """

        self._Uid = Uid

    @property
    def ResourceVersion(self):
        """
        Gets the ResourceVersion of this V1ObjectMeta.
        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The ResourceVersion of this V1ObjectMeta.
        :rtype: str
        """
        return self._ResourceVersion

    @ResourceVersion.setter
    def ResourceVersion(self, ResourceVersion):
        """
        Sets the ResourceVersion of this V1ObjectMeta.
        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :param ResourceVersion: The ResourceVersion of this V1ObjectMeta.
        :type: str
        """

        self._ResourceVersion = ResourceVersion

    @property
    def Generation(self):
        """
        Gets the Generation of this V1ObjectMeta.
        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.

        :return: The Generation of this V1ObjectMeta.
        :rtype: int
        """
        return self._Generation

    @Generation.setter
    def Generation(self, Generation):
        """
        Sets the Generation of this V1ObjectMeta.
        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.

        :param Generation: The Generation of this V1ObjectMeta.
        :type: int
        """

        self._Generation = Generation

    @property
    def CreationTimestamp(self):
        """
        Gets the CreationTimestamp of this V1ObjectMeta.
        CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The CreationTimestamp of this V1ObjectMeta.
        :rtype: datetime
        """
        return self._CreationTimestamp

    @CreationTimestamp.setter
    def CreationTimestamp(self, CreationTimestamp):
        """
        Sets the CreationTimestamp of this V1ObjectMeta.
        CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param CreationTimestamp: The CreationTimestamp of this V1ObjectMeta.
        :type: datetime
        """

        self._CreationTimestamp = CreationTimestamp

    @property
    def DeletionTimestamp(self):
        """
        Gets the DeletionTimestamp of this V1ObjectMeta.
        DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource will be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field. Once set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. Once the resource is deleted in the API, the Kubelet will send a hard termination signal to the container. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The DeletionTimestamp of this V1ObjectMeta.
        :rtype: datetime
        """
        return self._DeletionTimestamp

    @DeletionTimestamp.setter
    def DeletionTimestamp(self, DeletionTimestamp):
        """
        Sets the DeletionTimestamp of this V1ObjectMeta.
        DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource will be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field. Once set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. Once the resource is deleted in the API, the Kubelet will send a hard termination signal to the container. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param DeletionTimestamp: The DeletionTimestamp of this V1ObjectMeta.
        :type: datetime
        """

        self._DeletionTimestamp = DeletionTimestamp

    @property
    def DeletionGracePeriodSeconds(self):
        """
        Gets the DeletionGracePeriodSeconds of this V1ObjectMeta.
        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.

        :return: The DeletionGracePeriodSeconds of this V1ObjectMeta.
        :rtype: int
        """
        return self._DeletionGracePeriodSeconds

    @DeletionGracePeriodSeconds.setter
    def DeletionGracePeriodSeconds(self, DeletionGracePeriodSeconds):
        """
        Sets the DeletionGracePeriodSeconds of this V1ObjectMeta.
        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.

        :param DeletionGracePeriodSeconds: The DeletionGracePeriodSeconds of this V1ObjectMeta.
        :type: int
        """

        self._DeletionGracePeriodSeconds = DeletionGracePeriodSeconds

    @property
    def Labels(self):
        """
        Gets the Labels of this V1ObjectMeta.
        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://releases.k8s.io/HEAD/docs/user-guide/labels.md

        :return: The Labels of this V1ObjectMeta.
        :rtype: object
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        """
        Sets the Labels of this V1ObjectMeta.
        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://releases.k8s.io/HEAD/docs/user-guide/labels.md

        :param Labels: The Labels of this V1ObjectMeta.
        :type: object
        """

        self._Labels = Labels

    @property
    def Annotations(self):
        """
        Gets the Annotations of this V1ObjectMeta.
        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://releases.k8s.io/HEAD/docs/user-guide/annotations.md

        :return: The Annotations of this V1ObjectMeta.
        :rtype: object
        """
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        """
        Sets the Annotations of this V1ObjectMeta.
        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://releases.k8s.io/HEAD/docs/user-guide/annotations.md

        :param Annotations: The Annotations of this V1ObjectMeta.
        :type: object
        """

        self._Annotations = Annotations

    @property
    def OwnerReferences(self):
        """
        Gets the OwnerReferences of this V1ObjectMeta.
        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

        :return: The OwnerReferences of this V1ObjectMeta.
        :rtype: list[V1OwnerReference]
        """
        return self._OwnerReferences

    @OwnerReferences.setter
    def OwnerReferences(self, OwnerReferences):
        """
        Sets the OwnerReferences of this V1ObjectMeta.
        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

        :param OwnerReferences: The OwnerReferences of this V1ObjectMeta.
        :type: list[V1OwnerReference]
        """

        self._OwnerReferences = OwnerReferences

    @property
    def Finalizers(self):
        """
        Gets the Finalizers of this V1ObjectMeta.
        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.

        :return: The Finalizers of this V1ObjectMeta.
        :rtype: list[str]
        """
        return self._Finalizers

    @Finalizers.setter
    def Finalizers(self, Finalizers):
        """
        Sets the Finalizers of this V1ObjectMeta.
        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.

        :param Finalizers: The Finalizers of this V1ObjectMeta.
        :type: list[str]
        """

        self._Finalizers = Finalizers

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
