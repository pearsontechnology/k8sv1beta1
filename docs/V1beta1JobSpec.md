# V1beta1JobSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Parallelism** | **int** | Parallelism specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: http://releases.k8s.io/HEAD/docs/user-guide/jobs.md | [optional] 
**Completions** | **int** | Completions specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: http://releases.k8s.io/HEAD/docs/user-guide/jobs.md | [optional] 
**ActiveDeadlineSeconds** | **int** | Optional duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer | [optional] 
**Selector** | [**V1beta1LabelSelector**](V1beta1LabelSelector.md) | Selector is a label query over pods that should match the pod count. Normally, the system sets this field for you. More info: http://releases.k8s.io/HEAD/docs/user-guide/labels.md#label-selectors | [optional] 
**AutoSelector** | **bool** | AutoSelector controls generation of pod labels and pod selectors. It was not present in the original extensions/v1beta1 Job definition, but exists to allow conversion from batch/v1 Jobs, where it corresponds to, but has the opposite meaning as, ManualSelector. More info: http://releases.k8s.io/HEAD/docs/design/selector-generation.md | [optional] 
**Template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template is the object that describes the pod that will be created when executing a job. More info: http://releases.k8s.io/HEAD/docs/user-guide/jobs.md | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


