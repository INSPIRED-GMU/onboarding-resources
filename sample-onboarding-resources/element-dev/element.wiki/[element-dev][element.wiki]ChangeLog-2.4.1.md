- 移除 Autocomplete 的重复类型声明，#11388
- 修复嵌套在 Form 内的 Select 在 FireFox 浏览器中下拉箭头错位的问题，#11427
- 修复 Select 的初始值为 `null` 时仍然显示清除图标的问题，#11460
- 修复禁用的 Radio 在点击时显示 box-shadow 的问题，#11462
- 新增 MessageBox 的 `iconClass` 属性，#11499
- 新增 Tabs 的 `stretch` 属性，#11476
- 修复 Tabs 开启 `lazy` 时渲染顺序异常的问题，#11461
- 修复 Table 展开行时无法保留选中行样式的问题，#11464
- 修复 Tabs 调用 `before-leave` 并返回 Promise 的时候，Tabs 会存在 focus 状态的问题，#11386
- 修复 Popover 禁用状态下创建弹出框的问题，#11426
- 修复 Tree 在懒加载状态下添加新节点造成无限循环的问题，#11430 （by @wangjingf）
- 新增 Dialog 的 `closed` 事件，#11490

##

- Removed Autocomplete's duplicate type declaration, #11388
- Fixed Select's dropdown arrow style in FireFox when nested in Form, #11427
- Fixed clear icon of Select still showing when the initial value is `null`, #11460
- Fixed disabled radio showing box-shadow when clicked, #11462
- Added `iconClass` attribute for MessageBox, #11499
- Added `stretch` attribute for Tabs, #11476
- Fixed rendering order issue of TabPane when Tabs is `lazy`, #11461
- Fixed Table not retaining current highlight row when expanded, #11464
- Fixed focusing state when `before-leave` returns a resolved promise, #11386
- Fixed disabled Popover still creating poppers, #11426
- Fixed Tree's endless loop when a new node is added in lazy mode, #11430 (by @wangjingf)
- Added `closed` event for Dialog, #11490
