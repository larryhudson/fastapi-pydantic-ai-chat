# ModelRequestPartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**Content**](Content.md) |  | [default to undefined]
**timestamp** | **string** |  | [optional] [default to undefined]
**dynamic_ref** | **string** |  | [optional] [default to undefined]
**part_kind** | **string** |  | [optional] [default to PartKindEnum_RetryPrompt]
**tool_name** | **string** |  | [default to undefined]
**tool_call_id** | **string** |  | [optional] [default to undefined]
**metadata** | **any** |  | [optional] [default to undefined]

## Example

```typescript
import { ModelRequestPartsInner } from './api';

const instance: ModelRequestPartsInner = {
    content,
    timestamp,
    dynamic_ref,
    part_kind,
    tool_name,
    tool_call_id,
    metadata,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
