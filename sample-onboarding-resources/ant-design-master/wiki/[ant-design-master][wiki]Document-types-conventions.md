Follows TypeScript's type style.

## Lowercase type names：

* `boolean` for boolean values;
* `string` for string values;
* `string[]` or `Array<string>` for array values;
* `number` for number values;
* `any` for any value;
* `object` for plain objects;

## Function

```
(selectedRowKeys: string[], selectedRows: <T>[]) => any
```

## Array

```
string[]

// element has multiple types
Array<string|number>
```

## Enum

```
'primary'|'ghost'|'dashed'
```

## Using `|` for multiple types：

Markdown requires `\` to escape `|` in table.

```
boolean\|number
```

## If a prop accepts any kind of React node：

```
string|ReactNode
```

## If a prop only accepts string or a single React element:

```
string|ReactElement
```

## If a prop only accepts specific element：

```
Menu.Item

// for array
Menu.Item[]
```

## If a prop only accepts specific element with specific props:

```
ReactElement<InputProps>
```

## Link to a inner type

1. Get type's permanent link: https://github.com/ant-design/ant-design/blob/1bf0bab2a7bc0a774119f501806e3e0e3a6ba283/components/cascader/index.tsx#L9
1. Use https://git.io shorten url

```
[CascaderOptionType](https://git.io/vMMoK)[] 
```
