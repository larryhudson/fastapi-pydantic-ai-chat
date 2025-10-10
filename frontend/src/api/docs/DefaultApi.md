# DefaultApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**chatChatPost**](#chatchatpost) | **POST** /chat | Chat|

# **chatChatPost**
> any chatChatPost(chatRequest)

Simple streaming chat endpoint.

### Example

```typescript
import {
    DefaultApi,
    Configuration,
    ChatRequest
} from './api';

const configuration = new Configuration();
const apiInstance = new DefaultApi(configuration);

let chatRequest: ChatRequest; //

const { status, data } = await apiInstance.chatChatPost(
    chatRequest
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **chatRequest** | **ChatRequest**|  | |


### Return type

**any**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful Response |  -  |
|**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

