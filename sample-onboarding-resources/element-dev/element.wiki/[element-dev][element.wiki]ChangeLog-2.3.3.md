- 新增 Card 的 `shadow` 属性，#10418（by @YunYouJun）
- 修复 Badge 在 `value` 属性为 `0` 时不显示上标的问题，#10470
- 修复 Tree 节点拖拽相关的问题，#10474 #10494
- 新增 Autocomplete 的 `placement` 属性，#10475
- 现在 `default-time` 属性也可用于非范围选择的 DateTimePicker 了，#10321（by @RickMacTurk）
- 修复 TabItem 在浏览器失焦和隐藏后出现蓝色边框的问题，#10503
- 新增 SubMenu 的 `popper-append-to-body` 属性，#10515
- 现在非链接的 BreadcrumbItem 在 hover 时不再具有视觉反馈，#10551
- 调整 InputNumber `change` 事件的触发时机，使得在回调中能够取得最新的组件绑定值，#10553

##

- Added `shadow` attribute for Card, #10418 (by @YunYouJun)
- Fixed Badge being hidden when `value` is `0`, #10470
- Fixed some bugs of draggable Tree, #10474 #10494
- Added `placement` for Autocomplete, #10475
- Now `default-time` attribute also works in non-range DateTimePicker, #10321 (by @RickMacTurk)
- Removed the blue outline of TabItem after the browser blurs or is minimized, #10503
- Added `popper-append-to-body` attribute for SubMenu, #10515
- Removed visual feedback when hovering on non-link BreadcrumbItem, #10551
- Fixed InputNumber's `change` event to ensure the component's binding value is updated in the event handler, #10553
