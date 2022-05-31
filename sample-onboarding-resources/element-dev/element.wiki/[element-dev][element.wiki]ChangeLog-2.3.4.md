- 删除 SubMenu 在 TypeScript 类型声明中重复的 `showTimeout` 属性，#10566（by @kimond）
- 现在 Transfer 数据项的渲染支持通过 scoped slot 自定义，#10577
- 修复点击 Pagination 禁用的上一页、下一页按钮仍会触发 `current-change` 事件的问题，#10628
- 修复未绑定值的 Textarea 在 SSR 中会显示 `undefined` 的问题，#10630
- 修复 `type` 为 border-car 的 Tabs 中被禁用标签项的样式，#10640
- 新增 `$index` 为 Table 的 `formatter` 属性回调的第四个参数，#10645
- 修复 TypeScript 类型声明未导出 CheckboxButton 的问题，#10666

##

- Deleted duplicate `showTimeout` attribute in SubMenu's TypeScript declaration, #10566 (by @kimond)
- Now you can customize Transfer's data item using scoped slot, #10577
- Fixed clicking disabled prev and next button of Pagination still triggers `current-change` event, #10628
- Fixed Textarea displaying `undefined` in SSR when its value is not set, #10630
- Fixed disabled TabItem style when `type` is border-car, #10640
- Added `$index` as `formatter`'s fourth param of Table, #10645
- Fixed CheckboxButton not exported in TypeScript declaration, #10666