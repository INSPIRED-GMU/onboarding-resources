* Ensure all milestoned issues/PRs are closed, or reassign to new milestone
* Verify good Testswarm results; run tests in browsers which failed some tests locally (sometimes it's caused by TestSwarm itself):
  - http://swarm.jquery.org/project/jquery
* Run any release-only tests, such as those in the `test/integration` folder.
* Make sure latest Travis build for [a relevant branch](https://travis-ci.org/jquery/jquery/branches) is green; if not, restart a job or run `npm test` locally to verify.
* Ensure AUTHORS.txt file is up to date (jquery-release will abort otherwise)
  - Get recent authors with `grunt authors`
  - Look for *bad* names/emails and update `.mailmap` using real data from CLA sheet if needed
  - Run `grunt authors` again, tack new emails onto AUTHORS.txt
* Create draft blog post on blog.jquery.com; save the link, it will be needed during the `jquery-release` process
  - Highlight major changes and reason for release
  - Add contributor list generated above
  - Add changelog generated above
* Do release using instructions at [jquery-release project README](https://github.com/jquery/jquery-release#readme)
  - Be sure to clone a CLEAN copy, don't reuse
  - Target something other than jquery/jquery (like your own fork) for a dry run
* Verify that files were created correctly by jquery-release
  - jquery-VER.js, jquery-VER.min.js, jquery-VER.min.map
  - jquery.js, jquery.min.js, jquery.min.map
  - mscdn-jquery-VER.zip, googlecdn-jquery-VER.zip
* Publish post on http://blog.jquery.com
* Add a link to the blog post and a short description of the release to GitHub releases.
* Tweet the release on http://twitter.com

== beta and release candidates can stop here ==

* Close the milestone matching the current release: https://github.com/jquery/jquery/milestones
* Update the shipping version on http://jquery.com home page 
```js
git pull jquery/jquery.com
# (Edit to update index.html and download.md here)
git commit
npm version patch
git push origin main --tags
```
* Email hosted-libraries@google for Google CDN
  - Send googlecdn-jquery-a.b.c.zip via a dropbox link
* Email damian.edwards@microsoft, Pranav.Rastogi@microsoft, and Chris.Sfanos@microsoft
  - Send mscdn-jquery-a.b.c.zip via a dropbox link
* Email CDNJS folks ryan@ryankirkman and thomasalwyndavis@gmail
  - Just point them to the blog post, which has links to the CDN copies.
