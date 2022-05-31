- 修复 Tree 的 `allow-drop` 回调在使用 `type` 参数后的错误行为，#10821
- 修复可搜索的单选 Select 在 IE11 中无法输入搜索关键词的问题，#10822
- 修复单选 Select 在使用鼠标选中某个选项后错误地触发 `blur` 事件的问题，#10822
##

- Fixed wrong behavior of Tree's `allow-drop` callback when `type` parameter is used, #10821
- Now you can properly enter keywords in filterable single Select in IE11, #10822
- Fixed single Select incorrectly triggering `blur` event after clicking an option, #10822