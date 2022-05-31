- 修复 `type` 为 dates 的 DatePicker 在选择非当前月的日期后，面板会跳转至当前月的问题，#10973
- 修复可清空的只读 Input 仍会显示清空图标的问题，#10912
- 修复范围选择的 DatePicker 在未改变值的情况下关闭下拉面板仍会触发 `change` 事件的问题，#11017
- 修复 Select 在有分组选项时不能正确通过键盘导航的问题，#11058
- 新增 Select 的 `prefix` 具名 slot，#11063
- 新增 FormItem 的 `clearValidate` 方法，#11076
- 新增 Tree 的 `checkOnClickNode` 属性，#11111

##

- Fixed DatePicker panel jumping to the current month after picking a date in a non-current month when `type` is dates, #10973
- Fixed clearable Input still displaying the clear icon when readonly, #10912
- Fixed closing the DatePicker panel without changing the value incorrectly triggering the `change` event, #11017
- Fixed keyboard navigation not working properly when Select has grouped options, #11058
- Added `prefix` named slot for Select, #11063
- Added 'clearValidate` method for FormItem, #11076
- Added `checkOnClickNode` attribute for Tree, #11111