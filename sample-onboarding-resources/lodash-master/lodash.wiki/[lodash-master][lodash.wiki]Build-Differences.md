A summary of differences between various [custom builds](https://lodash.com/custom-builds) created by [lodash-cli](https://www.npmjs.com/package/lodash-cli).

 * __Core build__<br>
 `lodash core`
   - 4 kB (gzipped) core build (63 methods; Backbone ≥ v1.3.0 compatible)<br>
     `_.assignIn`, `_.before`, `_.bind`, `_.chain`, `_.clone`, `_.compact`,
     `_.concat`, `_.create`, `_.defaults`, `_.defer`, `_.delay`, `_.each`,
     `_.escape`, `_.every`, `_.filter`, `_.find`, `_.flatten`, `_.flattenDeep`,
     `_.forEach`, `_.has`, `_.head`, `_.identity`, `_.indexOf`, `_.isArguments`,
     `_.isArray`, `_.isBoolean`, `_.isDate`, `_.isEmpty`, `_.isEqual`, `_.isFinite`,
     `_.isFunction`, `_.isNaN`, `_.isNull`, `_.isNumber`, `_.isObject`, `_.isRegExp`,
     `_.isString`, `_.isUndefined`, `_.iteratee`, `_.keys`, `_.last`, `_.map`,
     `_.matches`, `_.max`, `_.min`, `_.mixin`, `_.negate`, `_.noConflict`, `_.noop`,
     `_.once`, `_.pick`, `_.reduce`, `_.result`, `_.size`, `_.slice`, `_.some`,
     `_.sortBy`, `_.tap`, `_.thru`, `_.toArray`, `_.uniqueId`, `_.value`, & `_.values`
   - Limitations
      - No `_.matchesProperty` iteratee shorthand
      - No deep property path support
      - No lazy evaluation
      - No placeholder support
      - No robust cloning (arrays & plain objects only)
      - No support for maps, sets, & typed arrays

 * __Strict build__<br>
 `lodash strict`
   - Methods like `_.assign`, `_.bindAll`, & `_.defaults` throw errors when
     attempting to overwrite read-only properties
