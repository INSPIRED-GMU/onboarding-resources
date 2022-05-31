## 老版本

- http://09x.ant.design
- http://010x.ant.design

原则上，大中版本的改动才需要发布旧版文档。

1. 在 ant-design 下建立项目库，项目名为 `{version}.ant.design`。

  比如：http://github.com/ant-design/010x.ant.design

  克隆到本地并建立 gh-pages 分支。

2. 在 [ant-design](http://github.com/ant-design/ant-design) 目录下切换到对应版本上，运行：

  ```bash
  npm run site
  ```

  拷贝构建出的 _site 目录里的文件到 `{version}.ant.design` 目录下。

3. 在 `{version}.ant.design` 目录下建立 `CNAME` 文件。内容和域名一致。

  例如：https://github.com/ant-design/010x.ant.design/blob/gh-pages/CNAME

5. 提交到 http://github.com/ant-design/010x.ant.design 的 `gh-pages` 分支上。

6. 到 godday 上建一个 CNAME 记录，将 `{version}.ant.design` 指到 ant-design.github.io。

7. 完成，等待 DNS 生效。

---

## beta 版本

流程基本如上。仓库地址为：https://github.com/ant-design/beta.ant.design

注意 CNAME 内容保持为 `beta.ant.design`。