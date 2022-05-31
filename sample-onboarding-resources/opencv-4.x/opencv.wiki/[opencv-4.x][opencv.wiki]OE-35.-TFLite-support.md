## Add import for TFLite models format

* Author: Julia Bareeva
* Link: [#13918](https://github.com/opencv/opencv/issues/13918)
* Status: **WIP**
* Platforms: **All**
* Complexity: 1-2 man-months

## Introduction and Rationale
TensorFlow Lite is a framework for on-device inference. Usually, a model file size can be very large but if we convert it to TFLite it can become mobile-friendly and be used on small devices. Also, TFLite supports quantized networks and could be a good platform for quantization support experiments in OpenCV.

## Proposed solution
We can support import from *.tflite files in the same way we do for *.pb files (TensorFlow format). To do this, we need to be able to parse files in Flatbuffer format and generate schema.
Technical details:
- Flatbuffer should be built from sources with OpenCV; Build guide: https://google.github.io/flatbuffers/flatbuffers_guide_building.html
- A lot of layers have already been implemented and can be reused
- Additional layers to support: TFLite_Detection_PostProcess
- Supported operating systems: Android, Windows, MacOS X, Linux
- Schema file should be generated during build (via CMake)
    - [TFLite Schema](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema.fbs) can be built by
     `./flatc -c ./schema.fbs --gen-mutable`
    - [How to generate schema during build in CMake](https://github.com/google/flatbuffers/issues/5548)

## Impact on existing code, compatibility

In general, the existing interface shouldn't change much.

## Possible alternatives
TFLite models can be converted to a frozen TensorFlow graphs:

```bazel run --config=opt //tensorflow/lite/toco:toco -- --input_file=model.tflite --output_file=graph.pb --input_format=TFLITE --output_format=TENSORFLOW_GRAPHDEF```

But this doesn't work for all. For example, there are several known problems for mediapipe models: https://github.com/google/mediapipe/issues/2770

## References

Related feature requests from OpenCV forum:

[Does readNetFromTensorflow support ".tflite" format?](https://answers.opencv.org/question/209280/does-readnetfromtensorflow-support-tflite-format/)

[Include .tflite or .pb files](https://forum.opencv.org/t/include-tflite-or-pb-files/3966)

[Tensorflow lite Graph with OpenCV DNN](https://answers.opencv.org/question/213204/tensorflow-lite-graph-with-opencv-dnn/)
