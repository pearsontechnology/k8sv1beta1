# V1beta1DeploymentRollback

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**ApiVersion** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**Name** | **str** | Required: This must match the Name of a deployment. | 
**UpdatedAnnotations** | **object** | The annotations to be updated to a deployment | [optional] 
**RollbackTo** | [**V1beta1RollbackConfig**](V1beta1RollbackConfig.md) | The config of this deployment rollback. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


