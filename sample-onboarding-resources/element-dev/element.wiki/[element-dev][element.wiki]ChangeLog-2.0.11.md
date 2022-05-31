- 修复 Input 的 `prepend` 或 `append` slot 中 Select 的边框颜色错误，#9089
- 修复 Select 的 `remove-tag` 事件参数与文档不符的问题，#9090
- 新增 SubMenu 的 `show-timeout` 和 `hide-timeout` 属性，#8934（by @HugoLew）
- 修复按需引入 Table 时 `show-overflow-tooltip` 的 Tooltip 样式丢失的问题，#9130
- 修复 Table 在执行 `clearSort` 后点击对应列的排序图标无法正常排序的问题，#9100（by @zEmily）
- 捷克语的 i18n 配置文件由 `cz` 重命名为 `cs-CZ`，#9164

##

- Fixed border color issue of Select when in `prepend` or `append` slot of Input, #9089
- Fixed `remove-tag` event's parameter of Select, #9090
- Added `show-timeout` and `hide-timeout` attributes for SubMenu, #8934 (by @HugoLew)
- Fixed missing Tooltip style of `show-overflow-tooltip` when Table is imported on demand, #9130
- Fixed Table column's sorting malfunctioning after `clearSort` is executed on that column, #9100 (by @zEmily)
- i18n config file for Czech is renamed from `cz` to `cs-CZ`, #9164