# ModelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts** | [**Array&lt;ModelResponsePartsInner&gt;**](ModelResponsePartsInner.md) |  | [default to undefined]
**usage** | [**RequestUsage**](RequestUsage.md) |  | [optional] [default to undefined]
**model_name** | **string** |  | [optional] [default to undefined]
**timestamp** | **string** |  | [optional] [default to undefined]
**kind** | **string** |  | [optional] [default to KindEnum_Response]
**provider_name** | **string** |  | [optional] [default to undefined]
**provider_details** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**provider_response_id** | **string** |  | [optional] [default to undefined]
**finish_reason** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { ModelResponse } from './api';

const instance: ModelResponse = {
    parts,
    usage,
    model_name,
    timestamp,
    kind,
    provider_name,
    provider_details,
    provider_response_id,
    finish_reason,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
