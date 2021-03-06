<!-- Do not edit this file. It is automatically generated by API Documenter. -->

[Home](./index.md) &gt; [puppeteer](./puppeteer.md) &gt; [Frame](./puppeteer.frame.md) &gt; [$](./puppeteer.frame._.md)

## Frame.$() method

This method queries the frame for the given selector.

<b>Signature:</b>

```typescript
$<T extends Element = Element>(selector: string): Promise<ElementHandle<T> | null>;
```

## Parameters

|  Parameter | Type | Description |
|  --- | --- | --- |
|  selector | string | a selector to query for. |

<b>Returns:</b>

Promise&lt;[ElementHandle](./puppeteer.elementhandle.md)&lt;T&gt; \| null&gt;

A promise which resolves to an `ElementHandle` pointing at the element, or `null` if it was not found.

