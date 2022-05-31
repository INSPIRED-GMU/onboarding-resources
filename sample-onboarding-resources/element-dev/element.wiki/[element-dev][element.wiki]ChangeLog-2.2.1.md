- 修复 Aside、Header 和 Footer 在某些布局中被压缩的问题，#9812
- 修复设置了 `height` 属性的 Table 在服务端渲染时无法加载的问题，#9876
- 修复可展开的 Table 在展开某一行后高度未重新计算的问题，#9848
- 修复在 DateTimePicker 中手动输入日期后不能正确触发 `change` 事件的问题，#9913
- 修复鼠标右键点击 Select 的输入框会展开选项的问题，#9894（by @openks）
- 新增 Slider 的 `tooltip-class` 属性，#9957
- 现在的 Select 在选中选项后仍然处于 focus 状态，#9857（by @Seebiscuit）
- 新增 Transfer 的 `target-order` 属性，#9960

##

- Fixed Aside, Header and Footer shrinking in some layout, #9812
- Fixed Table with a `height` attribute not rendering in SSR, #9876
- Fixed expandable Table not calculating its height when a row is expanded, #9848
- Fixed `change` event not trigger when manually typing date in DateTimePicker, #9913
- Fixed Select showing its options when the input box is right-clicked, #9894 (by @openks)
- Added `tooltip-class` attribute for Slider, #9957
- Now Select will stay focused after selection, #9857 (by @Seebiscuit)
- Added `target-order` attribute for Transfer, #9960