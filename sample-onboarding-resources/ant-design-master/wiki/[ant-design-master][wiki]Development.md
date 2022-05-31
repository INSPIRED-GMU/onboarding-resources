## Folders

```
├── components    # react source code and demos
├── docs          # documentation in markdown
├── scripts       # 
├── site          # website layout and code
└── package.json
```

## Local development

`Fork` and `git clone`.

```bash
$ npm install
$ npm start

// change start theme
$ DEV_THEME=dark npm start
```

Then visit http://127.0.0.1:8001

---

## Test Case and Lint

### lint source code

```bash
$ npm run lint
```

### Run all test cases

```bash
$ npm test
```

### Run test cases for one file

```bash
$ npm test components/button/__tests__/index.test.js
```

### Update snapshot files

```bash
$ npm test -u
```

---

## Publish site to [gh-pages](http://ant.design)

```bash
$ npm update && npm run deploy
```

npm publish tip for Administrators：[[轮值规则和版本发布流程]]