## Ant Design 新特性提交规范

\[[**English version**](https://github.com/ant-design/ant-design/wiki/PR-principle)]

0. 此规范适用于 [ant-design]( http://github.com/ant-design/ant-design) 和 [ant-design-pro](http://github.com/ant-design/ant-design-pro)。
1. [和现在一样的约定](https://ant.design/docs/react/contributing-cn#%E5%88%86%E6%94%AF%E7%AE%A1%E7%90%86)，所有 `新特性` **必须提交**到 `feature` 分支。
2. `新特性` 指那些新功能增加，UI 的明显变化，交互上的改进，底层重构等变更。
3. `feature` 分支将会锁定，不允许直接提交，**所有变动需要发送 Pull Request**。
4. **按下列 PR 模板提交特性的相关信息**。
5. 保证  CI 和各类校验工具通过。
6. **变动必须附带相应的 changelog，将改动如实反馈给用户**，也方便后续发布的同学查阅。
7. 需要得到**至少另一个维护者**的接受才能合并。
8. 日常 bugfix、文档、站点改进、分支合并等不在此规范约束范围内（但是仍需要通过 PR 形式提交一遍追踪变更）。
9. 此规范用于限制 Ant Design 官方维护者，其他成员提交 PR 时可以自行选择是否使用模板。

### Pull Request 模板

```
### 这个变动的性质是

- [x] 新特性提交
- [ ] 其他改动（日常 bugfix、文档、站点改进、分支合并等，不需要填写余下的模板）

### 需求背景
  
> 1. 描述相关需求的来源。
> 2. 要解决的问题。
> 3. 相关的 issue 讨论链接。
  
### 实现方案和 API
  
> 1. 基本的解决思路和其他可选方案。
> 2. 列出最终的 API 实现和用法。
> 3. 涉及UI/交互变动需要有截图或 GIF。
  
### 对用户的影响和可能的风险

> 1. 这个改动对用户端是否有影响？影响的方面有哪些？
> 2. 预期的 changelog 要怎么写？
> 3. 是否有可能隐含的 break change 和其他风险？

### 请求合并前的自查清单

- [x] 文档已补充或无须补充
- [x] 代码演示已提供或无须提供
- [x] TypeScript 定义已补充或无须补充
- [x] Changelog 已提供或无须提供

### 后续计划

> 如果这个提交后面还有相关的其他提交和跟进信息，可以写在这里。
```

---

范例：https://github.com/ant-design/ant-design/pull/14003