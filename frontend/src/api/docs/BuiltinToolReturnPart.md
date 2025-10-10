# BuiltinToolReturnPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **string** |  | [default to undefined]
**content** | **any** |  | [default to undefined]
**tool_call_id** | **string** |  | [optional] [default to undefined]
**metadata** | **any** |  | [optional] [default to undefined]
**timestamp** | **string** |  | [optional] [default to undefined]
**provider_name** | **string** |  | [optional] [default to undefined]
**part_kind** | **string** |  | [optional] [default to PartKindEnum_BuiltinToolReturn]

## Example

```typescript
import { BuiltinToolReturnPart } from './api';

const instance: BuiltinToolReturnPart = {
    tool_name,
    content,
    tool_call_id,
    metadata,
    timestamp,
    provider_name,
    part_kind,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
