- 修复了 Table 在固定列和合计行并存时的高度计算错误的问题，#9026
- 修复了 Table 样式 SCSS 文件错误编译的问题，#9028
- 现在 DatePicker 的 `change` 事件只会在 `value` 真正改变的时候触发，#9029（by @remizovvv）
- 新增 Input 的 `tabindex` 属性，#9041（by @dicklwm）

##

- Fixed wrong max height calculation of Table when fixed column and summary row co-exist, #9026
- Fixed uncompiled color style of empty text in Table, #9028
- Now DatePicker only emits `change` event when value is truly changed, #9029 (by @remizovvv)
- Added `tabindex` attribute for Input, #9041 (by @dicklwm)