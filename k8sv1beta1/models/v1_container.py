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


class V1Container(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, image=None, command=None, args=None, workingDir=None, ports=None, env=None, resources=None, volumeMounts=None, livenessProbe=None, readinessProbe=None, lifecycle=None, terminationMessagePath=None, imagePullPolicy=None, securityContext=None, stdin=None, stdinOnce=None, tty=None):
        """
        V1Container - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'image': 'str',
            'command': 'list[str]',
            'args': 'list[str]',
            'workingDir': 'str',
            'ports': 'list[V1ContainerPort]',
            'env': 'list[V1EnvVar]',
            'resources': 'V1ResourceRequirements',
            'volumeMounts': 'list[V1VolumeMount]',
            'livenessProbe': 'V1Probe',
            'readinessProbe': 'V1Probe',
            'lifecycle': 'V1Lifecycle',
            'terminationMessagePath': 'str',
            'imagePullPolicy': 'str',
            'securityContext': 'V1SecurityContext',
            'stdin': 'bool',
            'stdinOnce': 'bool',
            'tty': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'image': 'image',
            'command': 'command',
            'args': 'args',
            'workingDir': 'workingDir',
            'ports': 'ports',
            'env': 'env',
            'resources': 'resources',
            'volumeMounts': 'volumeMounts',
            'livenessProbe': 'livenessProbe',
            'readinessProbe': 'readinessProbe',
            'lifecycle': 'lifecycle',
            'terminationMessagePath': 'terminationMessagePath',
            'imagePullPolicy': 'imagePullPolicy',
            'securityContext': 'securityContext',
            'stdin': 'stdin',
            'stdinOnce': 'stdinOnce',
            'tty': 'tty'
        }

        self._name = name
        self._image = image
        self._command = command
        self._args = args
        self._workingDir = workingDir
        self._ports = ports
        self._env = env
        self._resources = resources
        self._volumeMounts = volumeMounts
        self._livenessProbe = livenessProbe
        self._readinessProbe = readinessProbe
        self._lifecycle = lifecycle
        self._terminationMessagePath = terminationMessagePath
        self._imagePullPolicy = imagePullPolicy
        self._securityContext = securityContext
        self._stdin = stdin
        self._stdinOnce = stdinOnce
        self._tty = tty

    @property
    def name(self):
        """
        Gets the name of this V1Container.
        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :return: The name of this V1Container.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1Container.
        Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.

        :param name: The name of this V1Container.
        :type: str
        """

        self._name = name

    @property
    def image(self):
        """
        Gets the image of this V1Container.
        Docker image name. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :return: The image of this V1Container.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1Container.
        Docker image name. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md

        :param image: The image of this V1Container.
        :type: str
        """

        self._image = image

    @property
    def command(self):
        """
        Gets the command of this V1Container.
        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md#containers-and-commands

        :return: The command of this V1Container.
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this V1Container.
        Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md#containers-and-commands

        :param command: The command of this V1Container.
        :type: list[str]
        """

        self._command = command

    @property
    def args(self):
        """
        Gets the args of this V1Container.
        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md#containers-and-commands

        :return: The args of this V1Container.
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """
        Sets the args of this V1Container.
        Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/containers.md#containers-and-commands

        :param args: The args of this V1Container.
        :type: list[str]
        """

        self._args = args

    @property
    def workingDir(self):
        """
        Gets the workingDir of this V1Container.
        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :return: The workingDir of this V1Container.
        :rtype: str
        """
        return self._workingDir

    @workingDir.setter
    def workingDir(self, workingDir):
        """
        Sets the workingDir of this V1Container.
        Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.

        :param workingDir: The workingDir of this V1Container.
        :type: str
        """

        self._workingDir = workingDir

    @property
    def ports(self):
        """
        Gets the ports of this V1Container.
        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.

        :return: The ports of this V1Container.
        :rtype: list[V1ContainerPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1Container.
        List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Cannot be updated.

        :param ports: The ports of this V1Container.
        :type: list[V1ContainerPort]
        """

        self._ports = ports

    @property
    def env(self):
        """
        Gets the env of this V1Container.
        List of environment variables to set in the container. Cannot be updated.

        :return: The env of this V1Container.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1Container.
        List of environment variables to set in the container. Cannot be updated.

        :param env: The env of this V1Container.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def resources(self):
        """
        Gets the resources of this V1Container.
        Compute Resources required by this container. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#resources

        :return: The resources of this V1Container.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1Container.
        Compute Resources required by this container. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/persistent-volumes.md#resources

        :param resources: The resources of this V1Container.
        :type: V1ResourceRequirements
        """

        self._resources = resources

    @property
    def volumeMounts(self):
        """
        Gets the volumeMounts of this V1Container.
        Pod volumes to mount into the container's filesystem. Cannot be updated.

        :return: The volumeMounts of this V1Container.
        :rtype: list[V1VolumeMount]
        """
        return self._volumeMounts

    @volumeMounts.setter
    def volumeMounts(self, volumeMounts):
        """
        Sets the volumeMounts of this V1Container.
        Pod volumes to mount into the container's filesystem. Cannot be updated.

        :param volumeMounts: The volumeMounts of this V1Container.
        :type: list[V1VolumeMount]
        """

        self._volumeMounts = volumeMounts

    @property
    def livenessProbe(self):
        """
        Gets the livenessProbe of this V1Container.
        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#container-probes

        :return: The livenessProbe of this V1Container.
        :rtype: V1Probe
        """
        return self._livenessProbe

    @livenessProbe.setter
    def livenessProbe(self, livenessProbe):
        """
        Sets the livenessProbe of this V1Container.
        Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#container-probes

        :param livenessProbe: The livenessProbe of this V1Container.
        :type: V1Probe
        """

        self._livenessProbe = livenessProbe

    @property
    def readinessProbe(self):
        """
        Gets the readinessProbe of this V1Container.
        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#container-probes

        :return: The readinessProbe of this V1Container.
        :rtype: V1Probe
        """
        return self._readinessProbe

    @readinessProbe.setter
    def readinessProbe(self, readinessProbe):
        """
        Sets the readinessProbe of this V1Container.
        Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/pod-states.md#container-probes

        :param readinessProbe: The readinessProbe of this V1Container.
        :type: V1Probe
        """

        self._readinessProbe = readinessProbe

    @property
    def lifecycle(self):
        """
        Gets the lifecycle of this V1Container.
        Actions that the management system should take in response to container lifecycle events. Cannot be updated.

        :return: The lifecycle of this V1Container.
        :rtype: V1Lifecycle
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """
        Sets the lifecycle of this V1Container.
        Actions that the management system should take in response to container lifecycle events. Cannot be updated.

        :param lifecycle: The lifecycle of this V1Container.
        :type: V1Lifecycle
        """

        self._lifecycle = lifecycle

    @property
    def terminationMessagePath(self):
        """
        Gets the terminationMessagePath of this V1Container.
        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Defaults to /dev/termination-log. Cannot be updated.

        :return: The terminationMessagePath of this V1Container.
        :rtype: str
        """
        return self._terminationMessagePath

    @terminationMessagePath.setter
    def terminationMessagePath(self, terminationMessagePath):
        """
        Sets the terminationMessagePath of this V1Container.
        Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Defaults to /dev/termination-log. Cannot be updated.

        :param terminationMessagePath: The terminationMessagePath of this V1Container.
        :type: str
        """

        self._terminationMessagePath = terminationMessagePath

    @property
    def imagePullPolicy(self):
        """
        Gets the imagePullPolicy of this V1Container.
        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md#updating-images

        :return: The imagePullPolicy of this V1Container.
        :rtype: str
        """
        return self._imagePullPolicy

    @imagePullPolicy.setter
    def imagePullPolicy(self, imagePullPolicy):
        """
        Sets the imagePullPolicy of this V1Container.
        Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: http://releases.k8s.io/HEAD/docs/user-guide/images.md#updating-images

        :param imagePullPolicy: The imagePullPolicy of this V1Container.
        :type: str
        """

        self._imagePullPolicy = imagePullPolicy

    @property
    def securityContext(self):
        """
        Gets the securityContext of this V1Container.
        Security options the pod should run with. More info: http://releases.k8s.io/HEAD/docs/design/security_context.md

        :return: The securityContext of this V1Container.
        :rtype: V1SecurityContext
        """
        return self._securityContext

    @securityContext.setter
    def securityContext(self, securityContext):
        """
        Sets the securityContext of this V1Container.
        Security options the pod should run with. More info: http://releases.k8s.io/HEAD/docs/design/security_context.md

        :param securityContext: The securityContext of this V1Container.
        :type: V1SecurityContext
        """

        self._securityContext = securityContext

    @property
    def stdin(self):
        """
        Gets the stdin of this V1Container.
        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.

        :return: The stdin of this V1Container.
        :rtype: bool
        """
        return self._stdin

    @stdin.setter
    def stdin(self, stdin):
        """
        Sets the stdin of this V1Container.
        Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.

        :param stdin: The stdin of this V1Container.
        :type: bool
        """

        self._stdin = stdin

    @property
    def stdinOnce(self):
        """
        Gets the stdinOnce of this V1Container.
        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false

        :return: The stdinOnce of this V1Container.
        :rtype: bool
        """
        return self._stdinOnce

    @stdinOnce.setter
    def stdinOnce(self, stdinOnce):
        """
        Sets the stdinOnce of this V1Container.
        Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false

        :param stdinOnce: The stdinOnce of this V1Container.
        :type: bool
        """

        self._stdinOnce = stdinOnce

    @property
    def tty(self):
        """
        Gets the tty of this V1Container.
        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.

        :return: The tty of this V1Container.
        :rtype: bool
        """
        return self._tty

    @tty.setter
    def tty(self, tty):
        """
        Sets the tty of this V1Container.
        Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.

        :param tty: The tty of this V1Container.
        :type: bool
        """

        self._tty = tty

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
