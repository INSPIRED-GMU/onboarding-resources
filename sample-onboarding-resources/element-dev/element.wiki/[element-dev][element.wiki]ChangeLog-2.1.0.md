### 新特性
- Cascader
  - 新增 `focus` 和 `blur` 事件，#9184（by @viewweiwu）
- Table
  - `filter-method` 方法加入第三个参数 `column`，#9196（by @liyanlong）
- DatePicker
  - 新增 `prefix-icon` 和 `clear-icon` 属性，#9237（by @AdamSGit）
  - 新增 `default-time` 属性，#9094（by @nighca）
  - `value-format` 属性增加对 `timestamp` 的支持，#9319（by @wacky6）
- InputNumber
  - 组件绑定变量的值支持 `undefined`，#9361
- Select
  - 新增 `auto-complete` 属性，#9388
- Form
  - 新增 `disabled` 属性，#9529
  - 新增 `validateOnRuleChange` 属性，#8141
- Notificaition
  - 新增 `closeAll` 方法，#9514

### 修复
- InputNumber
  - 修复初始输入小数点时被重置的问题，#9116
- Dropdown
  - 修复当页面仅有水平滚动条时，某些浏览器下拉菜单定位错误的问题，#9138（by @banzhuanmei）
- Table
  - 修复带有固定列的 Table 在列数据变化后固定列的个数计算错误的问题，#9188（by @kolesoffac）
  - 修复多级表头最后一列的边框不能正确显示的问题，#9326
  - 修复在 Safari 浏览器中表头错位的问题，#9327
  - 修复带有展开行的表格在展开某一行后，当表格数据更新但 `row-key` 值不变时，该行会自动收起的问题，#9462
  - 修复在一些情况下不必要的多次渲染问题，#9426
  - 修复动态改变 TableColumn 的 `width` 属性时，其宽度计算错误的问题，#9426
- Loading
  - 修复某些情况下 Loading 不能被正确隐藏的问题，#9313
- DatePicker
  - 修复 `focus` 方法在范围选择时无效的问题，#9437
  - 修复当目前时刻处于不可选择的范围内时，点击面板上的「此刻」按钮仍能选中目前时刻的问题，#9470（by @wacky6）
  - 修复当在月选择面板中选中天数较少的月份时，日期面板呈现下一个月的问题，#9577（by @wacky6）
- Steps
  - 修复在 IE 11 中的样式问题，#9454

### 非兼容性更新
- Menu
  - `collapse` 状态下的弹出菜单现在会插入至 body 元素，修复其位于 Aside 内时弹出菜单不可见的问题，#9263
- Table
  - 勾选多选表格的 checkbox 时不再同时触发 `row-click` 事件，#9467
- Loading
  - 非全屏 Loading 遮罩层的 `z-index` 修改为 2000；全屏 Loading 遮罩层的 `z-index` 值会随页面上的弹出组件动态更新，#9522
- Dropdown
  - `show-timeout` 和 `hide-timeout` 属性现在仅在 trigger 为 `hover` 时生效，#9573

##

### New features
- Cascader
  - Added `focus` and `blur` events, #9184 (by @viewweiwu)
- Table
  - The `filter-method` now has a third param `column`, #9196 (by @liyanlong)
- DatePicker
  - Added `prefix-icon` and `clear-icon` attributes, #9237 (by @AdamSGit)
  - Added `default-time` attribute, #9094 (by @nighca)
  - `value-format` now supports `timestamp`, #9319 (by @wacky6)
- InputNumber
  - Now the binding value can be `undefined`, #9361
- Select
  - Added `auto-complete` attribute, #9388
- Form
  - Added `disabled` attribute, #9529
  - Added `validateOnRuleChange` attribute, #8141
- Notificaition
  - Added `closeAll` method, #9514

### Bug fixes
- InputNumber
  - Fixed value resetting when typing decimal point, #9116
- Dropdown
  - Fixed dropdown menu incorrect positioning when the page only has a horizontal scrollbar in some browsers, #9138 (by @banzhuanmei)
- Table
  - Fixed an error in calculating number of fixed columns after the column data changes, #9188（by @kolesoffac）
  - Fixed the border of the last column of the grouped header not properly displayed, #9326
  - Fixed incorrect positioning of table header in Safari, #9327
  - Fixed expanded row collapsing when the table data changes, #9462
  - Fixed unnecessary multiple renders in some conditions, #9426
  - Fixed column width calculation error when `width` of TableColumn changes, #9426
- Loading
  - Fixed Loading not hiding correctly in some conditions, #9313
- DatePicker
  - Fixed `focus` method not working in range mode, #9437
  - Fixed clicking the "now" button still selecting the current date even if it is disabled, #9470 (by @wacky6)
  - Fixed date clamping when navigating, #9577 (by @wacky6)
- Steps
  - Fixed style error in IE 11, #9454

### Breaking changes
- Menu
  - The popup menu in `collapse` mode now appends directly to `body`, so that it is visible when nested in Aside, #9263
- Table
  - Now checking the checkboxes in multi-selection Table doesn't trigger `row-click` event, #9467
- Loading
  - The `z-index` of non-fullscreen loading mask is changed to 2000. The `z-index` of fullscreen loading mask will update dynamically with the popup components, #9522
- Dropdown
  - `show-timeout` and `hide-timeout` attributes now only works when trigger is `hover`, #9573