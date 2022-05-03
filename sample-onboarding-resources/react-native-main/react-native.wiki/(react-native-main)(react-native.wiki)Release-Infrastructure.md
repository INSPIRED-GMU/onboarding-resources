## Add `unless:` condition to any new workflow
This is a brain dump of the infrastructure we use to release React-Native. 

We use CircleCI workflows to publish our release to npm. Here are some brief points about that:
* CircleCI allows configuration of the following (ordered from largest superset to smallest)
  * pipelines - We only have one, `react-native`
  * workflows - These are the ones configured [here](https://github.com/facebook/react-native/blob/main/.circleci/config.yml#L854)
  * jobs - These are configured [here](https://github.com/facebook/react-native/blob/main/.circleci/config.yml#L854)
  * steps - Every job has a certain number of steps
* We have 2 workflows dedicated to releases: `package_release`, `publish_release`
* We first run `package_release` that basically just runs this script: https://github.com/facebook/react-native/blob/main/scripts/prepare-package-for-release.js
* In `prepare-package-for-release.js` we commit the changes, which triggers the `publish_release` workflow. CircleCI allows triggers of git tags or branch pushes 

To trigger `package_release` workflow, we leverage the CircleCI API. However, there are limitations to the CircleCI API where you cannot trigger a workflow individually, you can only trigger at a pipeline level.

The suggestion to trigger a single workflow is to add a conditional on every other workflow that is always true. See this: https://support.circleci.com/hc/en-us/articles/360050351292-How-to-trigger-a-workflow-via-CircleCI-API-v2

***Important* ** That means that whenever you add a new workflow, you should add: 
```
  my_new_workflow:
    unless: << pipeline.parameters.run_package_release_workflow_only >>
    ...
```