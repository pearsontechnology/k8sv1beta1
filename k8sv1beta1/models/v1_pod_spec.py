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


class V1PodSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, Volumes=None, Containers=None, RestartPolicy=None, TerminationGracePeriodSeconds=None, ActiveDeadlineSeconds=None, DnsPolicy=None, NodeSelector=None, ServiceAccountName=None, ServiceAccount=None, NodeName=None, HostNetwork=None, HostPID=None, HostIPC=None, SecurityContext=None, ImagePullSecrets=None, Hostname=None, Subdomain=None):
        """
        V1PodSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'Volumes': 'list[V1Volume]',
            'Containers': 'list[V1Container]',
            'RestartPolicy': 'str',
            'TerminationGracePeriodSeconds': 'int',
            'ActiveDeadlineSeconds': 'int',
            'DnsPolicy': 'str',
            'NodeSelector': 'object',
            'ServiceAccountName': 'str',
            'ServiceAccount': 'str',
            'NodeName': 'str',
            'HostNetwork': 'bool',
            'HostPID': 'bool',
            'HostIPC': 'bool',
            'SecurityContext': 'V1PodSecurityContext',
            'ImagePullSecrets': 'list[V1LocalObjectReference]',
            'Hostname': 'str',
            'Subdomain': 'str'
        }

        self.attribute_map = {
            'Volumes': 'volumes',
            'Containers': 'containers',
            'RestartPolicy': 'restartPolicy',
            'TerminationGracePeriodSeconds': 'terminationGracePeriodSeconds',
            'ActiveDeadlineSeconds': 'activeDeadlineSeconds',
            'DnsPolicy': 'dnsPolicy',
            'NodeSelector': 'nodeSelector',
            'ServiceAccountName': 'serviceAccountName',
            'ServiceAccount': 'serviceAccount',
            'NodeName': 'nodeName',
            'HostNetwork': 'hostNetwork',
            'HostPID': 'hostPID',
            'HostIPC': 'hostIPC',
            'SecurityContext': 'securityContext',
            'ImagePullSecrets': 'imagePullSecrets',
            'Hostname': 'hostname',
            'Subdomain': 'subdomain'
        }

        self._Volumes = Volumes
        self._Containers = Containers
        self._RestartPolicy = RestartPolicy
        self._TerminationGracePeriodSeconds = TerminationGracePeriodSeconds
        self._ActiveDeadlineSeconds = ActiveDeadlineSeconds
        self._DnsPolicy = DnsPolicy
        self._NodeSelector = NodeSelector
        self._ServiceAccountName = ServiceAccountName
        self._ServiceAccount = ServiceAccount
        self._NodeName = NodeName
        self._HostNetwork = HostNetwork
        self._HostPID = HostPID
        self._HostIPC = HostIPC
        self._SecurityContext = SecurityContext
        self._ImagePullSecrets = ImagePullSecrets
        self._Hostname = Hostname
        self._Subdomain = Subdomain

    @property
    def Volumes(self):
        """
        Gets the Volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md

        :return: The Volumes of this V1PodSpec.
        :rtype: list[V1Volume]
        """
        return self._Volumes

    @Volumes.setter
    def Volumes(self, Volumes):
        """
        Sets the Volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://releases.k8s.io/HEAD/docs/user-guide/volumes.md

        :param Volumes: The Volumes of this V1PodSpec.
        :type: list[V1Volume]
        """

        self._Volumes = Volumes

    @property
    def Containers(self):
        """
        Gets the Containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md

        :return: The Containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._Containers

    @Containers.setter
    def Containers(self, Containers):
        """
        Sets the Containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md

        :param Containers: The Containers of this V1PodSpec.
        :type: list[V1Container]
        """

        self._Containers = Containers

    @property
    def RestartPolicy(self):
        """
        Gets the RestartPolicy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#restartpolicy

        :return: The RestartPolicy of this V1PodSpec.
        :rtype: str
        """
        return self._RestartPolicy

    @RestartPolicy.setter
    def RestartPolicy(self, RestartPolicy):
        """
        Sets the RestartPolicy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#restartpolicy

        :param RestartPolicy: The RestartPolicy of this V1PodSpec.
        :type: str
        """

        self._RestartPolicy = RestartPolicy

    @property
    def TerminationGracePeriodSeconds(self):
        """
        Gets the TerminationGracePeriodSeconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :return: The TerminationGracePeriodSeconds of this V1PodSpec.
        :rtype: int
        """
        return self._TerminationGracePeriodSeconds

    @TerminationGracePeriodSeconds.setter
    def TerminationGracePeriodSeconds(self, TerminationGracePeriodSeconds):
        """
        Sets the TerminationGracePeriodSeconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :param TerminationGracePeriodSeconds: The TerminationGracePeriodSeconds of this V1PodSpec.
        :type: int
        """

        self._TerminationGracePeriodSeconds = TerminationGracePeriodSeconds

    @property
    def ActiveDeadlineSeconds(self):
        """
        Gets the ActiveDeadlineSeconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :return: The ActiveDeadlineSeconds of this V1PodSpec.
        :rtype: int
        """
        return self._ActiveDeadlineSeconds

    @ActiveDeadlineSeconds.setter
    def ActiveDeadlineSeconds(self, ActiveDeadlineSeconds):
        """
        Sets the ActiveDeadlineSeconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :param ActiveDeadlineSeconds: The ActiveDeadlineSeconds of this V1PodSpec.
        :type: int
        """

        self._ActiveDeadlineSeconds = ActiveDeadlineSeconds

    @property
    def DnsPolicy(self):
        """
        Gets the DnsPolicy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :return: The DnsPolicy of this V1PodSpec.
        :rtype: str
        """
        return self._DnsPolicy

    @DnsPolicy.setter
    def DnsPolicy(self, DnsPolicy):
        """
        Sets the DnsPolicy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :param DnsPolicy: The DnsPolicy of this V1PodSpec.
        :type: str
        """

        self._DnsPolicy = DnsPolicy

    @property
    def NodeSelector(self):
        """
        Gets the NodeSelector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://releases.k8s.io/HEAD/docs/user-guide/node-selection/README.md

        :return: The NodeSelector of this V1PodSpec.
        :rtype: object
        """
        return self._NodeSelector

    @NodeSelector.setter
    def NodeSelector(self, NodeSelector):
        """
        Sets the NodeSelector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://releases.k8s.io/HEAD/docs/user-guide/node-selection/README.md

        :param NodeSelector: The NodeSelector of this V1PodSpec.
        :type: object
        """

        self._NodeSelector = NodeSelector

    @property
    def ServiceAccountName(self):
        """
        Gets the ServiceAccountName of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :return: The ServiceAccountName of this V1PodSpec.
        :rtype: str
        """
        return self._ServiceAccountName

    @ServiceAccountName.setter
    def ServiceAccountName(self, ServiceAccountName):
        """
        Sets the ServiceAccountName of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :param ServiceAccountName: The ServiceAccountName of this V1PodSpec.
        :type: str
        """

        self._ServiceAccountName = ServiceAccountName

    @property
    def ServiceAccount(self):
        """
        Gets the ServiceAccount of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :return: The ServiceAccount of this V1PodSpec.
        :rtype: str
        """
        return self._ServiceAccount

    @ServiceAccount.setter
    def ServiceAccount(self, ServiceAccount):
        """
        Sets the ServiceAccount of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :param ServiceAccount: The ServiceAccount of this V1PodSpec.
        :type: str
        """

        self._ServiceAccount = ServiceAccount

    @property
    def NodeName(self):
        """
        Gets the NodeName of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :return: The NodeName of this V1PodSpec.
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        """
        Sets the NodeName of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :param NodeName: The NodeName of this V1PodSpec.
        :type: str
        """

        self._NodeName = NodeName

    @property
    def HostNetwork(self):
        """
        Gets the HostNetwork of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :return: The HostNetwork of this V1PodSpec.
        :rtype: bool
        """
        return self._HostNetwork

    @HostNetwork.setter
    def HostNetwork(self, HostNetwork):
        """
        Sets the HostNetwork of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :param HostNetwork: The HostNetwork of this V1PodSpec.
        :type: bool
        """

        self._HostNetwork = HostNetwork

    @property
    def HostPID(self):
        """
        Gets the HostPID of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :return: The HostPID of this V1PodSpec.
        :rtype: bool
        """
        return self._HostPID

    @HostPID.setter
    def HostPID(self, HostPID):
        """
        Sets the HostPID of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :param HostPID: The HostPID of this V1PodSpec.
        :type: bool
        """

        self._HostPID = HostPID

    @property
    def HostIPC(self):
        """
        Gets the HostIPC of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :return: The HostIPC of this V1PodSpec.
        :rtype: bool
        """
        return self._HostIPC

    @HostIPC.setter
    def HostIPC(self, HostIPC):
        """
        Sets the HostIPC of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :param HostIPC: The HostIPC of this V1PodSpec.
        :type: bool
        """

        self._HostIPC = HostIPC

    @property
    def SecurityContext(self):
        """
        Gets the SecurityContext of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :return: The SecurityContext of this V1PodSpec.
        :rtype: V1PodSecurityContext
        """
        return self._SecurityContext

    @SecurityContext.setter
    def SecurityContext(self, SecurityContext):
        """
        Sets the SecurityContext of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :param SecurityContext: The SecurityContext of this V1PodSpec.
        :type: V1PodSecurityContext
        """

        self._SecurityContext = SecurityContext

    @property
    def ImagePullSecrets(self):
        """
        Gets the ImagePullSecrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md#specifying-imagepullsecrets-on-a-pod

        :return: The ImagePullSecrets of this V1PodSpec.
        :rtype: list[V1LocalObjectReference]
        """
        return self._ImagePullSecrets

    @ImagePullSecrets.setter
    def ImagePullSecrets(self, ImagePullSecrets):
        """
        Sets the ImagePullSecrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md#specifying-imagepullsecrets-on-a-pod

        :param ImagePullSecrets: The ImagePullSecrets of this V1PodSpec.
        :type: list[V1LocalObjectReference]
        """

        self._ImagePullSecrets = ImagePullSecrets

    @property
    def Hostname(self):
        """
        Gets the Hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :return: The Hostname of this V1PodSpec.
        :rtype: str
        """
        return self._Hostname

    @Hostname.setter
    def Hostname(self, Hostname):
        """
        Sets the Hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :param Hostname: The Hostname of this V1PodSpec.
        :type: str
        """

        self._Hostname = Hostname

    @property
    def Subdomain(self):
        """
        Gets the Subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :return: The Subdomain of this V1PodSpec.
        :rtype: str
        """
        return self._Subdomain

    @Subdomain.setter
    def Subdomain(self, Subdomain):
        """
        Sets the Subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :param Subdomain: The Subdomain of this V1PodSpec.
        :type: str
        """

        self._Subdomain = Subdomain

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
