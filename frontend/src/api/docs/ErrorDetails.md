# ErrorDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **string** |  | [default to undefined]
**loc** | [**Array&lt;ErrorDetailsLocInner&gt;**](ErrorDetailsLocInner.md) |  | [default to undefined]
**msg** | **string** |  | [default to undefined]
**input** | **any** |  | [default to undefined]
**ctx** | **{ [key: string]: any; }** |  | [optional] [default to undefined]
**url** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { ErrorDetails } from './api';

const instance: ErrorDetails = {
    type,
    loc,
    msg,
    input,
    ctx,
    url,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
