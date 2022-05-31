## 新特性
- 综合
  - 新增 TypeScript 类型声明
  - 重绘了全部图标，并新增了部分图标
  - 为部分非兼容性更新增加控制台警告，方便迁移项目。当你在项目中使用了被移除或更名了的属性或事件时，控制台会出现一条警告，例如：
    ```
    [Element Migrating][ElSwitch][Attribute]: on-color is renamed to active-color.
    ```
  - 新增了一系列基于断点的工具类，用于当视口尺寸满足一定条件时隐藏元素
- Layout
  - 新增断点 `xl`，适用于宽度大于 1920px 的视口
- Table
  - 新增 `span-method` 属性，用于合并行或列
  - 新增 `clearSort` 方法，用于清空排序状态
  - 新增 `clearFilter` 方法，用于清空过滤状态
  - 对于可展开行，当该行展开时会获得一个 `.expanded` 类名，方便自定义样式
- DatePicker
  - 新增 `unlink-panels` 属性，用于在选择日期范围时取消两个日期面板之间的联动
- Select
  - 新增 `reserve-keyword` 属性，用于在选择某个选项后保留当前的搜索关键词

## 修复
- Table
  - 修复 TableColumn 的 `header-align` 属性失效的问题
  - 修复 Table 在父元素从 `display: none` 变成其他状态时会隐藏的问题
  - 修复 Table 在父元素为 `display: flex` 时可能出现的宽度逐渐变大的问题
  - 修复 `append` 具名 slot 和固定列并存时，动态获取表格数据会导致固定列消失的问题
  - 修复 `expand-row-keys` 属性初始化无效的问题
  - 修复 `data` 改变时过滤条件失效的问题
  - 修复多级表头时固定列隐藏情况计算错误的问题

## 非兼容性更新
- Switch
  - 由于 `on-*` 属性在 JSX 中会被识别为事件，导致 Switch 所有 `on-*` 属性在 JSX 中无法正常工作，所以 `on-*` 属性更名为 `active-*`，对应地，`off-*` 属性更名为 `inactive-*`。受到影响的属性有：`on-icon-class`、`off-icon-class`、`on-text`、`off-text`、`on-color`、`off-color`、`on-value`、`off-value`
- Table
  - `sort-method` 现在和 `Array.sort` 保持一致的逻辑，要求返回一个数字。

#

## New features
- General
  - Added TypeScript typings
  - All existing icons are redesigned. Some new icons are added.
  - To help you migrate from Element 1.x, we added some console warnings against deprecated APIs. When you use a
 removed or renamed attribute or event in your project, you'll get a warning like this:
    ```
    [Element Migrating][ElSwitch][Attribute]: on-color is renamed to active-color.
    ```
  - Added a series of breakpoint-based utility classes that hide elements when the viewport size meets certain conditions
- Layout
  - Added a new breakpoint `xl` for viewport wider than 1920px
- Table
  - Added `span-method` attribute for merging cells
  - Added `clearSort` method to clear sorting programmatically
  - Added `clearFilter` method to clear filter programmatically
  - For expandable rows, when a row is expanded, a `.expanded` class will be added to its class list, so that you can customize its styles
- DatePicker
  - Added `unlink-panels` attribute to unlink the two date panels when selecting a date range
- Select
  - Added `reserve-keyword` attribute for reserving current search keyword after selecting an option

## Fixes
- Table
  - Now `header-align` of TableColumn works properly
  - Fixed a bug that Table remains hiding when its parent element appears from `display: none`
  - Fixed Table expanding its width when its parent element has `display: flex`
  - Fixed a bug that fixed columns of a Table with `append` slot would disappear when data is dynamically fetched
  - Fixed `expand-row-keys` attribute not working with initial value
  - Fixed filter failing when `data` updates
  - Fixed a calculation error of fixed columns layout with grouped headers

## Breaking changes
- Switch
  - Attributes starting with `on-*` will be parsed to events in JSX, making all `on-*` attributes of Switch not
 able to work in JSX. So `on-*` attributes are renamed to `active-*`, and accordingly `off-*` attributes are renamed to `inactive-*`. This change affects the following attributes: `on-icon-class`, `off-icon-class`, `on-text`, `off-text`, `on-color`, `off-color`, `on-value`, `off-value`
- Table
  - `sort-method` now aligns with `Array.sort`. It should return a number instead of a boolean