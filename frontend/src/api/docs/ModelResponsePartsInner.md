# ModelResponsePartsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**BinaryContent**](BinaryContent.md) |  | [default to undefined]
**id** | **string** |  | [optional] [default to undefined]
**part_kind** | **string** |  | [optional] [default to PartKindEnum_File]
**tool_name** | **string** |  | [default to undefined]
**args** | [**Args**](Args.md) |  | [optional] [default to undefined]
**tool_call_id** | **string** |  | [optional] [default to undefined]
**provider_name** | **string** |  | [optional] [default to undefined]
**metadata** | **any** |  | [optional] [default to undefined]
**timestamp** | **string** |  | [optional] [default to undefined]
**signature** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { ModelResponsePartsInner } from './api';

const instance: ModelResponsePartsInner = {
    content,
    id,
    part_kind,
    tool_name,
    args,
    tool_call_id,
    provider_name,
    metadata,
    timestamp,
    signature,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
