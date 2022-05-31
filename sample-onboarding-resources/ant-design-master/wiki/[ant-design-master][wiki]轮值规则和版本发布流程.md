## 轮值规则

1. 如无特殊需求，**每周**发布一个 `patch` 版本，也可按照具体改动判断是否发布 `minor` 版本。通常 `minor` 版本在月末发布。`major` 版本发布不遵循此规则。
1. 从 2016 年 5 月 14 日起，**发布进行按周轮值**。
1. 轮值人当周负责
   - **及时进行 PR Reveiew 的分配和合并操作**。（不要合并 `In Progress` `WIP` 的 PR）
   - 定位、分配、跟踪需要解决的 Issue。
   - 关闭已解决或无法解决的 Issue。
   - 按时进行新版本发布。
1. 标签的使用
   - `help wanted`：同意用户的需求，机器人会自动回复，鼓励社区直接来提交代码。
   - `🤔 Need Reproduce`：用于没有提供重现的 issue，机器人会自动回复，如果之后 3 天未更新，机器人会自动关闭 issue。
   - `needs-more-info`：当用户展示信息不全时，可标记。如果 3 天未更新，机器会自动回复并关闭 issue。
   - `Usage` `Question`：用于 `如何使用` 相关的提问，机器人会自动回复并关闭问题。
   - `🐛 Bug`：用于已经重现了这个问题，标记这是一个 bug。
   - `someone working on it`：用于标记自己正在处理这个问题，避免其他同学撞车。
   - `3.x`：由于 3.x 分支已不再维护。用于标记属于 3.x 版本的 issue，机器人会回复并关闭。
   - `Invalid`：新开 issue 会校验是否从 issue-helper 创建而来。当用户删除原有内容，而填写无用信息时，可标记 `Invalid`。机器人会自动回复并关闭。
   - `🎱 Collaborate PR only`：当 issue 设计内容需要和设计师或不接受外部 PR 时，可添加。
   - `BranchAutoMerge`：用于 master 和 feature 分支互相合并使用，其他情况切勿使用。

## 自动合并的分支的命名规则

- master
- feature
- feature-merge-master
- master-merge-feature

## 发布流程

