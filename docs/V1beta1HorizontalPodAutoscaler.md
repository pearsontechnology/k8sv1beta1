# V1beta1HorizontalPodAutoscaler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**ApiVersion** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**Metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata | [optional] 
**Spec** | [**V1beta1HorizontalPodAutoscalerSpec**](V1beta1HorizontalPodAutoscalerSpec.md) | behaviour of autoscaler. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status. | [optional] 
**Status** | [**V1beta1HorizontalPodAutoscalerStatus**](V1beta1HorizontalPodAutoscalerStatus.md) | current information about the autoscaler. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


