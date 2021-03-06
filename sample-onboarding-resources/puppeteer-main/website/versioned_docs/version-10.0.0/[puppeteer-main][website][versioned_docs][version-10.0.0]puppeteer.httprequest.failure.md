<!-- Do not edit this file. It is automatically generated by API Documenter. -->

[Home](./index.md) &gt; [puppeteer](./puppeteer.md) &gt; [HTTPRequest](./puppeteer.httprequest.md) &gt; [failure](./puppeteer.httprequest.failure.md)

## HTTPRequest.failure() method

Access information about the request's failure.

<b>Signature:</b>

```typescript
failure(): {
        errorText: string;
    } | null;
```
<b>Returns:</b>

{ errorText: string; } \| null

`null` unless the request failed. If the request fails this can return an object with `errorText` containing a human-readable error message, e.g. `net::ERR_FAILED`. It is not guaranteed that there will be failure text if the request fails.

## Remarks


## Example

Example of logging all failed requests:

```js
page.on('requestfailed', request => {
  console.log(request.url() + ' ' + request.failure().errorText);
});

```

