- 新增 Upload 的 `before-remove` 钩子方法，#8788（by @firesh）
- 修复 FormItem 的 `error` 属性初始值无效的问题，#8840
- 通过指令调用的 Loading 现在支持以 `element-loading-custom-class` 属性的方式设置自定义类名，#8826（by @earlymeme）
- 修复 CarouselItem 为异步获取时被隐藏的问题，#8921
- 新增 Tree 的 `renderAfterExpand` 属性，#8972

##

- Added `before-remove` hook function for Upload, #8788 (by @firesh)
- Fixed initial value of `error` not working for FormItem, #8840
- Now Loading directive supports custom class name by assigning `element-loading-custom-class` attribute, #8826 (by @earlymeme)
- Fixed CarouselItem becoming invisible when data is asynchronously updated, #8921
- Added `renderAfterExpand` attribute for Tree, #8972