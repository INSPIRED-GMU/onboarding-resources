- 修复 DatePicker 的 `type` 为 week 时面板错误高亮的问题，#10712
- 修复 InputNumber 初始值为 0 时输入框为空的问题，#10714
- 新增 Select 的 `automatic-dropdown` 属性，#10042（by @Seebiscuit）
- 修复 `disabled` 的 Rate 仍能通过键盘左右键改变组件值的问题，#10726（by @Richard-Choooou）
- 现在 DatePicker 的 `type` 属性可以接收 `'dates'`，用于选择多个日期，#10650（by @Mini256）
- 新增 Pagination 的 `prev-click` 和 `next-click` 事件，#10755
- 新增 Pagination 的 `pager-count` 属性，#10493（by @chongjohn716）
- 新增 `type` 作为 Tree 的 `allow-drop` 属性回调的第三个参数，#10792
- 改用 ResizeObserver 对元素的尺寸变化进行监测，#10779

##

- Fixed incorrect highlights in DatePicker panel when `type` is week, #10712
- Fixed InputNumber being empty when its initial value is 0, #10714
- Added `automatic-dropdown` attribute for Select, #10042 (by @Seebiscuit)
- Fixed disabled Rate's value still being updated by navigation keys, #10726 (by @Richard-Choooou)
- Now DatePicker's `type` attribute can be `'dates'`, where you can pick multiple dates in one picker, #10650 (by @Mini256)
- Added `prev-click` and `next-click` events for Pagination, #10755
- Added `pager-count` attribute for Pagination, #10493 (by @chongjohn716)
- Added `type` as the 3rd param of Tree's `allow-drop` attribute callback, #10792
- Now we use ResizeObserver to detect DOM element resizing, #10779