# k8sv1beta1.ApisextensionsvbetaApi

All URIs are relative to *https://10.10.10.10:6443/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_daemon_set**](ApisextensionsvbetaApi.md#create_namespaced_daemon_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | create a DaemonSet
[**create_namespaced_deployment**](ApisextensionsvbetaApi.md#create_namespaced_deployment) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | create a Deployment
[**create_namespaced_deployment_rollback_rollback**](ApisextensionsvbetaApi.md#create_namespaced_deployment_rollback_rollback) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/rollback | create rollback of a DeploymentRollback
[**create_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#create_namespaced_horizontal_pod_autoscaler) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | create a HorizontalPodAutoscaler
[**create_namespaced_ingress**](ApisextensionsvbetaApi.md#create_namespaced_ingress) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | create an Ingress
[**create_namespaced_job**](ApisextensionsvbetaApi.md#create_namespaced_job) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | create a Job
[**create_namespaced_network_policy**](ApisextensionsvbetaApi.md#create_namespaced_network_policy) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | create a NetworkPolicy
[**create_namespaced_replica_set**](ApisextensionsvbetaApi.md#create_namespaced_replica_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | create a ReplicaSet
[**create_third_party_resource**](ApisextensionsvbetaApi.md#create_third_party_resource) | **POST** /apis/extensions/v1beta1/thirdpartyresources | create a ThirdPartyResource
[**delete_namespaced_daemon_set**](ApisextensionsvbetaApi.md#delete_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | delete a DaemonSet
[**delete_namespaced_deployment**](ApisextensionsvbetaApi.md#delete_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | delete a Deployment
[**delete_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#delete_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | delete a HorizontalPodAutoscaler
[**delete_namespaced_ingress**](ApisextensionsvbetaApi.md#delete_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | delete an Ingress
[**delete_namespaced_job**](ApisextensionsvbetaApi.md#delete_namespaced_job) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | delete a Job
[**delete_namespaced_network_policy**](ApisextensionsvbetaApi.md#delete_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | delete a NetworkPolicy
[**delete_namespaced_replica_set**](ApisextensionsvbetaApi.md#delete_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | delete a ReplicaSet
[**delete_third_party_resource**](ApisextensionsvbetaApi.md#delete_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources/{name} | delete a ThirdPartyResource
[**deletecollection_namespaced_daemon_set**](ApisextensionsvbetaApi.md#deletecollection_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | delete collection of DaemonSet
[**deletecollection_namespaced_deployment**](ApisextensionsvbetaApi.md#deletecollection_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | delete collection of Deployment
[**deletecollection_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#deletecollection_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | delete collection of HorizontalPodAutoscaler
[**deletecollection_namespaced_ingress**](ApisextensionsvbetaApi.md#deletecollection_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | delete collection of Ingress
[**deletecollection_namespaced_job**](ApisextensionsvbetaApi.md#deletecollection_namespaced_job) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | delete collection of Job
[**deletecollection_namespaced_network_policy**](ApisextensionsvbetaApi.md#deletecollection_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | delete collection of NetworkPolicy
[**deletecollection_namespaced_replica_set**](ApisextensionsvbetaApi.md#deletecollection_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | delete collection of ReplicaSet
[**deletecollection_third_party_resource**](ApisextensionsvbetaApi.md#deletecollection_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources | delete collection of ThirdPartyResource
[**get_api_resources**](ApisextensionsvbetaApi.md#get_api_resources) | **GET** /apis/extensions/v1beta1 | get available resources
[**list_daemon_set_for_all_namespaces**](ApisextensionsvbetaApi.md#list_daemon_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/daemonsets | list or watch objects of kind DaemonSet
[**list_deployment_for_all_namespaces**](ApisextensionsvbetaApi.md#list_deployment_for_all_namespaces) | **GET** /apis/extensions/v1beta1/deployments | list or watch objects of kind Deployment
[**list_horizontal_pod_autoscaler_for_all_namespaces**](ApisextensionsvbetaApi.md#list_horizontal_pod_autoscaler_for_all_namespaces) | **GET** /apis/extensions/v1beta1/horizontalpodautoscalers | list or watch objects of kind HorizontalPodAutoscaler
[**list_ingress_for_all_namespaces**](ApisextensionsvbetaApi.md#list_ingress_for_all_namespaces) | **GET** /apis/extensions/v1beta1/ingresses | list or watch objects of kind Ingress
[**list_job_for_all_namespaces**](ApisextensionsvbetaApi.md#list_job_for_all_namespaces) | **GET** /apis/extensions/v1beta1/jobs | list or watch objects of kind Job
[**list_namespaced_daemon_set**](ApisextensionsvbetaApi.md#list_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | list or watch objects of kind DaemonSet
[**list_namespaced_deployment**](ApisextensionsvbetaApi.md#list_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | list or watch objects of kind Deployment
[**list_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#list_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | list or watch objects of kind HorizontalPodAutoscaler
[**list_namespaced_ingress**](ApisextensionsvbetaApi.md#list_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | list or watch objects of kind Ingress
[**list_namespaced_job**](ApisextensionsvbetaApi.md#list_namespaced_job) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | list or watch objects of kind Job
[**list_namespaced_network_policy**](ApisextensionsvbetaApi.md#list_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | list or watch objects of kind NetworkPolicy
[**list_namespaced_replica_set**](ApisextensionsvbetaApi.md#list_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | list or watch objects of kind ReplicaSet
[**list_network_policy_for_all_namespaces**](ApisextensionsvbetaApi.md#list_network_policy_for_all_namespaces) | **GET** /apis/extensions/v1beta1/networkpolicies | list or watch objects of kind NetworkPolicy
[**list_replica_set_for_all_namespaces**](ApisextensionsvbetaApi.md#list_replica_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/replicasets | list or watch objects of kind ReplicaSet
[**list_third_party_resource**](ApisextensionsvbetaApi.md#list_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources | list or watch objects of kind ThirdPartyResource
[**patch_namespaced_daemon_set**](ApisextensionsvbetaApi.md#patch_namespaced_daemon_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | partially update the specified DaemonSet
[**patch_namespaced_daemon_set_status**](ApisextensionsvbetaApi.md#patch_namespaced_daemon_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | partially update status of the specified DaemonSet
[**patch_namespaced_deployment**](ApisextensionsvbetaApi.md#patch_namespaced_deployment) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | partially update the specified Deployment
[**patch_namespaced_deployment_status**](ApisextensionsvbetaApi.md#patch_namespaced_deployment_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | partially update status of the specified Deployment
[**patch_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#patch_namespaced_horizontal_pod_autoscaler) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | partially update the specified HorizontalPodAutoscaler
[**patch_namespaced_horizontal_pod_autoscaler_status**](ApisextensionsvbetaApi.md#patch_namespaced_horizontal_pod_autoscaler_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | partially update status of the specified HorizontalPodAutoscaler
[**patch_namespaced_ingress**](ApisextensionsvbetaApi.md#patch_namespaced_ingress) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | partially update the specified Ingress
[**patch_namespaced_ingress_status**](ApisextensionsvbetaApi.md#patch_namespaced_ingress_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | partially update status of the specified Ingress
[**patch_namespaced_job**](ApisextensionsvbetaApi.md#patch_namespaced_job) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | partially update the specified Job
[**patch_namespaced_job_status**](ApisextensionsvbetaApi.md#patch_namespaced_job_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | partially update status of the specified Job
[**patch_namespaced_network_policy**](ApisextensionsvbetaApi.md#patch_namespaced_network_policy) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | partially update the specified NetworkPolicy
[**patch_namespaced_replica_set**](ApisextensionsvbetaApi.md#patch_namespaced_replica_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | partially update the specified ReplicaSet
[**patch_namespaced_replica_set_status**](ApisextensionsvbetaApi.md#patch_namespaced_replica_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | partially update status of the specified ReplicaSet
[**patch_namespaced_scale_scale**](ApisextensionsvbetaApi.md#patch_namespaced_scale_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | partially update scale of the specified Scale
[**patch_namespaced_scale_scale_0**](ApisextensionsvbetaApi.md#patch_namespaced_scale_scale_0) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | partially update scale of the specified Scale
[**patch_namespaced_scale_scale_1**](ApisextensionsvbetaApi.md#patch_namespaced_scale_scale_1) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | partially update scale of the specified Scale
[**patch_third_party_resource**](ApisextensionsvbetaApi.md#patch_third_party_resource) | **PATCH** /apis/extensions/v1beta1/thirdpartyresources/{name} | partially update the specified ThirdPartyResource
[**read_namespaced_daemon_set**](ApisextensionsvbetaApi.md#read_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | read the specified DaemonSet
[**read_namespaced_daemon_set_status**](ApisextensionsvbetaApi.md#read_namespaced_daemon_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | read status of the specified DaemonSet
[**read_namespaced_deployment**](ApisextensionsvbetaApi.md#read_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | read the specified Deployment
[**read_namespaced_deployment_status**](ApisextensionsvbetaApi.md#read_namespaced_deployment_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | read status of the specified Deployment
[**read_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#read_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | read the specified HorizontalPodAutoscaler
[**read_namespaced_horizontal_pod_autoscaler_status**](ApisextensionsvbetaApi.md#read_namespaced_horizontal_pod_autoscaler_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | read status of the specified HorizontalPodAutoscaler
[**read_namespaced_ingress**](ApisextensionsvbetaApi.md#read_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | read the specified Ingress
[**read_namespaced_ingress_status**](ApisextensionsvbetaApi.md#read_namespaced_ingress_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | read status of the specified Ingress
[**read_namespaced_job**](ApisextensionsvbetaApi.md#read_namespaced_job) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | read the specified Job
[**read_namespaced_job_status**](ApisextensionsvbetaApi.md#read_namespaced_job_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | read status of the specified Job
[**read_namespaced_network_policy**](ApisextensionsvbetaApi.md#read_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | read the specified NetworkPolicy
[**read_namespaced_replica_set**](ApisextensionsvbetaApi.md#read_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | read the specified ReplicaSet
[**read_namespaced_replica_set_status**](ApisextensionsvbetaApi.md#read_namespaced_replica_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | read status of the specified ReplicaSet
[**read_namespaced_scale_scale**](ApisextensionsvbetaApi.md#read_namespaced_scale_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | read scale of the specified Scale
[**read_namespaced_scale_scale_0**](ApisextensionsvbetaApi.md#read_namespaced_scale_scale_0) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | read scale of the specified Scale
[**read_namespaced_scale_scale_1**](ApisextensionsvbetaApi.md#read_namespaced_scale_scale_1) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | read scale of the specified Scale
[**read_third_party_resource**](ApisextensionsvbetaApi.md#read_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources/{name} | read the specified ThirdPartyResource
[**replace_namespaced_daemon_set**](ApisextensionsvbetaApi.md#replace_namespaced_daemon_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | replace the specified DaemonSet
[**replace_namespaced_daemon_set_status**](ApisextensionsvbetaApi.md#replace_namespaced_daemon_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | replace status of the specified DaemonSet
[**replace_namespaced_deployment**](ApisextensionsvbetaApi.md#replace_namespaced_deployment) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | replace the specified Deployment
[**replace_namespaced_deployment_status**](ApisextensionsvbetaApi.md#replace_namespaced_deployment_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | replace status of the specified Deployment
[**replace_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#replace_namespaced_horizontal_pod_autoscaler) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | replace the specified HorizontalPodAutoscaler
[**replace_namespaced_horizontal_pod_autoscaler_status**](ApisextensionsvbetaApi.md#replace_namespaced_horizontal_pod_autoscaler_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | replace status of the specified HorizontalPodAutoscaler
[**replace_namespaced_ingress**](ApisextensionsvbetaApi.md#replace_namespaced_ingress) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | replace the specified Ingress
[**replace_namespaced_ingress_status**](ApisextensionsvbetaApi.md#replace_namespaced_ingress_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | replace status of the specified Ingress
[**replace_namespaced_job**](ApisextensionsvbetaApi.md#replace_namespaced_job) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | replace the specified Job
[**replace_namespaced_job_status**](ApisextensionsvbetaApi.md#replace_namespaced_job_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | replace status of the specified Job
[**replace_namespaced_network_policy**](ApisextensionsvbetaApi.md#replace_namespaced_network_policy) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | replace the specified NetworkPolicy
[**replace_namespaced_replica_set**](ApisextensionsvbetaApi.md#replace_namespaced_replica_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | replace the specified ReplicaSet
[**replace_namespaced_replica_set_status**](ApisextensionsvbetaApi.md#replace_namespaced_replica_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | replace status of the specified ReplicaSet
[**replace_namespaced_scale_scale**](ApisextensionsvbetaApi.md#replace_namespaced_scale_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | replace scale of the specified Scale
[**replace_namespaced_scale_scale_0**](ApisextensionsvbetaApi.md#replace_namespaced_scale_scale_0) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | replace scale of the specified Scale
[**replace_namespaced_scale_scale_1**](ApisextensionsvbetaApi.md#replace_namespaced_scale_scale_1) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | replace scale of the specified Scale
[**replace_third_party_resource**](ApisextensionsvbetaApi.md#replace_third_party_resource) | **PUT** /apis/extensions/v1beta1/thirdpartyresources/{name} | replace the specified ThirdPartyResource
[**watch_daemon_set_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_daemon_set_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/daemonsets | watch individual changes to a list of DaemonSet
[**watch_deployment_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_deployment_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/deployments | watch individual changes to a list of Deployment
[**watch_horizontal_pod_autoscaler_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_horizontal_pod_autoscaler_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/horizontalpodautoscalers | watch individual changes to a list of HorizontalPodAutoscaler
[**watch_ingress_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_ingress_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/ingresses | watch individual changes to a list of Ingress
[**watch_job_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_job_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/jobs | watch individual changes to a list of Job
[**watch_namespaced_daemon_set**](ApisextensionsvbetaApi.md#watch_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/daemonsets/{name} | watch changes to an object of kind DaemonSet
[**watch_namespaced_daemon_set_list**](ApisextensionsvbetaApi.md#watch_namespaced_daemon_set_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/daemonsets | watch individual changes to a list of DaemonSet
[**watch_namespaced_deployment**](ApisextensionsvbetaApi.md#watch_namespaced_deployment) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/deployments/{name} | watch changes to an object of kind Deployment
[**watch_namespaced_deployment_list**](ApisextensionsvbetaApi.md#watch_namespaced_deployment_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/deployments | watch individual changes to a list of Deployment
[**watch_namespaced_horizontal_pod_autoscaler**](ApisextensionsvbetaApi.md#watch_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name} | watch changes to an object of kind HorizontalPodAutoscaler
[**watch_namespaced_horizontal_pod_autoscaler_list**](ApisextensionsvbetaApi.md#watch_namespaced_horizontal_pod_autoscaler_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/horizontalpodautoscalers | watch individual changes to a list of HorizontalPodAutoscaler
[**watch_namespaced_ingress**](ApisextensionsvbetaApi.md#watch_namespaced_ingress) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/ingresses/{name} | watch changes to an object of kind Ingress
[**watch_namespaced_ingress_list**](ApisextensionsvbetaApi.md#watch_namespaced_ingress_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/ingresses | watch individual changes to a list of Ingress
[**watch_namespaced_job**](ApisextensionsvbetaApi.md#watch_namespaced_job) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/jobs/{name} | watch changes to an object of kind Job
[**watch_namespaced_job_list**](ApisextensionsvbetaApi.md#watch_namespaced_job_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/jobs | watch individual changes to a list of Job
[**watch_namespaced_network_policy**](ApisextensionsvbetaApi.md#watch_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/networkpolicies/{name} | watch changes to an object of kind NetworkPolicy
[**watch_namespaced_network_policy_list**](ApisextensionsvbetaApi.md#watch_namespaced_network_policy_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/networkpolicies | watch individual changes to a list of NetworkPolicy
[**watch_namespaced_replica_set**](ApisextensionsvbetaApi.md#watch_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/replicasets/{name} | watch changes to an object of kind ReplicaSet
[**watch_namespaced_replica_set_list**](ApisextensionsvbetaApi.md#watch_namespaced_replica_set_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/replicasets | watch individual changes to a list of ReplicaSet
[**watch_network_policy_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_network_policy_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/networkpolicies | watch individual changes to a list of NetworkPolicy
[**watch_replica_set_list_for_all_namespaces**](ApisextensionsvbetaApi.md#watch_replica_set_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/replicasets | watch individual changes to a list of ReplicaSet
[**watch_third_party_resource**](ApisextensionsvbetaApi.md#watch_third_party_resource) | **GET** /apis/extensions/v1beta1/watch/thirdpartyresources/{name} | watch changes to an object of kind ThirdPartyResource
[**watch_third_party_resource_list**](ApisextensionsvbetaApi.md#watch_third_party_resource_list) | **GET** /apis/extensions/v1beta1/watch/thirdpartyresources | watch individual changes to a list of ThirdPartyResource


# **create_namespaced_daemon_set**
> V1beta1DaemonSet create_namespaced_daemon_set(body, namespace, pretty=pretty)

create a DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1DaemonSet() # V1beta1DaemonSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a DaemonSet
    api_response = api_instance.create_namespaced_daemon_set(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment**
> V1beta1Deployment create_namespaced_deployment(body, namespace, pretty=pretty)

create a Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Deployment() # V1beta1Deployment | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Deployment
    api_response = api_instance.create_namespaced_deployment(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment_rollback_rollback**
> V1beta1DeploymentRollback create_namespaced_deployment_rollback_rollback(body, namespace, name, pretty=pretty)

create rollback of a DeploymentRollback

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1DeploymentRollback() # V1beta1DeploymentRollback | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DeploymentRollback
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create rollback of a DeploymentRollback
    api_response = api_instance.create_namespaced_deployment_rollback_rollback(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_deployment_rollback_rollback: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DeploymentRollback**](V1beta1DeploymentRollback.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DeploymentRollback | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DeploymentRollback**](V1beta1DeploymentRollback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler create_namespaced_horizontal_pod_autoscaler(body, namespace, pretty=pretty)

create a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a HorizontalPodAutoscaler
    api_response = api_instance.create_namespaced_horizontal_pod_autoscaler(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_ingress**
> V1beta1Ingress create_namespaced_ingress(body, namespace, pretty=pretty)

create an Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Ingress() # V1beta1Ingress | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create an Ingress
    api_response = api_instance.create_namespaced_ingress(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_job**
> V1beta1Job create_namespaced_job(body, namespace, pretty=pretty)

create a Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Job() # V1beta1Job | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a Job
    api_response = api_instance.create_namespaced_job(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_network_policy**
> V1beta1NetworkPolicy create_namespaced_network_policy(body, namespace, pretty=pretty)

create a NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a NetworkPolicy
    api_response = api_instance.create_namespaced_network_policy(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_replica_set**
> V1beta1ReplicaSet create_namespaced_replica_set(body, namespace, pretty=pretty)

create a ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ReplicaSet
    api_response = api_instance.create_namespaced_replica_set(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_third_party_resource**
> V1beta1ThirdPartyResource create_third_party_resource(body, pretty=pretty)

create a ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # create a ThirdPartyResource
    api_response = api_instance.create_third_party_resource(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->create_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_daemon_set**
> UnversionedStatus delete_namespaced_daemon_set(body, namespace, name, pretty=pretty)

delete a DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a DaemonSet
    api_response = api_instance.delete_namespaced_daemon_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_deployment**
> UnversionedStatus delete_namespaced_deployment(body, namespace, name, pretty=pretty)

delete a Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Deployment
    api_response = api_instance.delete_namespaced_deployment(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus delete_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

delete a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a HorizontalPodAutoscaler
    api_response = api_instance.delete_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_ingress**
> UnversionedStatus delete_namespaced_ingress(body, namespace, name, pretty=pretty)

delete an Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete an Ingress
    api_response = api_instance.delete_namespaced_ingress(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_job**
> UnversionedStatus delete_namespaced_job(body, namespace, name, pretty=pretty)

delete a Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a Job
    api_response = api_instance.delete_namespaced_job(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_network_policy**
> UnversionedStatus delete_namespaced_network_policy(body, namespace, name, pretty=pretty)

delete a NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the NetworkPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a NetworkPolicy
    api_response = api_instance.delete_namespaced_network_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the NetworkPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_replica_set**
> UnversionedStatus delete_namespaced_replica_set(body, namespace, name, pretty=pretty)

delete a ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ReplicaSet
    api_response = api_instance.delete_namespaced_replica_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_third_party_resource**
> UnversionedStatus delete_third_party_resource(body, name, pretty=pretty)

delete a ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1DeleteOptions() # V1DeleteOptions | 
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # delete a ThirdPartyResource
    api_response = api_instance.delete_third_party_resource(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->delete_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_daemon_set**
> UnversionedStatus deletecollection_namespaced_daemon_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of DaemonSet
    api_response = api_instance.deletecollection_namespaced_daemon_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_deployment**
> UnversionedStatus deletecollection_namespaced_deployment(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Deployment
    api_response = api_instance.deletecollection_namespaced_deployment(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of HorizontalPodAutoscaler
    api_response = api_instance.deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_ingress**
> UnversionedStatus deletecollection_namespaced_ingress(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Ingress
    api_response = api_instance.deletecollection_namespaced_ingress(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_job**
> UnversionedStatus deletecollection_namespaced_job(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of Job
    api_response = api_instance.deletecollection_namespaced_job(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_network_policy**
> UnversionedStatus deletecollection_namespaced_network_policy(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of NetworkPolicy
    api_response = api_instance.deletecollection_namespaced_network_policy(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_replica_set**
> UnversionedStatus deletecollection_namespaced_replica_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ReplicaSet
    api_response = api_instance.deletecollection_namespaced_replica_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_third_party_resource**
> UnversionedStatus deletecollection_third_party_resource(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

delete collection of ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # delete collection of ThirdPartyResource
    api_response = api_instance.deletecollection_third_party_resource(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->deletecollection_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> UnversionedAPIResourceList get_api_resources()

get available resources

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()

try: 
    # get available resources
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->get_api_resources: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIResourceList**](UnversionedAPIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_daemon_set_for_all_namespaces**
> V1beta1DaemonSetList list_daemon_set_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DaemonSet
    api_response = api_instance.list_daemon_set_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_daemon_set_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployment_for_all_namespaces**
> V1beta1DeploymentList list_deployment_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Deployment
    api_response = api_instance.list_deployment_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_deployment_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1DeploymentList**](V1beta1DeploymentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_horizontal_pod_autoscaler_for_all_namespaces**
> V1beta1HorizontalPodAutoscalerList list_horizontal_pod_autoscaler_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HorizontalPodAutoscaler
    api_response = api_instance.list_horizontal_pod_autoscaler_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_horizontal_pod_autoscaler_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscalerList**](V1beta1HorizontalPodAutoscalerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingress_for_all_namespaces**
> V1beta1IngressList list_ingress_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Ingress
    api_response = api_instance.list_ingress_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_ingress_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_for_all_namespaces**
> V1beta1JobList list_job_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Job
    api_response = api_instance.list_job_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_job_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1JobList**](V1beta1JobList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_daemon_set**
> V1beta1DaemonSetList list_namespaced_daemon_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind DaemonSet
    api_response = api_instance.list_namespaced_daemon_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_deployment**
> V1beta1DeploymentList list_namespaced_deployment(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Deployment
    api_response = api_instance.list_namespaced_deployment(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1DeploymentList**](V1beta1DeploymentList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscalerList list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind HorizontalPodAutoscaler
    api_response = api_instance.list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscalerList**](V1beta1HorizontalPodAutoscalerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_ingress**
> V1beta1IngressList list_namespaced_ingress(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Ingress
    api_response = api_instance.list_namespaced_ingress(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_job**
> V1beta1JobList list_namespaced_job(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind Job
    api_response = api_instance.list_namespaced_job(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1JobList**](V1beta1JobList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_network_policy**
> V1beta1NetworkPolicyList list_namespaced_network_policy(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind NetworkPolicy
    api_response = api_instance.list_namespaced_network_policy(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_replica_set**
> V1beta1ReplicaSetList list_namespaced_replica_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ReplicaSet
    api_response = api_instance.list_namespaced_replica_set(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_policy_for_all_namespaces**
> V1beta1NetworkPolicyList list_network_policy_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind NetworkPolicy
    api_response = api_instance.list_network_policy_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_network_policy_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replica_set_for_all_namespaces**
> V1beta1ReplicaSetList list_replica_set_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ReplicaSet
    api_response = api_instance.list_replica_set_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_replica_set_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_third_party_resource**
> V1beta1ThirdPartyResourceList list_third_party_resource(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

list or watch objects of kind ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # list or watch objects of kind ThirdPartyResource
    api_response = api_instance.list_third_party_resource(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->list_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**V1beta1ThirdPartyResourceList**](V1beta1ThirdPartyResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set**
> V1beta1DaemonSet patch_namespaced_daemon_set(body, namespace, name, pretty=pretty)

partially update the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified DaemonSet
    api_response = api_instance.patch_namespaced_daemon_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set_status**
> V1beta1DaemonSet patch_namespaced_daemon_set_status(body, namespace, name, pretty=pretty)

partially update status of the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified DaemonSet
    api_response = api_instance.patch_namespaced_daemon_set_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment**
> V1beta1Deployment patch_namespaced_deployment(body, namespace, name, pretty=pretty)

partially update the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Deployment
    api_response = api_instance.patch_namespaced_deployment(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment_status**
> V1beta1Deployment patch_namespaced_deployment_status(body, namespace, name, pretty=pretty)

partially update status of the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified Deployment
    api_response = api_instance.patch_namespaced_deployment_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

partially update the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified HorizontalPodAutoscaler
    api_response = api_instance.patch_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)

partially update status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified HorizontalPodAutoscaler
    api_response = api_instance.patch_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress**
> V1beta1Ingress patch_namespaced_ingress(body, namespace, name, pretty=pretty)

partially update the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Ingress
    api_response = api_instance.patch_namespaced_ingress(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress_status**
> V1beta1Ingress patch_namespaced_ingress_status(body, namespace, name, pretty=pretty)

partially update status of the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified Ingress
    api_response = api_instance.patch_namespaced_ingress_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job**
> V1beta1Job patch_namespaced_job(body, namespace, name, pretty=pretty)

partially update the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified Job
    api_response = api_instance.patch_namespaced_job(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job_status**
> V1beta1Job patch_namespaced_job_status(body, namespace, name, pretty=pretty)

partially update status of the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified Job
    api_response = api_instance.patch_namespaced_job_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_network_policy**
> V1beta1NetworkPolicy patch_namespaced_network_policy(body, namespace, name, pretty=pretty)

partially update the specified NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the NetworkPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified NetworkPolicy
    api_response = api_instance.patch_namespaced_network_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the NetworkPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set**
> V1beta1ReplicaSet patch_namespaced_replica_set(body, namespace, name, pretty=pretty)

partially update the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ReplicaSet
    api_response = api_instance.patch_namespaced_replica_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set_status**
> V1beta1ReplicaSet patch_namespaced_replica_set_status(body, namespace, name, pretty=pretty)

partially update status of the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update status of the specified ReplicaSet
    api_response = api_instance.patch_namespaced_replica_set_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scale_scale**
> V1beta1Scale patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scale_scale_0**
> V1beta1Scale patch_namespaced_scale_scale_0(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_scale_scale_0(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_scale_scale_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scale_scale_1**
> V1beta1Scale patch_namespaced_scale_scale_1(body, namespace, name, pretty=pretty)

partially update scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update scale of the specified Scale
    api_response = api_instance.patch_namespaced_scale_scale_1(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_namespaced_scale_scale_1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_third_party_resource**
> V1beta1ThirdPartyResource patch_third_party_resource(body, name, pretty=pretty)

partially update the specified ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.UnversionedPatch() # UnversionedPatch | 
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # partially update the specified ThirdPartyResource
    api_response = api_instance.patch_third_party_resource(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->patch_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set**
> V1beta1DaemonSet read_namespaced_daemon_set(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified DaemonSet
    api_response = api_instance.read_namespaced_daemon_set(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set_status**
> V1beta1DaemonSet read_namespaced_daemon_set_status(namespace, name, pretty=pretty)

read status of the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified DaemonSet
    api_response = api_instance.read_namespaced_daemon_set_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment**
> V1beta1Deployment read_namespaced_deployment(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Deployment
    api_response = api_instance.read_namespaced_deployment(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_status**
> V1beta1Deployment read_namespaced_deployment_status(namespace, name, pretty=pretty)

read status of the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified Deployment
    api_response = api_instance.read_namespaced_deployment_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified HorizontalPodAutoscaler
    api_response = api_instance.read_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler_status(namespace, name, pretty=pretty)

read status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified HorizontalPodAutoscaler
    api_response = api_instance.read_namespaced_horizontal_pod_autoscaler_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress**
> V1beta1Ingress read_namespaced_ingress(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Ingress
    api_response = api_instance.read_namespaced_ingress(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress_status**
> V1beta1Ingress read_namespaced_ingress_status(namespace, name, pretty=pretty)

read status of the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified Ingress
    api_response = api_instance.read_namespaced_ingress_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job**
> V1beta1Job read_namespaced_job(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified Job
    api_response = api_instance.read_namespaced_job(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job_status**
> V1beta1Job read_namespaced_job_status(namespace, name, pretty=pretty)

read status of the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified Job
    api_response = api_instance.read_namespaced_job_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_network_policy**
> V1beta1NetworkPolicy read_namespaced_network_policy(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the NetworkPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified NetworkPolicy
    api_response = api_instance.read_namespaced_network_policy(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the NetworkPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set**
> V1beta1ReplicaSet read_namespaced_replica_set(namespace, name, pretty=pretty, export=export, exact=exact)

read the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ReplicaSet
    api_response = api_instance.read_namespaced_replica_set(namespace, name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set_status**
> V1beta1ReplicaSet read_namespaced_replica_set_status(namespace, name, pretty=pretty)

read status of the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read status of the specified ReplicaSet
    api_response = api_instance.read_namespaced_replica_set_status(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scale_scale**
> V1beta1Scale read_namespaced_scale_scale(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.read_namespaced_scale_scale(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scale_scale_0**
> V1beta1Scale read_namespaced_scale_scale_0(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.read_namespaced_scale_scale_0(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_scale_scale_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scale_scale_1**
> V1beta1Scale read_namespaced_scale_scale_1(namespace, name, pretty=pretty)

read scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # read scale of the specified Scale
    api_response = api_instance.read_namespaced_scale_scale_1(namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_namespaced_scale_scale_1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_third_party_resource**
> V1beta1ThirdPartyResource read_third_party_resource(name, pretty=pretty, export=export, exact=exact)

read the specified ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)

try: 
    # read the specified ThirdPartyResource
    api_response = api_instance.read_third_party_resource(name, pretty=pretty, export=export, exact=exact)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->read_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set**
> V1beta1DaemonSet replace_namespaced_daemon_set(body, namespace, name, pretty=pretty)

replace the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1DaemonSet() # V1beta1DaemonSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified DaemonSet
    api_response = api_instance.replace_namespaced_daemon_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set_status**
> V1beta1DaemonSet replace_namespaced_daemon_set_status(body, namespace, name, pretty=pretty)

replace status of the specified DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1DaemonSet() # V1beta1DaemonSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified DaemonSet
    api_response = api_instance.replace_namespaced_daemon_set_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment**
> V1beta1Deployment replace_namespaced_deployment(body, namespace, name, pretty=pretty)

replace the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Deployment() # V1beta1Deployment | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Deployment
    api_response = api_instance.replace_namespaced_deployment(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment_status**
> V1beta1Deployment replace_namespaced_deployment_status(body, namespace, name, pretty=pretty)

replace status of the specified Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Deployment() # V1beta1Deployment | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Deployment
    api_response = api_instance.replace_namespaced_deployment_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)

replace the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified HorizontalPodAutoscaler
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)

replace status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified HorizontalPodAutoscaler
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress**
> V1beta1Ingress replace_namespaced_ingress(body, namespace, name, pretty=pretty)

replace the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Ingress() # V1beta1Ingress | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Ingress
    api_response = api_instance.replace_namespaced_ingress(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress_status**
> V1beta1Ingress replace_namespaced_ingress_status(body, namespace, name, pretty=pretty)

replace status of the specified Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Ingress() # V1beta1Ingress | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Ingress
    api_response = api_instance.replace_namespaced_ingress_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job**
> V1beta1Job replace_namespaced_job(body, namespace, name, pretty=pretty)

replace the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Job() # V1beta1Job | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified Job
    api_response = api_instance.replace_namespaced_job(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job_status**
> V1beta1Job replace_namespaced_job_status(body, namespace, name, pretty=pretty)

replace status of the specified Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Job() # V1beta1Job | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified Job
    api_response = api_instance.replace_namespaced_job_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_network_policy**
> V1beta1NetworkPolicy replace_namespaced_network_policy(body, namespace, name, pretty=pretty)

replace the specified NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the NetworkPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified NetworkPolicy
    api_response = api_instance.replace_namespaced_network_policy(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the NetworkPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set**
> V1beta1ReplicaSet replace_namespaced_replica_set(body, namespace, name, pretty=pretty)

replace the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ReplicaSet
    api_response = api_instance.replace_namespaced_replica_set(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set_status**
> V1beta1ReplicaSet replace_namespaced_replica_set_status(body, namespace, name, pretty=pretty)

replace status of the specified ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace status of the specified ReplicaSet
    api_response = api_instance.replace_namespaced_replica_set_status(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scale_scale**
> V1beta1Scale replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Scale() # V1beta1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_scale_scale(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_scale_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scale_scale_0**
> V1beta1Scale replace_namespaced_scale_scale_0(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Scale() # V1beta1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_scale_scale_0(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_scale_scale_0: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scale_scale_1**
> V1beta1Scale replace_namespaced_scale_scale_1(body, namespace, name, pretty=pretty)

replace scale of the specified Scale

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1Scale() # V1beta1Scale | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Scale
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace scale of the specified Scale
    api_response = api_instance.replace_namespaced_scale_scale_1(body, namespace, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_namespaced_scale_scale_1: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Scale | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_third_party_resource**
> V1beta1ThirdPartyResource replace_third_party_resource(body, name, pretty=pretty)

replace the specified ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
body = k8sv1beta1.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    # replace the specified ThirdPartyResource
    api_response = api_instance.replace_third_party_resource(body, name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->replace_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_daemon_set_list_for_all_namespaces**
> VersionedEvent watch_daemon_set_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DaemonSet
    api_response = api_instance.watch_daemon_set_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_daemon_set_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_deployment_list_for_all_namespaces**
> VersionedEvent watch_deployment_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Deployment
    api_response = api_instance.watch_deployment_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_deployment_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_horizontal_pod_autoscaler_list_for_all_namespaces**
> VersionedEvent watch_horizontal_pod_autoscaler_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HorizontalPodAutoscaler
    api_response = api_instance.watch_horizontal_pod_autoscaler_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_horizontal_pod_autoscaler_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_ingress_list_for_all_namespaces**
> VersionedEvent watch_ingress_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Ingress
    api_response = api_instance.watch_ingress_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_ingress_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_job_list_for_all_namespaces**
> VersionedEvent watch_job_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Job
    api_response = api_instance.watch_job_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_job_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_daemon_set**
> VersionedEvent watch_namespaced_daemon_set(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the DaemonSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind DaemonSet
    api_response = api_instance.watch_namespaced_daemon_set(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the DaemonSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_daemon_set_list**
> VersionedEvent watch_namespaced_daemon_set_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of DaemonSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of DaemonSet
    api_response = api_instance.watch_namespaced_daemon_set_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_daemon_set_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_deployment**
> VersionedEvent watch_namespaced_deployment(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Deployment
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Deployment
    api_response = api_instance.watch_namespaced_deployment(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Deployment | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_deployment_list**
> VersionedEvent watch_namespaced_deployment_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Deployment

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Deployment
    api_response = api_instance.watch_namespaced_deployment_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_deployment_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_horizontal_pod_autoscaler**
> VersionedEvent watch_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the HorizontalPodAutoscaler
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind HorizontalPodAutoscaler
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_horizontal_pod_autoscaler_list**
> VersionedEvent watch_namespaced_horizontal_pod_autoscaler_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of HorizontalPodAutoscaler
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_horizontal_pod_autoscaler_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_ingress**
> VersionedEvent watch_namespaced_ingress(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Ingress
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Ingress
    api_response = api_instance.watch_namespaced_ingress(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Ingress | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_ingress_list**
> VersionedEvent watch_namespaced_ingress_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Ingress

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Ingress
    api_response = api_instance.watch_namespaced_ingress_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_ingress_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_job**
> VersionedEvent watch_namespaced_job(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the Job
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind Job
    api_response = api_instance.watch_namespaced_job(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the Job | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_job_list**
> VersionedEvent watch_namespaced_job_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of Job

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of Job
    api_response = api_instance.watch_namespaced_job_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_job_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_network_policy**
> VersionedEvent watch_namespaced_network_policy(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the NetworkPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind NetworkPolicy
    api_response = api_instance.watch_namespaced_network_policy(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the NetworkPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_network_policy_list**
> VersionedEvent watch_namespaced_network_policy_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of NetworkPolicy
    api_response = api_instance.watch_namespaced_network_policy_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_network_policy_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_replica_set**
> VersionedEvent watch_namespaced_replica_set(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
name = 'name_example' # str | name of the ReplicaSet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ReplicaSet
    api_response = api_instance.watch_namespaced_replica_set(namespace, name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **name** | **str**| name of the ReplicaSet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_replica_set_list**
> VersionedEvent watch_namespaced_replica_set_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ReplicaSet
    api_response = api_instance.watch_namespaced_replica_set_list(namespace, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_namespaced_replica_set_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_network_policy_list_for_all_namespaces**
> VersionedEvent watch_network_policy_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of NetworkPolicy

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of NetworkPolicy
    api_response = api_instance.watch_network_policy_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_network_policy_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_replica_set_list_for_all_namespaces**
> VersionedEvent watch_replica_set_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of ReplicaSet

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ReplicaSet
    api_response = api_instance.watch_replica_set_list_for_all_namespaces(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_replica_set_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_third_party_resource**
> VersionedEvent watch_third_party_resource(name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch changes to an object of kind ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch changes to an object of kind ThirdPartyResource
    api_response = api_instance.watch_third_party_resource(name, pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_third_party_resource_list**
> VersionedEvent watch_third_party_resource_list(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)

watch individual changes to a list of ThirdPartyResource

### Example 
```python
import time
import k8sv1beta1
from k8sv1beta1.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = k8sv1beta1.ApisextensionsvbetaApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
labelSelector = 'labelSelector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
fieldSelector = 'fieldSelector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)
resourceVersion = 'resourceVersion_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeoutSeconds = 56 # int | Timeout for the list/watch call. (optional)

try: 
    # watch individual changes to a list of ThirdPartyResource
    api_response = api_instance.watch_third_party_resource_list(pretty=pretty, labelSelector=labelSelector, fieldSelector=fieldSelector, watch=watch, resourceVersion=resourceVersion, timeoutSeconds=timeoutSeconds)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApisextensionsvbetaApi->watch_third_party_resource_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **labelSelector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **fieldSelector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 
 **resourceVersion** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeoutSeconds** | **int**| Timeout for the list/watch call. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

