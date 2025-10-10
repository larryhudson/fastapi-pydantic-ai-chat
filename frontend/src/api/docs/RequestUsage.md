# RequestUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **number** |  | [optional] [default to 0]
**cache_write_tokens** | **number** |  | [optional] [default to 0]
**cache_read_tokens** | **number** |  | [optional] [default to 0]
**output_tokens** | **number** |  | [optional] [default to 0]
**input_audio_tokens** | **number** |  | [optional] [default to 0]
**cache_audio_read_tokens** | **number** |  | [optional] [default to 0]
**output_audio_tokens** | **number** |  | [optional] [default to 0]
**details** | **{ [key: string]: number; }** |  | [optional] [default to undefined]

## Example

```typescript
import { RequestUsage } from './api';

const instance: RequestUsage = {
    input_tokens,
    cache_write_tokens,
    cache_read_tokens,
    output_tokens,
    input_audio_tokens,
    cache_audio_read_tokens,
    output_audio_tokens,
    details,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
