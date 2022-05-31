New features, research paper code implmentation, bug fixes, documentation
and any other changes to the code base are subject to code review.

Reviewing code from contributors such as a pull request is a crucial component
of TensorFlow Model Garden development.
We encourage anyone to start reviewing code submitted by other developers,
especially if the feature is something that you are likely to use.

Here are some questions to keep in mind during the code review process:

* Do we want this in the TensorFlow Model Garden?
  * Is it likely to be used? Do you, as a TensorFlow user,
  like the change and intend to use it?
  * Is this change in the scope of TensorFlow?
  * Will the cost of maintaining a new feature be worth its benefits?
* Does it include documentation?
* Is the code human-readable?
  * Is it low on redundancy?
  * Should variable names be improved for clarity or consistency?
* Is the code efficient?
  * Could it be rewritten easily to run more efficiently?
* Will the new code add new dependencies on other libraries?