### 1. 发布前相关工作。

   - 确认各项 CI 和检查是绿的。
   - 关闭已修复/简单明确的 issue，合并已通过的 PR。
   - **如果是发布 minor 版本**，依赖的 rc 组件版本在向下兼容的前提下升级到最新（参看 [david 版本过期服务](https://david-dm.org/ant-design/ant-design)），升级后对演示进行基本的人工检查。

### 2. 编辑更新日志以及升级版本号

  - **如果是发布 minor 版本**，先新建一个 pr 将 feature 分支合并到 master，所有发布操作需要在 master 分支上进行。**注意！不要使用 squash merge！防止提交信息丢失！请添加 `BranchAutoMerge` label，CI 通过后会自动合并**
  - 从 master 新建一个 release 分支用来做发布的修改（例如：`git checkout -b release-3.6.0`）。
  - 在 ` CHANGELOG.en-US.md` 和 ` CHANGELOG.zh-CN.md` 和 里添加发布日志，可以用 [compare](https://github.com/ant-design/ant-design/compare/1.0.1...master) 功能找到当前和之前版本的区别，将有价值的改动如实反馈给用户。
  - 对用户使用上无感知的改动建议（文档修补、微小的样式优化、代码风格重构等等）不要提及，保持 CHANGELOG 的内容有效性。
  - 用面向开发者的角度和叙述方式撰写 CHANGELOG，**不描述修复细节，描述问题和对开发者的影响；描述用户第一现场的问题，而非你的解决方式**。
    - 例子一
      - ❌ 修复组件 Typography 的 dom 结构问题。
      - ✅ 重构并简化了 List Item 的 dom 结构，并且修复了 Item 中内容空格丢失的问题。
    - 例子二
      - ❌ 修复 `lib` 下样式文件路径问题。
      - ✅ 修复部分组件样式丢失的问题。
  - 新增属性时，建议用易于理解的语言描述用户可以感知的变化。（例如，新增 `onCellClick` 属性，可以定义单元格点击事件）
  - 尽量给出原始的 PR 链接，社区提交的 PR 改动加上提交者的链接。
  - 底层模块升级中间版本要去 rc-component 里找到改动，给出变动说明。
  - 如果不确定改动的真实目的，可以向提交者进行咨询。
  - 参考之前版本的日志写法，添加必要的截图帮助说清楚新功能。
  - 每一个改动前加一个 emoji 增加文档的可读性和生动性，可选的 emoji [参考这里](#emoji-for-changelog)。
  - 将一个组件的多个改动放入一个 LOG，作为一个子 List。
  - 将同类型的改动放在一起，尽量不要穿插。
  - changlog 的 PR 里需将 `package.json` 的版本号一起改掉。
  - push release 分支并发起 CHANGELOG 的 PR 请其他同学 review。
  - **PR 的主楼内容里直接复制上 CHANGELOG 的改动内容**，好处是版本 CHANGELOG 的 PR 会关联在各个 issue 中，很容易知道 issue 在哪个版本被改了。https://github.com/ant-design/ant-design/pull/15018
  - 在改动被人审过后，轮值同学可以合并代码。
  - CHANGELOG 合并时使用 squash merge。

changelog PR 可以参考 https://github.com/ant-design/ant-design/pull/12615 。

> 注：底层 rc 组件的小版本修复，可以不用写入 changelog。

#### 2.1 Changelog 编辑器

运行 `npm run changelog` 自动拉取变更信息：

<img width="616" alt="截屏2020-04-13 下午9 40 04" src="https://user-images.githubusercontent.com/5378891/79124644-58d0c280-7dcf-11ea-9b70-6fa97217532c.png">

拉取完毕后会启动可视化编辑器用于编辑 changelog：

<img width="1440" alt="截屏2020-04-13 下午9 40 53" src="https://user-images.githubusercontent.com/507615/89774981-7291d480-db39-11ea-9e7e-8947704f54c0.png">

### 3. npm 发布

更新日志的修改合并后，删除 release-x.x.x 分支。接下来可以正式发布 `antd`。

- 执行 `rm -rf node_modules && npm i`，如果有.lock 文件，最好删除后进行安装，确保 node_modules 目录是最新的。
- 按照[语义化版本](https://semver.org/lang/zh-CN/)修改 `package.json` 版本号，`bugfix` 升级小版本，新功能添加升级中间的版本号。
- 在项目根目录下执行：

```bash
npm run pub
```

检查 [releases](https://github.com/ant-design/ant-design/releases) 和 [unpkg](https://unpkg.com/antd/) 是否发布成功。

- 涉及 Action：release-helper.yml

`npm run pub` 会调用 `antd-tools` 工具运行 pub 生成一个新版本 tag，同时会发布 npm，新 tag 的推送会触发该 Action。机器人自动发布新版本 Release，同时进行进行钉钉通知。

#### Conch Tag

在发布完成后，post script 会自动执行并且提示 conch tag 更新（默认为当前版本往前 15 天的正式版本，没有特殊需求直接确认即可）：

<img width="492" src="https://user-images.githubusercontent.com/5378891/150078517-e0dd8bb4-4259-4d0a-93ab-21a1ec2df34d.png">

### 4. 发布网站

CI 会自动发布官网，出了问题再手动发布。

```bash
npm run deploy
```

依次执行完上面的两条命令后，访问 https://ant.design 和国内站点 https://ant-design.gitee.io 确认网站发布成功。

- 涉及 Action：site-deploy.yml

新 tag 触发该 Action 部署 gh-pages。

### 6. 更新 feature 分支

发版确认一切正常后，应及时合并 `master` 进当前的 `feature` 分支。

## Emoji for changelog

- 🐞 Bug 修复
- 💄 样式更新/less 变量更新
- 🆕 新增特性
- 🔥 极其值得关注的新增特性
- 🇺🇸🇨🇳🇬🇧 国际化改动，注意这里直接用对应国家/地区的旗帜。
- 📖 :memo: 文档或网站改进
- ✅ 新增或更新测试用例
- 🛎 更新警告/提示信息
- ⌨️ :wheelchair: 可访问性增强
- 🗑 废弃或移除
- 🛠 重构或工具链优化
- ⚡️ 性能提升