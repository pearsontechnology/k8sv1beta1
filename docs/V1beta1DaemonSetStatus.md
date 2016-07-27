# V1beta1DaemonSetStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CurrentNumberScheduled** | **int** | CurrentNumberScheduled is the number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 
**NumberMisscheduled** | **int** | NumberMisscheduled is the number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 
**DesiredNumberScheduled** | **int** | DesiredNumberScheduled is the total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: http://releases.k8s.io/HEAD/docs/admin/daemons.md | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


