### v5.0.0 (~2021)

 * Discontinue [lodash-cli](https://www.npmjs.com/package/lodash-cli) in favor of bundling with [webpack](https://www.npmjs.com/package/webpack)
 * Discontinue [per method packages](https://www.npmjs.com/browse/keyword/lodash-modularized) in favor of modular [lodash](https://www.npmjs.com/package/lodash)
 * Drop support for unmaintained Node.js versions *(0.10, 0.12, 4, 5)*
 * ES2015+ syntax using [babel-preset-env](https://github.com/babel/babel-preset-env)
 * Split “Collection” methods into array & object methods
 * Remove monolithic entry point in favor of cherry-picking with [babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash)
 * Remove shorthand support by default
 * Remove `_.ary`, `_.assignWith`, & `_.find`
 * Remove `_.bind`, `_.curry`, `_.rest`, & `_.spread` variations in favor of built-in syntax
 * Remove `_.omit` in favor of only `_.pick`
 * Remove `_.partial`, `_.partialRight`, & `_.wrap` in favor of arrow functions
 * Remove `_.sortBy` in favor of `_.orderBy`
 * Remove `_.template` & `_.templateSettings` in favor of string template
 * Reduce `lodash` package size by more than 94%
   * Minify & gzip modules *(will use a .gz loader)*
   * Move `lodash/fp` back to `lodash-fp` _(35% savings)_
   * Possibly move browser/core monolithic bundles to a separate package
 * `camelCase`, `startCase`, `upperCase`, `kebabCase`, `lowerCase` and `snakeCase` do not deburr letters

### Implemented

 * Absorbed `_.sortByAll` into `_.sortBy` _(v4.0.0)_
 * Added alias for `_#value` & API to replace the root value of a chain sequence _(v3.2.0)_
 * Added AMD, ES, Node.js, & per method packages _(v2.0.0, v3.0.0)_
 * Added deep property helpers _(v3.7.0)_
 * Added implicit chaining _(v1.0.0-rc.3)_
 * Added lazy evaluation to chaining methods _(v3.0.0)_
 * Added math helpers _(v3.4.0)_
 * Added string methods like `startsWith`, `endsWith`, & `trim` _(v3.0.0)_
 * Added `_.mapKeys` _(v3.8.0)_
 * Added `_.spread` _(v3.2.0)_
 * Aligned `_.defaults` & `_.extend` with `Object.assign` _(v0.10.0)_
 * Aligned `_.isFinite` & `_.keys` with ES2015 _(v3.0.0)_
 * Changed default filename of compiled templates to `lodash.templates.js` _(v3.0.0)_
 * Created a small 4 kB core build  _(v4.0.0)_
 * Dropped IE 6-8 support _(v4.0.0)_
 * Dropped Node.js 0.6 support _(v3.0.0)_
 * Dropped Node.js 0.8 support _(v4.0.0)_
 * Enabled `_.merge` to deep merge properties onto functions _(v4.0.0)_
 * Dropped support for the `csp`, `legacy`, `mobile`, & `underscore` builds _(v3.0.0)_
 * Made `_.flatten` shallow by default instead of deep _(v3.0.0)_
 * Made `_.forEach` implicitly end a chain sequence _(v4.0.0)_
 * Made `_.max` & `_.min` non-chainable by default _(v3.0.0)_
 * Moved website to [Netlify](https://www.netlify.com/) _(Sept. 2016)_
 * Split out `_.max`, `_.min`, `_.sum`, & `_.uniq` _(v4.0.0)_
 * Renamed `_.createCallback` to `_.callback` _(v3.0.0)_
 * Removed the `data` parameter from `_.template` _(v3.0.0)_
 * Removed result sorting from `_.functions` _(v3.0.0)_
 * Removed `_.findWhere`, `_.pluck`, & `_.where` _(v4.0.0)_
 * Removed aliases _(v4.0.0)_<br>
   `_.all`, `_.any`, `_.backflow`, `_.callback`, `_.collect`, `_.compose`, `_.contains`,
   `_.detect`, `_.foldl`, `_.foldr`, `_.include`, `_.inject`, `_.methods`, `_.object`,
   `_#run`, `_.select`, & `_.unique`
