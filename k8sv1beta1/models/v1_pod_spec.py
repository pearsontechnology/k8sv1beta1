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
    def __init__(self, volumes=None, containers=None, restartPolicy=None, terminationGracePeriodSeconds=None, activeDeadlineSeconds=None, dnsPolicy=None, nodeSelector=None, serviceAccountName=None, serviceAccount=None, nodeName=None, hostNetwork=None, hostPID=None, hostIPC=None, securityContext=None, imagePullSecrets=None, hostname=None, subdomain=None):
        """
        V1PodSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'volumes': 'list[V1Volume]',
            'containers': 'list[V1Container]',
            'restartPolicy': 'str',
            'terminationGracePeriodSeconds': 'int',
            'activeDeadlineSeconds': 'int',
            'dnsPolicy': 'str',
            'nodeSelector': 'object',
            'serviceAccountName': 'str',
            'serviceAccount': 'str',
            'nodeName': 'str',
            'hostNetwork': 'bool',
            'hostPID': 'bool',
            'hostIPC': 'bool',
            'securityContext': 'V1PodSecurityContext',
            'imagePullSecrets': 'list[V1LocalObjectReference]',
            'hostname': 'str',
            'subdomain': 'str'
        }

        self.attribute_map = {
            'volumes': 'volumes',
            'containers': 'containers',
            'restartPolicy': 'restartPolicy',
            'terminationGracePeriodSeconds': 'terminationGracePeriodSeconds',
            'activeDeadlineSeconds': 'activeDeadlineSeconds',
            'dnsPolicy': 'dnsPolicy',
            'nodeSelector': 'nodeSelector',
            'serviceAccountName': 'serviceAccountName',
            'serviceAccount': 'serviceAccount',
            'nodeName': 'nodeName',
            'hostNetwork': 'hostNetwork',
            'hostPID': 'hostPID',
            'hostIPC': 'hostIPC',
            'securityContext': 'securityContext',
            'imagePullSecrets': 'imagePullSecrets',
            'hostname': 'hostname',
            'subdomain': 'subdomain'
        }

        self._volumes = volumes
        self._containers = containers
        self._restartPolicy = restartPolicy
        self._terminationGracePeriodSeconds = terminationGracePeriodSeconds
        self._activeDeadlineSeconds = activeDeadlineSeconds
        self._dnsPolicy = dnsPolicy
        self._nodeSelector = nodeSelector
        self._serviceAccountName = serviceAccountName
        self._serviceAccount = serviceAccount
        self._nodeName = nodeName
        self._hostNetwork = hostNetwork
        self._hostPID = hostPID
        self._hostIPC = hostIPC
        self._securityContext = securityContext
        self._imagePullSecrets = imagePullSecrets
        self._hostname = hostname
        self._subdomain = subdomain

    @property
    def volumes(self):
        """
        Gets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://kubernetes.io/docs/user-guide/volumes

        :return: The volumes of this V1PodSpec.
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: http://kubernetes.io/docs/user-guide/volumes

        :param volumes: The volumes of this V1PodSpec.
        :type: list[V1Volume]
        """

        self._volumes = volumes

    @property
    def containers(self):
        """
        Gets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers

        :return: The containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/containers

        :param containers: The containers of this V1PodSpec.
        :type: list[V1Container]
        """

        self._containers = containers

    @property
    def restartPolicy(self):
        """
        Gets the restartPolicy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://kubernetes.io/docs/user-guide/pod-states#restartpolicy

        :return: The restartPolicy of this V1PodSpec.
        :rtype: str
        """
        return self._restartPolicy

    @restartPolicy.setter
    def restartPolicy(self, restartPolicy):
        """
        Sets the restartPolicy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: http://kubernetes.io/docs/user-guide/pod-states#restartpolicy

        :param restartPolicy: The restartPolicy of this V1PodSpec.
        :type: str
        """

        self._restartPolicy = restartPolicy

    @property
    def terminationGracePeriodSeconds(self):
        """
        Gets the terminationGracePeriodSeconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :return: The terminationGracePeriodSeconds of this V1PodSpec.
        :rtype: int
        """
        return self._terminationGracePeriodSeconds

    @terminationGracePeriodSeconds.setter
    def terminationGracePeriodSeconds(self, terminationGracePeriodSeconds):
        """
        Sets the terminationGracePeriodSeconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :param terminationGracePeriodSeconds: The terminationGracePeriodSeconds of this V1PodSpec.
        :type: int
        """

        self._terminationGracePeriodSeconds = terminationGracePeriodSeconds

    @property
    def activeDeadlineSeconds(self):
        """
        Gets the activeDeadlineSeconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :return: The activeDeadlineSeconds of this V1PodSpec.
        :rtype: int
        """
        return self._activeDeadlineSeconds

    @activeDeadlineSeconds.setter
    def activeDeadlineSeconds(self, activeDeadlineSeconds):
        """
        Sets the activeDeadlineSeconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :param activeDeadlineSeconds: The activeDeadlineSeconds of this V1PodSpec.
        :type: int
        """

        self._activeDeadlineSeconds = activeDeadlineSeconds

    @property
    def dnsPolicy(self):
        """
        Gets the dnsPolicy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :return: The dnsPolicy of this V1PodSpec.
        :rtype: str
        """
        return self._dnsPolicy

    @dnsPolicy.setter
    def dnsPolicy(self, dnsPolicy):
        """
        Sets the dnsPolicy of this V1PodSpec.
        Set DNS policy for containers within the pod. One of 'ClusterFirst' or 'Default'. Defaults to \"ClusterFirst\".

        :param dnsPolicy: The dnsPolicy of this V1PodSpec.
        :type: str
        """

        self._dnsPolicy = dnsPolicy

    @property
    def nodeSelector(self):
        """
        Gets the nodeSelector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://kubernetes.io/docs/user-guide/node-selection/README

        :return: The nodeSelector of this V1PodSpec.
        :rtype: object
        """
        return self._nodeSelector

    @nodeSelector.setter
    def nodeSelector(self, nodeSelector):
        """
        Sets the nodeSelector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: http://kubernetes.io/docs/user-guide/node-selection/README

        :param nodeSelector: The nodeSelector of this V1PodSpec.
        :type: object
        """

        self._nodeSelector = nodeSelector

    @property
    def serviceAccountName(self):
        """
        Gets the serviceAccountName of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :return: The serviceAccountName of this V1PodSpec.
        :rtype: str
        """
        return self._serviceAccountName

    @serviceAccountName.setter
    def serviceAccountName(self, serviceAccountName):
        """
        Sets the serviceAccountName of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: http://releases.k8s.io/HEAD/docs/design/service_accounts.md

        :param serviceAccountName: The serviceAccountName of this V1PodSpec.
        :type: str
        """

        self._serviceAccountName = serviceAccountName

    @property
    def serviceAccount(self):
        """
        Gets the serviceAccount of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :return: The serviceAccount of this V1PodSpec.
        :rtype: str
        """
        return self._serviceAccount

    @serviceAccount.setter
    def serviceAccount(self, serviceAccount):
        """
        Sets the serviceAccount of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :param serviceAccount: The serviceAccount of this V1PodSpec.
        :type: str
        """

        self._serviceAccount = serviceAccount

    @property
    def nodeName(self):
        """
        Gets the nodeName of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :return: The nodeName of this V1PodSpec.
        :rtype: str
        """
        return self._nodeName

    @nodeName.setter
    def nodeName(self, nodeName):
        """
        Sets the nodeName of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :param nodeName: The nodeName of this V1PodSpec.
        :type: str
        """

        self._nodeName = nodeName

    @property
    def hostNetwork(self):
        """
        Gets the hostNetwork of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :return: The hostNetwork of this V1PodSpec.
        :rtype: bool
        """
        return self._hostNetwork

    @hostNetwork.setter
    def hostNetwork(self, hostNetwork):
        """
        Sets the hostNetwork of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :param hostNetwork: The hostNetwork of this V1PodSpec.
        :type: bool
        """

        self._hostNetwork = hostNetwork

    @property
    def hostPID(self):
        """
        Gets the hostPID of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :return: The hostPID of this V1PodSpec.
        :rtype: bool
        """
        return self._hostPID

    @hostPID.setter
    def hostPID(self, hostPID):
        """
        Sets the hostPID of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :param hostPID: The hostPID of this V1PodSpec.
        :type: bool
        """

        self._hostPID = hostPID

    @property
    def hostIPC(self):
        """
        Gets the hostIPC of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :return: The hostIPC of this V1PodSpec.
        :rtype: bool
        """
        return self._hostIPC

    @hostIPC.setter
    def hostIPC(self, hostIPC):
        """
        Sets the hostIPC of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :param hostIPC: The hostIPC of this V1PodSpec.
        :type: bool
        """

        self._hostIPC = hostIPC

    @property
    def securityContext(self):
        """
        Gets the securityContext of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :return: The securityContext of this V1PodSpec.
        :rtype: V1PodSecurityContext
        """
        return self._securityContext

    @securityContext.setter
    def securityContext(self, securityContext):
        """
        Sets the securityContext of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :param securityContext: The securityContext of this V1PodSpec.
        :type: V1PodSecurityContext
        """

        self._securityContext = securityContext

    @property
    def imagePullSecrets(self):
        """
        Gets the imagePullSecrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod

        :return: The imagePullSecrets of this V1PodSpec.
        :rtype: list[V1LocalObjectReference]
        """
        return self._imagePullSecrets

    @imagePullSecrets.setter
    def imagePullSecrets(self, imagePullSecrets):
        """
        Sets the imagePullSecrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: http://kubernetes.io/docs/user-guide/images#specifying-imagepullsecrets-on-a-pod

        :param imagePullSecrets: The imagePullSecrets of this V1PodSpec.
        :type: list[V1LocalObjectReference]
        """

        self._imagePullSecrets = imagePullSecrets

    @property
    def hostname(self):
        """
        Gets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :return: The hostname of this V1PodSpec.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :param hostname: The hostname of this V1PodSpec.
        :type: str
        """

        self._hostname = hostname

    @property
    def subdomain(self):
        """
        Gets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :return: The subdomain of this V1PodSpec.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :param subdomain: The subdomain of this V1PodSpec.
        :type: str
        """

        self._subdomain = subdomain

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
