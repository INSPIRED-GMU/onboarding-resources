Basically, antd naming requires **FULL NAME** instead of Abbreviation.

## Props
* Initialize prop: `default` + `PropName`
* Force render: `forceRender`
  * Force render sub component: `force` + `Sub Component Name` + `Render`
* Sub render: `Sub Component Name`+ `Render`
* Data Source: `dataSource`
* Panel visible: popup only `visible`, dropdown `open`, additional popup `popupName` + `Visible` like `tooltipVisible`
* `children`:
  * Mainly display content. To avoid additional prop name.
  * Option list like `Select.Option` or `Tree.TreeNode`.
  * Customize wrapped component can consider use `component` prop if `children` may have other usage in future.
* Display related naming: `show` + `PropName`
* Functional: `PropName` + `able`
* Disable: `disabled`
  * sub component: `disabled` + `Sub Component Name`
* mainly icon: `icon`
  * Merge with function first: `functionName: { icon }`. e.g. `expandable: { icon: <Smile /> }`
  * Multiple icons: `FunctionName` + `Icon`
* Trigger: `trigger`
  * Sub function trigger: `Sub Function` + `Trigger`
  * Trigger on the time point: `xxx` + `On` + `EventName` (e.g. `destroyOnClose`)
* Component use other component config. Naming as component.(e.g. `<Table pagination={{...}} />`)

## Event
* Trigger event: `on` + `EventName`
  * Trigger sub component event: `on` + `SubComponentName` + `EventName` (e.g.`onSearchChange`)
  * Trigger prop event: `on` + `PropName` + `EventName` (e.g.`onDragStart`)
* Before trigger event: `before` + `EventName`
* After trigger event: `after` + `EventName`

## Current listing api & Chinese version
ref: [#16048](https://github.com/ant-design/ant-design/issues/16048)

## API standard in the document

### Examples

| Property      | Description                   | Type                           | Default |
| --------- | ---------------------- | ------------------------------ | ------ |
| htmlType | xxx        | string                               | `button `      |
| type          | xxx           | `horizontal ` \| `vertical `  | `horizontal` | 
| disabled  | xxx           | boolean                            | false  |
| minLength      | xxx                         | number                           | 0      |
|  style      | xxx                    | CSSProperties                  | -   |
| character | xxx | (props) => ReactNode | - |
| offset | xxx| \[number, number] | \[0, 0] |
| value     | xxx         | string \| number | `small`      | 

### Promise
- When string type, the **Default** use ` `` `.
- Can also list string optional values ​​in **Type**.
- When boolean type, the **Default** value is true or false.
- When number type, the **Default** value use numbers directly.
- When function type, use an arrow function expression in **Type**.
- No default value use - .
- Capitalize the first letter in **Description** apart from `someProp`.
- No period at the end of the **Description**.
- API order is arranged in alphabetical order, and can be put together under special circumstances (such as: xs sm md).

ref: [#25066](https://github.com/ant-design/ant-design/issues/25066)