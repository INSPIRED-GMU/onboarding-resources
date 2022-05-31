- 修复 Table 的 `class-name` 和 `label-class-name` 属性不支持动态更新的问题，#11626
- 修复 Table 在 `highlight-current-row` 为 `false` 时点击行也会触发高亮的问题，#11691 #11563
- 修复 ButtonGroup 中只有一个 `round` 或 `circle` 的 Button 时的样式错误，#11605
- 修复在某些情况下 Pagination 的条目数选择器的样式错误，#11622
- 修复 Menu 的 `collapse` 属性变化后无法使用 `open` 方法的问题，#11646
- Tabs 的 `before-leave` 钩子添加了 `activeName` 和 `oldActiveName` 参数，#11713
- 修复 Cascader 关闭后的聚焦问题，#11588
- 修复 Cascader 在 `change-on-select` 状态下点击选项不关闭的问题，#11623
- 现在通过代码改变 Select 的值后会触发表单校验，与 Input 行为一致，#11672

##

- Now `class-name` and `label-class-name` of Table are reactive, #11626
- Fixed Table still highlighting clicked row when `highlight-current-row` is `false`, #11646
- Fixed a style bug of ButtonGroup when it has only one `round` or `circle` Button, #11605
- Fixed style of page size Select of Pagination, #11622
- Fixed Menu's `open` method error when `collapse` is dynamically changed, #11646
- Added `activeName` and `oldActiveName` parameters to the `before-leave` hook of Tabs, #11713
- Fixed Cascader focused after outside clicked, #11588
- Fixed Cascader not closing when option is clicked when `change-on-select` is `true`, #11623
- Now updating Select's value programmatically will trigger form validation, #11672
