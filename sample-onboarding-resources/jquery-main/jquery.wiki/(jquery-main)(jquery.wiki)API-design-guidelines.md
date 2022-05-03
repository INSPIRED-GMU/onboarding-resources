jQuery Core project guidelines:
* **Provide a set of APIs that work consistently across supported browsers.**
* **Document exceptions where consistency is impractical or impossible.**
* **Work with browser makers to make the web platform behave consistently.**

jQuery API guidelines:
* **Avoid Boolean traps.** - In particular, there should never be more than one Boolean value in an API signature. Booleans should be avoided in general, since they are not self-documenting.
* **Avoid global state.** - APIs such as `jQuery.ajaxSetup()` affect behavior globally, making it difficult for a plugin author to depend on default values. We will avoid these types of APIs in the future.
* **Prefer using existing public methods over private references or reimplementations** - Such exposed plumbing was a prominent characteristic of early releases, and many downstream libraries ["duckpunch"](https://en.wikipedia.org/wiki/Monkey_patch) internal utilities as de facto hooks. Note, however, that this guideline does not require introducing _new_ public interfaces.
* **Undocumented inputs result in unpredictable output.** - The API may throw an error inside jQuery, do nothing, or have some unpredictable behavior. This may change without warning across versions, even patch versions. However, each change will be evaluated by the team on a case-by-case basis to determine if a thrown error will disrupt too many users. In that case, we will warn about this change and include it in a minor or, more probably, major version.
* **Use `.api(name)` for getters and `.api(name, value)` for setters.**
* **A getter on an empty jQuery collection returns `undefined`.**
