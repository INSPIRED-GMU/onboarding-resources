- 新增 Input 的 `clear` 事件，#9988（by @blackmiaool）
- 现在 ColorPicker 的手动输入支持 `hsl`、`hsv` 和 `rgb` 格式了，#9991
- 修复 DatePicker 在清除初始值时不触发 `change` 事件的问题，#9986
- 现在 Rate 的图标类相关属性支持动态更新了，#10003
- 修复含有固定列的 Table 在设置 `max-height` 属性后有时不能及时更新布局高度的问题，#10034
- 现在 DatePicker 的范围选择支持先点选结束日期，再点选开始日期了，#8156（by @earlymeme）
- 新增 Pagination 的 `disabled` 属性，#10006
- 新增 Popover 的 `after-enter` 和 `after-leave` 事件，#10047
- 修复重置表单后，用户第一次改变 Select 的值时不触发校验的问题，#10105
- 修复 Table 的固定列在某些情况下宽度不正确的问题，#10130
- 修复调用 MessageBox 未传入 `title` 时，打开的 MessageBox 会继承上一个实例的 `title` 属性的问题，#10126（by @Pochodaydayup）
- 新增 Slider 的 `input-size` 属性，#10154
- 新增 Transfer 的 `left-check-change` 和 `right-check-change` 事件，#10156

##

- Added `clear` event for Input, #9988 (by @blackmiaool)
- Now manual input of ColorPicker supports `hsl`, `hsv` and `rgb` modes, #9991
- Fixed DatePicker not triggering `change` event when its initial value is cleared, #9986
- Now icon class related attributes of Rate support dynamic updates, #10003
- Fixed Table with fixed columns not updating its height correctly if `max-height` is set, #10034
- Now DatePicker's range mode supports reverse selection (clicking the end date, then clicking the start date), #8156 (by @earlymeme)
- Added `disabled` attribute for Pagination, #10006
- Added `after-enter` and ` after-leave` events for Popover, #10047
- Fixed Select not triggering validation when user selects an option after executing `resetFields` of Form, #10105
- Fixed incorrect widths of fixed columns of Table in some cases, #10130
- Fixed MessageBox inheriting the `title` attribute of its previous instance when called without `title`, #10126 (by @Pochodaydayup)
- Added `input-size` attribute for Slider, #10154
- Added `left-check-change` and `right-check-change` events for Transfer, #10156