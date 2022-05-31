## 新特性
- Form
  - 新增 `clearValidate` 方法，用于清空所有表单项的验证信息，#7623
- MessageBox
  - 新增 `inputType` 属性，用户指定内部输入框的类型，#7651
- Table
  - 新增 `size` 属性，用于控制表格尺寸
  - 新增 `toggleRowExpansion` 方法，用于手动展开或关闭行
  - 新增 `cell-class-name` 属性，用于指定单元格的类名
  - 新增 `cell-style` 属性，用于指定单元格的样式
  - 新增 `header-row-class-name` 属性，用于指定表头行的类名
  - 新增 `header-row-style` 属性，用于指定表头行的样式
  - 新增 `header-cell-class-name` 属性，用于指定表头单元格的类名
  - 新增 `header-cell-style` 属性，用于指定表头单元格的样式
  - TableColumn 的 `prop` 属性支持 `object[key]` 格式
  - TableColumn 新增 `index` 属性，用于自定义索引值

## 修复
- Table
  - 修复 `max-height` 变更后无法恢复的问题
  - 修复一些样式上的计算错误

## 非兼容性更新
- Autocomplete
  - 移除 `props` 属性，现在使用 `value-key` 属性指定输入建议对象中用于显示的键名
- Table
  - 将 `append` slot 移至 `tbody` 元素以外，以保证其只被渲染一次
  - `expand` 事件更名为 `expand-change`，以保证 API 的命名一致性
  - `row-class-name` 和 `row-style` 的函数参数改为对象，以保证 API 的一致性

##

## New features
- Form
  - Added `clearValidate` method for clearing validating results for all form items, #7623
- MessageBox
  - Added `inputType` attribute to assign type for the inner input box, #7651
- Table
  - Added `size` attribute
  - Added `toggleRowExpansion` method to expand or collapse expandable rows programmatically
  - Added `cell-class-name` attribute to assign class name for cells
  - Added `cell-style` attribute to style cells
  - Added `header-row-class-name` attribute to assign class name for header rows
  - Added `header-row-style` attribute to style header rows
  - Added `header-cell-class-name` attribute to assign class name for header cells
  - Added `header-cell-style` attribute to style header cells
  - TableColumn's `prop` attribute now accepts `object[key]` notations
  - Added `index` attribute for TableColumn to customize row indices

## Fixes
- Table
  - Fixed a dynamic `max-height` bug
  - Fixed some style calculation errors

## Breaking changes
- Autocomplete
  - Removed `props` attribute. Now you can use `value-key` attribute to designate key name of the input suggestion
 object for display
- Table
  - `append` slot is moved outside the `tbody` element to avoid multiple rendering
  - `expand` event is renamed to `expand-change`
  - The params of `row-class-name` and `row-style` method is now an object