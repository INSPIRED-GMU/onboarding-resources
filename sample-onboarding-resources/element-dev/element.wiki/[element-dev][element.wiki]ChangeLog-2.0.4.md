- 提升 Cascader、Dropdown、Message、Notification、Popover、Tooltip、Tree 的可访问性
- 修复当视口变窄时 Container 无法同步更新其宽度的问题，#8042
- 修复 Tree 的 `updateKeyChildren` 在删除子节点时的行为错误，#8100
- 修复带有边框的 CheckboxButton 在 Form 中高度错误的问题，#8100
- 修复 Menu 在解析自定义颜色时的错误，#8153（by @zhouyixiang）

##

- Improved accessibility for Cascader, Dropdown, Message, Notification, Popover, Tooltip and Tree
- Fixed Container resize when the width of viewport decreases, #8042
- Fixed Tree's `updateKeyChildren` incorrectly deleting child nodes, #8100
- Fixed bordered CheckboxButton's height when nested in a Form, #8100
- Fixed Menu's parsing error for custom colors, #8153 (by @zhouyixiang)