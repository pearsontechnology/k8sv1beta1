# V1beta1DeploymentSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Replicas** | **int** | Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1. | [optional] 
**Selector** | [**V1beta1LabelSelector**](V1beta1LabelSelector.md) | Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. | [optional] 
**Template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template describes the pods that will be created. | 
**Strategy** | [**V1beta1DeploymentStrategy**](V1beta1DeploymentStrategy.md) | The deployment strategy to use to replace existing pods with new ones. | [optional] 
**MinReadySeconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] 
**RevisionHistoryLimit** | **int** | The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. | [optional] 
**Paused** | **bool** | Indicates that the deployment is paused and will not be processed by the deployment controller. | [optional] 
**RollbackTo** | [**V1beta1RollbackConfig**](V1beta1RollbackConfig.md) | The config this deployment is rolling back to. Will be cleared after rollback is done. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


