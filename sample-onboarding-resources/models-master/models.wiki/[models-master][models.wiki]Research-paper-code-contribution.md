# How to contribute a research paper code implementation

[![help wanted:paper implementation](https://img.shields.io/github/issues/tensorflow/models/help%20wanted%3Apaper%20implementation)](https://github.com/tensorflow/models/labels/help%20wanted%3Apaper%20implementation)

We encourage researchers to publish new state-of-the-art
machine learning models to the TensorFlow Model Garden.

To contribute a new research paper code, **please provide your plans using GitHub
issues in this repository before making any pull requests**.

## Requirements

We want to ensure research code implementations from contributors are
high-quality and well-documented.

Your contributions must meet the following requirements to be accepted to
the TensorFlow Model Garden repository.

| Directory | Requirements |
|-----------|--------------|
| [official](https://github.com/tensorflow/models/tree/master/official) | • Provide a model implemented in TensorFlow 2<br />• Use the modelling libraries provided by the Model Garden<br />• Provide baseline results<br />• Support distributed training on GPUs ***and*** TPUs<br />• Reasonable performance on GPUs ***and*** TPUs<br />• Need a SLA (Service Level Agreement) for community support<br />• Pass the TensorFlow code usability review process |
| [research](https://github.com/tensorflow/models/tree/master/research) | • Provide a model implemented in TensorFlow 2<br />• Use the modelling libraries provided by the Model Garden for supported ML tasks<br />• Provide baseline results <br />• Reasonable performance on GPUs ***or*** TPUs<br />• Need a SLA (Service Level Agreement) for community support  |
| [community](https://github.com/tensorflow/models/tree/master/community) | • Models implemented in TensorFlow 2 by external contributors<br />• Reproduce the paper results<br /> |

### Model selection

* A model from the paper accepted at top machine learning venues or
* A state-of-the-art model from a pre-publication available at [arXiv](https://arxiv.org/)

### Model accuracy and performance

* Should be able to reproduce the same results in a published paper
* Should provide reasonable out-of-box performance
  * Should have accuracy and performance test results on GPUs or TPUs

### Pre-trained models

* Pre-trained models in TensorFlow SavedModel format should be published
  to [TensorFlow Hub](https://tfhub.dev/).

### Documentation

* Use the [README template](https://github.com/tensorflow/models/blob/master/.github/README_TEMPLATE.md) that describes the information required for publishing a new code implementation.
* We also recommend to use [Read the Docs](https://readthedocs.org/) for hosting documentation.
  * Documentation can be automatically generated from your repository.
  * Please see [Read the Docs Template](https://github.com/readthedocs/template/tree/master/docs).

Note: Exceptions can be made case by case basis.
