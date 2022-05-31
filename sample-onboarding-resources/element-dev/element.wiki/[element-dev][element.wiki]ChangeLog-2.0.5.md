- 修复上个版本引入的 Popover、Tree、Breadcrumb、Cascader 的 bug，#8188 #8217 #8283
- 修复 clickoutside 指令的内存泄露问题，#8168 #8225（by @badpunman @STLighter）
- 修复默认尺寸的多选 Select 在清空选项后输入框高度不随之更新的问题，#8317（by @luciy）
- 新增 Select 的 `collapse-tags` 属性，用于在多选时以文字代替 Tag，避免组件高度的增大，#8190
- 修复被隐藏的 Table 会造成 CPU 占用持续增加的问题，#8351
- 开放 Table 的 `doLayout` 方法，用于重新计算 Table 的布局，#8351

##

- Fixed Popover, Tree, Breadcrumb and Cascader regression in 2.0.4, #8188 #8217 #8283
- Fixed memory leak of clickoutside directive, #8168 #8225 (by @badpunman @STLighter)
- Fixed multiple Select height when its value is cleared, #8317 (by @luciy)
- Added `collapse-tags` attribute for multiple Select to replace tags with one line of text, #8190
- Fixed high CPU consumption caused by hidden Table, #8351
- Now you can use `doLayout` method of Table to update its layout, #8351

