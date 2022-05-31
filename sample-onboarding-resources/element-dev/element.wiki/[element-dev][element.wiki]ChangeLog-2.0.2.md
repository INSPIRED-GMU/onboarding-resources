- 在 InputNumber 的加减按钮上单击鼠标右键不再触发值的改变，#7817
- Form 的 `validate` 方法现在能够正确地在异步校验完成后执行回调了，#7774（by @Allenice）
- 修复 DatePicker 的范围选择在内核为 Chromium 53-57 的浏览器中无法使用的问题，#7838
- 修复 `list-type` 为 picture-card 的 Upload 预览和删除图标丢失的问题，#7857
- 新增 TableColumn 的 `sort-by` 属性，#7828（by @wangfengming）
- 修复周模式下的 DatePicker 在选择某年第一周可能会显示为前一年第一周的问题，#7860（by @hh23485）
- 修复垂直模式的 Steps 中图标宽度的样式错误，#7891
- 增大了 Tree 中展开箭头的点击热区，#7891

##

- Now right-clicking the buttons of InputNumber won't change its value, #7817
- `validate` method of Form can now wait for asynchronous validations before executing its callback, #7774 (by @Allenice)
- Fixed range selection of DatePicker not working in Chromium 53-57 browsers, #7838
- Fixed missing preview and delete icons of Upload when its `list-type` is picture-card, #7857
- Added `sort-by` attribute for TableColumn, #7828 (by @wangfengming)
- Fixed DatePicker sometimes displaying wrong year number when selecting the first week in week mode, #7860 (by @hh23485)
- Fixed icon style error of vertical Steps, #7891
- The hot area for node arrows in Tree is expanded, #7891