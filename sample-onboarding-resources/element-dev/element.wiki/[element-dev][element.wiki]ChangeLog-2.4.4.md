- 修复重置表单后触发 Select 组件校验问题，#11837
- 修复 Input 组件 `suffix` 与 `append` 共存时样式错乱问题，#11951
- 修复可清空的只读 Input 仍会显示清空图标的问题，#11967
- 修复 Tree 节点禁用时仍可以选中的问题，#11847
- 修复 Tree `default-checked-keys` 属性不生效的问题，#11971
- 修复 Tree 在过滤节点时下 `empty-text` 不显示的问题，#11971
- 修复 Table 的 `empty-text` 过长时的位置样式问题，#11965
- 修复 Table 的 `current-row-key` 设置为 `null` 时高亮行不清除的问题，#11866
- 修复当 `filters` 为空数组时显示过滤器下拉列表的问题，#11864
- 修复 Radio 的 label 不阻止事件冒泡的问题，#11912

##

- Fixed triggering Select validation after Form resetting, #11837
- Fixed wrong position of Input `suffix` slot when `suffix` slot with `append` slot, #11951
- Fixed clearable Input still displaying the clear icon when readonly, #11967
- Fixed Tree node checked when it's disabled, #11847
- Fixed Tree's `default-checked-keys` not working, #11971
- Fixed `empty-text` not visible when Tree node filtered, #11971
- Fixed the position of oversized `empty-text` in Table, #11965
- Fixed Table row not be unhighlighted when `current-row-key` is assigned to `null`, #11866
- Fixed showing filter dropdown when `filters` is an empty array, #11864
- Fixed Radio's label does not stop event propagation, #11912