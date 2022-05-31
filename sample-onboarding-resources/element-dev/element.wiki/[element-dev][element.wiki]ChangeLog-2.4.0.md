### 新特性
- 综合
  - 使用原生 webpack 作为构建和打包工具，#11216
  - 可以全局配置弹出层的初始 z-index，#11257
- Autocomplete
  - 新增 `hide-loading` 属性，#11260
- Button
  - 现在圆形按钮也支持通过 `size` 属性改变其尺寸了，#11275
- InputNumber
  - 新增 `precision` 属性，#11281
- Tabs
  - 新增 `before-leave` 钩子，#11259
  - 新增 `lazy` 属性，#11167（by @Kingwl）
- Table
  - 新增 `sort` 方法，支持手动排序，#11311

### 修复
- Input
  - 修复使用中文输入法快速输入文字时会导致视图重新渲染的问题，#11235（by @STLighter）
- Popover
  - 修复当触发元素为 Radio 或 Checkbox 时控制台报错的问题，#11265
- Breadcrumb
  - 修复 `to` 属性不支持动态更新的问题，#11286
- Upload
  - 修复在 `beforeUpload` 方法返回的 Promise 中 resolve 一个 File 时控制台报错的问题，#11297（by @qusiba）
- Tooltip
  - 修复内容为空时箭头错位的问题，#11335
- Autocomplete
  - 修复在快速删除搜索内容后输入建议不正确的问题，#11323
- ColorPicker
  - 修复关闭选色器时触发 `active-change` 事件的问题，#11304
- Table
  - 修复筛选列表过长导致样式超出的问题，#11314
  - 修复排序后导致无法正常显示选中行样式的问题，#11348
- Checkbox
  - 修复单个 Checkbox 不支持表单验证的问题，#11271
- Radio
  - 修复通过空格可以选中被禁用的 Radio 的问题，#11303
- MessageBox
  - 修复连续打开两个 MessageBox 时 `el-popup-parent--hidden` 无法移除的问题，#11371

##

### New features
- General
  - Dev tool and bundler is switched to native webpack, #11216
  - Now you can globally set the initial z-index of popups, #11257
- Autocomplete
  - Added `hide-loading` attribute, #11260
- Button
  - Now you can use the `size` attribute on circle buttons to control their sizes, #11275
- InputNumber
  - Added `precision` attribute, #11281
- Tabs
  - Added `before-leave` attribute, #11259
  - Added `lazy` attribute, #11167（by @Kingwl）
- Table
  - Added `sort` method to manually sort the table, #11311

### Bug fixes
- Input
  - Fixed an issue that causes a re-render when using the Chinese IME to quickly input text, #11235 (by @STLighter)
- Popover
  - Fixed the console error when the triggering element is Radio or Checkbox, #11265
- Breadcrumb
  - Fixed the `to` attribute not supporting dynamic update, #11286
- Upload
  - Fixed the console error when a File is resolved in the returned Promise of the `beforeUpload` method, #11297 (by @qusiba)
- Tooltip
  - Fixed arrow not positioned correctly when content is empty, #11335
- Autocomplete
  - Fixed incorrect input suggestions after deleting keyword quickly, #11323
- ColorPicker
  - Fixed `active-change` event incorrectly triggering when picker dropdown is closed, #11304
- Table
  - Fixed style error of oversized filter panel, #11314
  - Fixed currently selected row not retained when the table is sorted, #11348
- Checkbox
  - Fixed single checkbox not supporting validation, #11271
- Radio
  - Fixed disabled Radio still being selected when pressing space key, #11303
- MessageBox
  - Fixed the `el-popup-parent--hidden` class not removed when opening MessageBox in succession, #11371