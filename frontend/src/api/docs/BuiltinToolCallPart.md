# BuiltinToolCallPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **string** |  | [default to undefined]
**args** | [**Args**](Args.md) |  | [optional] [default to undefined]
**tool_call_id** | **string** |  | [optional] [default to undefined]
**provider_name** | **string** |  | [optional] [default to undefined]
**part_kind** | **string** |  | [optional] [default to PartKindEnum_BuiltinToolCall]

## Example

```typescript
import { BuiltinToolCallPart } from './api';

const instance: BuiltinToolCallPart = {
    tool_name,
    args,
    tool_call_id,
    provider_name,
    part_kind,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
