## Ant Design PR Principle

\[[**中文版**](https://github.com/ant-design/ant-design/wiki/PR-%E8%A7%84%E8%8C%83)]

0. This principle is suitable for [ant-design]( http://github.com/ant-design/ant-design) and [ant-design-pro](http://github.com/ant-design/ant-design-pro).
1. [As current agreement](https://ant.design/docs/react/contributing#Branch-Organization), all the `new feature` **must PR** to `feature` branch.
2. `new feature` contains new feature added, obviously UI modification, interactive update, reconstruction, etc.
3. `feature` branch is locked and not allow push code directly. **All the modification must use Pull Request**.
4. **Use follow PR template to submit feature related info**.
5. CI and other check tools pass.
6. **Modification must contains related changelog which contains truthful feedback to user**, and also easy for releaser to check.
7. Merge PR must get at least **one another collaborator**'s approve.
8. Daily bugfix, doc update, site maintain, branch merge is free for the principle (But still update through PR for trace).
9. Ant Design official maintainers must comply with the principle. Other contributor can use PR template optional. 

### Pull Request Template

```
### This is a ...

- [x] New feature
- [ ] Other

### What's the background?
  
> 1. Describe the source of requirement.
> 2. Resolve what problem.
> 3. Related issue link.
  
### API Realization
  
> 1. Basic thought of solution and other optional proposal.
> 2. List final API realization and usage sample.
> 3. GIF or snapshot should be provided if includes UI/interactive modification.
  
### What's the affect?

> 1. Does this PR affect user? Which part will be affected?
> 2. What will say in changelog?
> 3. Does this PR contains potential break change or other risk?

### Self Check before Merge

- [x] Doc is ready or not need
- [x] Demo is provided or not need
- [x] TypeScript definition is ready or not need
- [x] Changelog provided

### Additional Plan?

> If this PR related with other PR or following info. You can type here.
```

---

Sample：https://github.com/ant-design/ant-design/pull/14003