- 修复 Table 在由于筛选而使原有的滚动条消失后表头各列宽度未及时更新的问题，#10834
- 修复可清空的 Input 在初始值为 `null` 时仍然显示清空图标的问题，#10912
- 修复在通过代码改变 ColorPicker 的绑定值后错误地触发 `active-change` 事件的问题，#10903（by @zhangbobell）
- 修复可搜索的 Select 在备选项均被禁用时，通过键盘导航会造成无限循环的问题，#10945

##

- Fixed Table not updating its header widths when the scroll bar disappears due to filtering, #10834
- Fixed clearable Input still showing the clear icon when its initial value is `null`, #10912
- Fixed incorrect trigger of the `active-change` event after changing ColorPicker's binding value programatically, #10903 (by @zhangbobell)
- Fixed filterable Select causing an infinite loop when navigating options using keyboard if all options are disabled, #10945