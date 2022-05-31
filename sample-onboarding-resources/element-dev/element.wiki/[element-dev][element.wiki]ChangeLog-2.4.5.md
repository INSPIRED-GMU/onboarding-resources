- 修复 Table 设置 `class-name` 对 `expand` 列不生效的问题，#12006
- 新增 Table 的 `toggleAllSelection` 方法，#12047
- 修复 Input 包含 Select 时，suffix 插槽位置显示不正确的问题，#12108
- 修复 Option 的 `line-height` 无法设置的问题，#12120
- 修复初始值为 `null` 的 TimeSelect 在执行 `resetField` 后无法再赋值的问题，#12010
- 修复 Tree 组件中不响应方向键以外 keydown 事件的问题，#12008
- 修复 Tree 在懒加载情况下选中父节点的问题，#12106
- Tree 的 `getCheckedNodes` 方法新增 `includeHalfChecked` 参数，#12014

##

- Fixed Table setting `class-name` does not work for `expand` column, #12006
- Added `toggleAllSelection` method for Table, #12047
- Fixed wrong position of suffix slot when Input contains Select, #12108 
- Fixed `line-height` of Option unable to set, #12120
- Fixed TimeSelect with default value of `null` could not be assigned after executing `resetField`, #12010
- Fixed keydown event which is not arrow key does not work in Tree, #12008
- Fixed parent node checked in lazy mode, #12106
- Added `includeHalfChecked` parameter for getCheckedNodes of Tree, #12014

