# 2021  OpenCV Technical Committee

* [Markdown Syntax](https://guides.github.com/features/mastering-markdown/)
* OpenCV
   * [OpenCV Home Page](https://opencv.org/)
   * [OpenCV Developer Site](https://github.com/opencv/opencv/wiki)
   * [OpenCV Meeting Notes Home](https://github.com/opencv/opencv/wiki/Meeting_notes)

[[Meeting_notes]]

# Template

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-mm-dd

## __*Agenda*__
* 

### *__Minutes__*
* 

### *__To Dos__*
* Name
  - [ ] todo


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-12-29


### *__Minutes__*

### Done:
* Shiqi: argmax and argmin parsing for tensorflow (PR#21268)
* Alexander S: Reviewed and tested PRs and issues ## 21351, 21349, 21337, 21312, OpenCv-Python ## 594, 599.
* Alexander S: Helped Andrey with OpenCV-Python release.
* Andrey: Updated submodules in opencv-python repository for 3.4 and master branches to release tags.
* Andrey: Created OpenCV python packages releases with 3.4.17.61 and 4.5.5.62 versions.
* Egor: Reviewed:
   * dnn: improve logging, catch import errors #21322
   * dnn: do not try to rebuilt network during setInput() #21323
* Alexander P: issues Aruco detectMarkers crashing #595 and cv::aruco::refineDetectedMarkers change detectedCorners[i] shape in some cases #14014
   * API change for detectMarkers() is being prepared (for consistency in OpenCV).
   * Errors are fixed, tests are prepared.

### In progress:
* Egor: [Finished Broadcast layer](https://github.com/rogday/opencv/tree/broadcast) for CPU and OpenCL targets; WIP on rewrite using memcpys since CUDA’s TensorView doesn’t support strides and hence subviews of appropriate type. This should speed up CPU and OpenCL as well.



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-12-22

### *__Minutes__*

* Vadim:
  * Ficus: implemented draft version of ONNX parser (based on protobuf-c) for Ficus. As expected, ONNX structure is conveniently represented in Ficus. The next goal is to implement some of the operations and the inference pipeline, enough to run face detection using YuNet or YOLO, classification using Resnet etc.
  * OpenCV China:
    * fixed problem incorrect results/crashes when processing small images with Tim-VX backend.
    * most of the layer tests now pass, with a notable exception of Leaky-ReLU. Tim-VX implementation is fixed-point, so it produces a LUT slightly different from the reference C implementation.
    * problem with different hash sums of .zip archives is still unsolved and would probably be difficult to solve.
    * experiments on per-channel vs per-tensor quantization are in progress.
* Alexander V:
  * The team is working on pre-release package validation.
  * 4.5.5 Changelog placeholder at Wiki: https://github.com/opencv/opencv/wiki/ChangeLog#version454
  * The team has fixed some issues found by Klocwork: https://github.com/opencv/opencv/pull/21267
  * Lapack patch has been merged: https://github.com/opencv/opencv/pull/21114
  * C++ and Python spectrogram samples has been merged: https://github.com/opencv/opencv/pull/20934
  * Integration Audio I/O functionality into GSoC speech recognition sample is going to be merged soon: https://github.com/opencv/opencv/pull/21197
* Alexander S:
  * Done:
    * Egor: Merged:
       * const/x fix for Div PR.
       * Flatten fix for ONNX PR.
       * Add celu, hardsigmoid, selu, thresholdedrelu layers PR.
       * Add acos, acosh, asin, asinh, atan, atanh, cos, cosh, erf, hardswish, sin, sinh, softplus, softsign, tan layers PR.
    * Egor: Reviewed:
       * add argmax and argmin parsing for tensorflow #21268.
       * dnn(test): update ONNX conformance filters (4.x) #21265.
       * Fixed several issues found by static analysis #21267.
    * Alexander P: Update ArUco tutorial #3126:
       * Fixed and merged. In total:
       * fixed ArUco, ChArUco, diamonds, calibration chapters;
       * added read dictionary and read params API;
       * added calibration photos;
       * added tests of tutorial to avoid regression;
       * added aruco_samples_utility.hpp to avoid code duplication.
       * on sick leave currently.
    * Andrey: Tested OpenCV python packages building after merging the PR with changes for python limited API support on all platforms and different python versions.
  * In progress:
    * Egor: Benchmarked attempts #1 and #2 of general broadcasting implementations, they turned out to be pretty slow. WIP on dims*log(MAX_DIM) solution - it is working and is faster than alternatives, but I think I need to get rid of allocations.
* Shiqi:
  * 2 PRs have been merged from the students:
    * Square operator from TF
    * batch Mat mul
  * argmax, argmin for TF is in progress.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-12-15

### *__Minutes__*

* Vadim:
  * Ficus: compiler quality and the standard library have been improved; performance of the all 5 benchmarks has been improved. The speed was re-measured on Mac M1: Ficus 1.0alpha+ is on on par with C++, faster than Julia 1.7 on 3 benchmarks, slower on the other two, noticeably faster than Python+numba.
  * OpenCV China:
    * Performance of Tim-VX backend was measured on Khadas board, YOLO v4 is 10x faster, Shiqi Yu's YuNet is 3x faster.
    * Many models from opencv model zoo have been quantized. There is some quality issue with some models, larger calibration dataset will be used.
* Alexander V:
  * The fix for PnPRansac with USAC parameters has been merged: https://github.com/opencv/opencv/pull/21166
  * PR about GStreamer support in Audio I/O is going to be created this week. It covers "wav" format only. "mp3" and media containers support will be added later.
  * ResizeLN fix is merged (the issue happened for depth >8U/8S, if the resizeLN OpenCL kernel is compiled without INTER_LINEAR_INTEGER, it gives invalid results): https://github.com/opencv/opencv/pull/21228
  * GTK2 with OpenGL compilation issue has been fixed: https://github.com/opencv/opencv/pull/21213
  * Levenberg-Marquadt algorithm implementation: PR was moved from draft to ready state, some comments already received: https://github.com/opencv/opencv/pull/21018
  * clip() was changed to avoid invalid memory accesses in RGB2Luv: https://github.com/opencv/opencv/pull/21111
* Alexander S:
  * ONNX: revised the test infrastructure significantly. The goal is to get automatically-generated table of supported operations in the default backend. The next goal is to provide more comprehensive table with information which operations are supported by which layer.
  * Aruco/Charuco: there is large patch in opencv_contrib that improves Aruco/Charuco. Those are useful algorithms; probably, at some point we will move them to the main repository.
  * OpenCV Python: we want to generate binary blobs (which are core parts of the current OpenCV bindings) that supports multiple versions of Python. Should be ready by OpenCV 4.5.5 (to be out in Dec 2021)
  * suggest to make wiki page about use of floating-point arithmetics in OpenCV. Vincent: can also describe the behaviour of empty matrices.
* Vincent:
  * working on removing C API from OpenCV-based products.
  * there is internal mesh simplification code, maybe it could be contributed.
* Anna:
  * Done:
    * Andrey: Tested python limited API for OpenCV python packages successfully. Modified scripts and CI/CD workflows in opencv-python repository to support python limited API. PR
    * Andrey: Replaced distutils with shutil for files in 4.x branch in opencv repository which are not located in 3.4 branch. PR
    * Egor: Fixed a few issues in MaxUnpool, ReduceMean/Max/Sum, Pad: fixed MaxUnpool missing attributes. fixed ReduceMean/Max/Sum keep_dims defaults and added support for keepdims=true in full reduction mode. added edge padding type to Pad.
    * Egor: ONNX conformance tests PR merged.
    * Egor: created OpenCV ONNX test summary table.
    * Egor: reviewed Add BatchMatMul layer support for tf_importer #21154,  Add Square layer support for tf_importer #21246.
  * In progress:
    * Andrey: Implementing download models function in a python package.
    * Alexander P: Update ArUco tutorial #3126. fix “Detection of Diamond Markers” (by using custom dictionary and custom detector parameters) and “Calibrate with ArUco and ChArUco” (by new calibration photos) chapters and samples. add indices and corners check to tests:
        * can_find_gboriginal
        * can_find_singlemarkersoriginal
        * can_find_choriginal
        * can_find_diamondmarkers
        now trying to pass the review.
    * Alexander P: Aruco detectMarkers crashing #595. Fixed type cast error, added test. PR is being prepared.
    * Alexander P: PR #20949 remap large images support. New solution to the problem was developed with Alexander Smorkalov, Vadim Pisarevsky and Alexander Alekhin.
    * Egor: Made a working version in prod(broadcasting dims) calls to copyTo() in my branch. WIP on log^d(max_broad_dim) version. The next step will be evaluation and I'll probably need to optimize away mat indexation since it reallocates internal buffers in each iteration.
* Shiqi:
  * one group students working on processing 3D point clouds. Suggested to use USAC, but they found they need to modify it. PR #21168 was submitted.
* Gary:
  * Funding from fway should be received very soon, it will be converted to new hire(s) who will work on robotics.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-12-08

### *__Minutes__*

* Vadim:
  * Ficus: continue to improve performance of the generated code, fixing bugs, adding functionality
  * OpenCV China:
    * working on Tim-VX (all 8-bit layers are now covered; trying to make a cmake script that will automatically download and build tim-vx from github).
    * working on OpenCV model zoo. Some models have been quantized; the quality is not measured yet.
* Anna:
  * Done:
    * Andrey: Moved cv2 binary from the root directory in OpenCV python package to the proper folder, the same as it locates in the original OpenCV build.
    * Andrey: The idea to keep extra imports for OpenCV python package in opencv repository is not very good, kept them in opencv-python repository and adapted to the changes.
    * Andrey: Replaced distutils module in opencv repository because deprecation warnings happen.
    * Alexander P: cv2.remap in the cv2.INTER_LINEAR has some problem in border values, issue #21148
there is no problem in INTER_LINEAR, INTER_CUBIC, ..., interpolations. The problem is in the matrix mapping.  The code fixing mapping was attached. issue was closed
    * Egor: Add ArgMax and ArgMin layers #21208 PR merged
    * Egor: Merged every fix to master locally to check ONNX score - 24.11%(it was 19.35%)
    * Egor: PRs merged: 
       * fix ceil_mode for Average/MaxPooling PR
       * Add alpha parameter to ELU layer PR
       * Add Log/Softmax simplification PR
       * Add default order to Transpose PR
       * add Sum of 1 input PR
  * In progress:
    * Andrey: Testing python limited API for OpenCV python package, which may reduce the opencv-python package size.
    * Andrey: Implementing downloading models function in a python package.
    * Alexander P: some samples from ArUco tutorial are not reproduced. prepared PR Update ArUco tutorial #3126; added new tests for tutorial; fixed flags and samples; added calibrate photos; added new custom dictionaries; refactoring samples of ArUco (-500 lines of code).
    * Egor: Implemented acos, acosh, asin, asinh, atan, atanh, cos, cosh, erf, hardswish, sin, sinh, softplus, softsign, tan layers #21176
    * Egor: Implemented celu, hardsigmoid, selu, thresholdedrelu layers #21190
    * Egor: WIP on general broadcasting layer
* Alexander:
  * The fix for PnPRansac with USAC parameters has been prepared: https://github.com/opencv/opencv/pull/21166
Aleksandr Alekhin provided some comments, they will be addressed by the author.
  * [GSoC 2021] DNN speech recognition sample PR is opened: https://github.com/opencv/opencv/pull/21197
  * In this PR Audio I/O functionality has been integrated into python sample (instead of using Python audio  library SoundFile). C++ sample is gong to be updated as well.
  * Filtering has been proposed for ONNX conformance tests suite: https://github.com/opencv/opencv/pull/21088
  * SO version will be increased each release to maintain ABI compatibility: https://github.com/opencv/opencv/pull/21178
  * Bit-exact tests for YUV cvtColor conversions have been implemented: https://github.com/opencv/opencv/pull/21193
* Vincent:
  * Fixing more fuzzer issues.
* Gary:
  * Thinking of robotic platform. It can be a combination of some hardware + software + courseware.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-12-01

### *__Minutes__*
* Vincent updated all to be 4.0
   * Fuzzing code and analyzing it with more tools
   * Intel team handling issues as they are found

* Vadim
1. OpenCV wrappers for Ficus (_new, efficient, easy functional language_) have been finished. Not all the functionality is available, but it will be extended later. Currently, the modules core, imgproc, imgcodecs, videoio, highgui and dnn are covered. Deep learning-based face detection sample has been ported to Ficus and works well
2. Ficus 1.0 alpha is released
3. Article on Ficus has been written (in Russian) and submitted to [habr.com](http://habr.com/). Awaiting for moderation. It will be translated and published at [opencv.org](http://opencv.org/) as well

* **Done:**
   * Alexander P: ArUco tutorial should contain camera parameters of example images [#3045](https://github.com/opencv/opencv_contrib/issues/3045)
      * [PR](https://github.com/opencv/opencv_contrib/pull/3120) was merged
   * Andrey: Fixed the [issue](https://github.com/opencv/opencv-python/issues/569) when pyinstaller does not know about extra config files of OpenCV python packages, [PR](https://github.com/pyinstaller/pyinstaller-hooks-contrib/pull/354) was merged in pyinstaller repository.
   * Egor: ArgMax [PR](https://github.com/opencv/opencv/pull/20733) merged.
   * Egor: [fix](https://github.com/opencv/opencv/pull/21152) Clip, LeakyReLU, LRN, Split defaults PR merged.
   * Egor: ONNX model crash [issue](https://github.com/opencv/opencv/issues/21093) seems to be resolved - user mixed up the order of dimensions

* **In progress:**
   * Alexander P: some samples from [ArUco tutorial](https://docs.opencv.org/4.x/d9/d6d/tutorial_table_of_content_aruco.html) are not reproduced.
      * The [custom dictionary](https://sourceforge.net/projects/aruco/files/OldVersions/) was used to create the tutorial. This dictionary was added to OpenCV (BSD license).
      * Added some tests for checking the tutorial.
      * Added some snippets to integrate samples with tutorials.
      * The ability to run samples with images has been added (previously samples run only with videos).
   * Alexander P: cv2.remap in the cv2.INTER_LINEAR has some problem in border values, [issue #21148](https://github.com/opencv/opencv/issues/21148)
      * Found strange remap behavior at the border of the image. Solutions are considered.
   * Andrey: Working on moving extra imports and scripts from opencv-python repository to opencv repository.
   * Egor: implemented ONNX Backend API for [scoreboard in this](https://github.com/rogday/opencv/tree/onnx_backend_api) branch. Initial coverage of the ONNX standart is 19.35%.
   * Egor: found easy to fix issues in existing layers using ONNX [conformance tests](https://github.com/opencv/opencv/pull/21088), the percentage rose to 21.68%, which is not much, but considering we probably won’t be supporting control flow operations, it’s good enough. Opened PRs: 
      * fix ceil_mode for Average/MaxPooling [PR](https://github.com/opencv/opencv/pull/21159)
      * Add alpha parameter to ELU layer [PR](https://github.com/opencv/opencv/pull/21160)
      * Add alpha parameter to ELU (CUDA) [PR](https://github.com/opencv/opencv/pull/21161)
      * Add Log/Softmax simplification [PR](https://github.com/opencv/opencv/pull/21162)
      * Add default order to Transpose [PR](https://github.com/opencv/opencv/pull/21163)
      * add Sum of 1 input [PR](https://github.com/opencv/opencv/pull/21164)
   * Egor: WIP on layer implementation priorities.
   * Egor: WIP on ONNX conformance [tests](https://github.com/opencv/opencv/pull/21088) integration.

### *__To Dos__*
* Gary
  - [ ] Contact Future way

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-11-24

## __*Agenda*__
* 

### *__Minutes__*
* Released newest OpenCV python package
  * infrastructure to make it faster to update OpenCV python packages, contrib with stats
* Working on ONNX compatibility of architectures
  * Pull request for ONNX conformance tests across architectures
  * ArUco tutorial
* Valgrind is red while working. ongraphapi merged from last week
   * patches being prepared to fix
* tracking team asked cvalt update for js
   * https://github.com/opencv/opencv/issues/21070
* New odometry pipeline is coming
   * https://github.com/opencv/opencv/pull/21032
* new odometry PRs:
   * https://github.com/opencv/opencv/pull/20755
   * https://github.com/opencv/opencv_contrib/pull/3055
* New MPU board for testing
   * Resnet50 ... inference in 15ms
   * Working on pull request soon
* Looking at Fuzzer bugs: NAN, empty matrices, only one bad one found
* Bug #threads == #cores not necessarily a good idea with massive #s of cores at level of libc
* Finishing FICUS alpha 1.0
* **Done:**
   * Andrey: Created 4.5.4.60 and 3.4.16.59 releases of OpenCV python packages and tested it.
   * Andrey: Backed up all OpenCV python packages for all releases on the fileserver.
   * Andrey: Prepared a table with all releases of OpenCV python packages, it's packages (with or without contrib and headless) and a statistic of downloads for the last 3 months.
   * Andrey: Suggested a citation of opencv-python repository and opencv in the issue.

* **In progress:**
   * Egor: Created an issue containing a list with most of the problems that conformance tests surfaced.
   * Egor: Made a PR, adding ONNX conformance tests.
   * Egor: WIP on figuring out how ONNX-Scoreboard and ONNX-Backend python API works.
   * Andrey: Fixing an issue when pyinstaller does not know about extra config files of OpenCV python packages.
   * Alexander P: ArUco tutorial should contain camera parameters of example images #3045.
   * prepared PR add camera parameters for the tutorial #3120
   * Alexander P: ArUco tutorial, new issue was found:
      * some examples from the tutorial (Detection of ArUco Boards, Detection of ChArUco Corners, Detection of Diamond Markers, Calibration with ArUco and ChArUco) are not reproduced.
      * the cause of the error is found: the use of the marker dictionary has changed (presumably in this PR).
   * Alexander P: cv::aruco::refineDetectedMarkers change detectedCorners[i] shape in some cases #14014
   * received a PR review. It takes several hours (mb 1-2 days) to change the API.
   * Alexander P: Remap does not support images longer than 32k pixel #4694
   * Add Q notation info to docs. Looking forward to the next review.


### *__To Dos__*
* Name
  - [ ] todo


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-11-17

### *__Minutes__*

* Alexander:
  * OSPP PR about QR encoding has been merged on this week: https://github.com/opencv/opencv/pull/17889
  * C++ and python samples of spectrogram feature PR has been opened: https://github.com/opencv/opencv/pull/20934
  * Rostislav is redesigning Levenberg-Marquadt algorithm for both sparse and dense matrices (needed for pose graph optimization) https://github.com/opencv/opencv/pull/21018
  * Implementation of GStreamer support in Audio I/O is in progress (Windows support is already merged).
* Julia:
  * Done:
    * Andrey: Prepared source packages for all old OpenCV python releases and tested to build it locally.
    * Andrey: Made a backup for OpenCV python packages which are removal release candidates on a file server.
    * Andrey: Updated 3.4 branch after new changes in the master branch in opencv-python repository.
    * Alexander P: issue “gen_pattern.py doesn't work” #21026. PR "fix markers parse in doc/pattern_tools/gen_pattern.py" was merged ##21028
    * Julia: triaged and submitted issue: cuda::remap never stops in case of overflow and params INTER_CUBIC, BORDER_REPLICATE #21042
  * In progress:
    * Egor: fixed ArgMax PR, it’s ready for review.
    * Egor: ONNX tests: roughly clustered errors; code coverage increased. *The idea is to form a subset of DNN tests with specially formed names that match ONNX operation names (as in the standard), so that we will have automatically generated list of ONNX operations supported by OpenCV*
    * Andrey: Preparing a new release for OpenCV python packages with fixes.
    * Alexander P: issue “Python binding with cv.aruco.refineDetectedMarkers #14014“ tests and PRs (#3105 #935) were prepared checked  the status of the tests and the module
    * Alexander P: Remap does not support images longer than 32k pixel #4694 fixed PR after review
    * Julia: started working on TFLite importer: investigated ability to generate schema*.hpp file during build in CMake; preparation of evolution proposal is in progress
    * Julia: addressed some issues found on review: Add CUDA backend for LSTM layer #2093
* Vadim:
  * Ficus bindings for OpenCV is still in progress. 2 minor patches have been merged.
  * OpenCV China team continues working on NPU support in DNN, based on Tim-VX
  * Yuantao from OpenCV China has added a few models into opencv model zoo: tracking and Chinese text recognition.
* Vincent:
  * Fuzzer has found a few bugs in OpenCV.
  * Allow empty matrices in most functions
* Shiqi:
  * One group of students (working on car detection) have submitted another PR: https://github.com/opencv/opencv/pull/20904
* Gary:
  * Some more negotiations with Futureway.
  * Maybe it makes sense to organize something like GSoC (but maybe in a different format), say, find labs in some universities that could do OpenCV-related projects.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-11-10

### *__Minutes__*

* Vadim:
  * Ficus bindings for OpenCV is in progress; core & imgproc module are supported now, dnn is in progress.
  * OpenCV China continues working on NPU support in DNN, based on Tim-VX; 8-bit convolution is now working correctly and several issues with memory management have been caught and resolved.
* Shiqi:
  * The first patch from the group of students from Sustech supervised by Shiqi has been merged to OpenCV: https://github.com/opencv/opencv/pull/20784
  * 2 groups of students are working on OpenCV: the first one is working on plane detection and other point cloud processing algorithms. The second group is working on car detection in point clouds.
  * Last week had meeting with CSDN. Jia will be working on OpenCV knowledge tree. CSDN will help. There is also mirror of OpenCV at CSDN (more friendly for Chinese audience). There is also negotiation about organization of OpenCV conference in China in Spring-summer 2022.
* Alexander:
  * Alexander A has created 4.x and 5.x branches. Q: What to do with existing PRs?
  * Upgraded 3rd-party libprotobuf was upgraded to v3.19.1.
  * Found and fixed issue in trackbar::setRange().
  * cvat team submitted issue to OpenCV bug tracker: added MIL tracker. Deep learning-based trackers are not feasible because of the huge model size (~1Gb). **Would be nice to find and add to opencv_zoo more compact object tracking model**
* Julia:
  * Done:
    * Andrey: Fixed OpenCV packaging for Python 3.9. #572
    * Andrey: Fixed pylint no-member warnings for OpenCV python packages and autocomplete in IDE. #570
    * Alexander P: review radon PR #3090 user fixes (after first review) was checked PR was merged
    * Egor: reviewed #20904, it was merged.
    * Julia: investigated ability to import TFLite networks:
      * run simple sample to read model from flatbuffer
      * prepared draft branch w/ flatbuffer integrated to OpenCV CMake
    * Julia: reviewed: Uniqueness ratio support for cuda::StereoBM #3081 and #3091
  * In progress:
    * Andrey: Preparing source packages for old opencv-python releases.
    * Andrey: Updating 3.4 branch after new changes in master in opencv-python repository.
    * Alexander P: issue “gen_pattern.py doesn't work” #21026 fixed, prepared PR "fix markers parse in doc/pattern_tools/gen_pattern.py" #21028
    * Alexander P: issue “Python binding with cv.aruco.refineDetectedMarkers #14014“ the function returns matrices of different dimensions (for similar cases); error was found, the solution is being prepared. C++ reproducer was created
    * Egor: Figured out how onnx tests are being generated and why sionnx auto-generated tests require rewrite of onnx test infrastructure(tests are collected into a single list and we run out of RAM). Ran 717 ONNX tests on OpenCV and 133 of them seem to pass. In the process of figuring out whether code coverage increased or not.
    * Julia: add Erf layer: added perf and accuracy tests with basic trivial implementation using std::erf to compare; speed up implementation of cv::erf from 17 ms to 9 ms (try about 5 different approximations); but it's still not faster than trivial loop with std::erf (#14357)
* Vincent:
  * Couple of issues have been found by the sanitiser:
     * assert() is used instead of CV_Assert()
     * Rect::area() overflows.
* Gary:
  * negotiations with Futureway are at the final stage; some funding is hopefully coming.
  * need to design a robotics toolkit
  * AR/VR can become really big if it can be applied not just to games, but to repairing things/cooking etc.

## 2021-11-03

### *__Minutes__*

* Vadim:
  * Continue working on Ficus bindings for OpenCV.
  * OpenCV China team has prepared the draft version of [Tim-VX](https://github.com/VeriSilicon/TIM-VX) framework support that adds support for VeriSilicon-based ML accelerators. It's similar to Tengine backend. It's being debugged now.
* Shiqi:
  * Collected several ARM development boards that can be used with OpenCV. 2 of them are with NPU. One of them could use Tengine for NPU.
  * Tomorrow have meeting with CSDN; they will visit OpenCV China office. Probably there will be OpenCV "knowledge tree" at CSDN. Also, there will probably be "OpenCV conference".
* Vincent:
  * Migration to OpenCV 4.5.x is now complete. Now planning to slowly get rid of C API.
* Alexander:
  * Alexander A is going to create 4.x and 5.x branches (master will still exist; next will be completely replaced with 5.x): https://github.com/opencv/opencv/wiki/Branches
  * CMake now always builds "Release" configuration; before it was "Release" or "Debug" depending on system configuration.
  * cvtColor now supports 1-pixel (1x1) images.
  * Buildbot now builds OpenCV 5.x in static mode, some 3D tests fail. Rostislav is exploring this issue.
* Julia:
  * Done:
    * Alexander P: issue “Bug in cv::remap function” #18407. added assert to avoid bad case to PR #20911;
    * Alexander P: review radon PR #3090. create sample to compare with scikit-image radon version; crop image problem was found; slightly different result problem was found;
    * Andrey: Fixed the build from the source for OpenCV python packages. #577
    * Andrey: Updated common information in opencv-python repository. #578
    * Julia: fixed cuda::remap - illegal memory access #18224: Added overflow handling during conversion from float to int for LinearFilter and added regression test PR (in contrib) for remap in case of overflow
    * Julia: addressed issues found on review #14296: Move 16-bit tests for NonLocalMeans to its own test case and calculate distance for 16-bit as for norm_l1
  * In progress:
    * Alexander P: issue “Remap does not support images longer than 32k pixel” #4694 add check_remap_type PR #2091 rewritten PRs (#20949, #20911) descriptions; added assert to avoid bad case to PR #20911; Remap large images support #20949 added int32 to remap, enable int32 for CV_32FC2 map. Run old tests for new int32 remap and new tests with “big” (width/height large than 32767) images. Updated docs. prepared PR #20949 to review
    * Alexander P: issue Singular Value Decomposition #20975 checked, started debug
    * Andrey: Fixing OpenCV packaging for Python 3.9. #572
    * Andrey: Fixing pylint no-member warnings for OpenCV python packages and autocomplete in IDE. #570
    * Julia: WIP: Feature request: cv::erf() and cv::erfc() #14357 : looked at the existing approximation algorithms; this operation can be implemented using existed matrix ops
  * Org: 
    * Egor is on the sick leave
    * Alexander S. is on another project
    * Andrey was on vacation till Monday 
* Gary:
  * GSoC payments are done.
  * Probably will talk to one of car companies on the camera/sensor calibration.
  * OpenCV.org website is now completely belongs to OpenCV.org organization (all the legal process is complete, trademarks, rights are transferred etc.).

## 2021-10-27

### *__Minutes__*

* Alexander:
  * Maksim has prepared a script that downloads OpenCV, since OpenCV is now optional dependency of the upcoming OpenVINO releases, not the strict dependency anymore.
  * Audio I/O is now available on Windows (PR is merged); Linux version is still in progress, based on gstreamer.
  * Another intern (Maria) is working on spectrogram functionality; this is a sample that reads audio sample and computes FFT on it.
  * Maria is also working on polishing GSoC PR to prepare it for merge.
* Julia:
  * **xperience.ai** is now working on adding Transformers into OpenCV DNN.
  * Alexander P: minEnclosingTriangle() raises an error when input is vector<Point> #20890. Fixed, added tests, prepared and merged PR #20912
  * Julia: added tests for photo: Add support for CV_16U to cv::cuda::fastNlMeansDenoising
  * Julia: updated old PR w/ CUDA lstm layer and submitted it Add CUDA backend for LSTM layer #20938
  * Julia: prepared initial estimations of time and resources required to support Transformers NN (BERT, RoBERTa, GPT-2, T5, ViT etc)
  * In progress:
    * Alexander P: issue “Remap does not support images longer than 32k pixel” #4694. Prepared PR to make it easier to add int32 in remap.
    * Improved code coverage for remap/covertMaps by new param tests. Removed the wrong branch that is never called.
    * Add new types support for convertMaps (now any map type can convert to any other map type). Prepared draft PR for int32 remap.
    * Alexander P: issue “Bug in cv::remap function” #18407
    * Reproduced, create new reproducer. The cause and location of the problem was found. The solution is being prepared.
    * Julia: investigate cuda::remap - illegal memory access #18224
  * Org: 
    * Andrey is on vacation this week
    * Egor is on the sick leave
    * Alexander S. is on another project
    * Julia was on vacation till Monday 
* Gary:
  * GSoC mentors finally received the money (at least, most of them).
  * Playing with robotics "toy" car, but there are issues with battery and with resuming motion after sudden stop.
  * Camera calibration revision. Maybe it can be a commercial solution (with WebUI)?

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-10-20

### *__Minutes__*
* Vadim:
  * Added 2 little features to Ficus, merged one patch from the contributor. Continue working on OpenCV wrappers.
* Alexander:
  * Audio I/O on Windows is done; Linux part is in progress (gstreamer-based).
  * Open Model Zoo is being revised - which models are not supported by default backend of OpenCV DNN.
* Shiqi:
  * Gave talk to Baidu; introduced OpenCV. There were questions about OpenCV 5 is release date :) have no definite answer for now.
  * There was question from NVidia China on whether OpenCV can support NVidia GPU better.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-10-13

### *__Minutes__*
* Vadim:
  * Resumed the work on OpenCV Ficus bindings
  * OpenCV China team started work on adding tim-vx backend to OpenCV DNN in order to support VeriSilicon NPU
* Vincent:
  * Continue working on upgrading internal projects to OpenCV (4.5.4).
  * ORB algorithm won a prestigious prize at ICCV as a great algorithm that influenced ORB.
  * Custom Input/OutputArray should be implemented in OpenCV 5. Will submit a feature request about it.
* Shiqi:
  * Giving talk at Baidu office, present OpenCV 5 roadmap and plans.
  * Giving another talk via CSDN (online) next weekend (the programmer's day) about open-source in general with OpenCV being used as example
* Alexander:
  * OpenCV 4.5.4 and 3.4.16 have been released: several GSoC patches have been merged: Julia bindings, 8-bit DNN, RISC-V optimization etc.
  * Audio I/O activities (using Windows Media Foundation Framework); GStreamer port has just started.
  * Rostislav and Artem continue work on 3D module; reviewed PR about 3D point cloud sampling.
* Anna:
  * Done:
    * Lydia: made and published final GSoC-21 video
    * Alexander: Finished initial NVIDIA OpticalFlow SDK integration for stereo matching in contrib (#3069). Enable NVIDIA OpticalFlow SDK support in core OpenCV and made related fixes in existing OpticalFlow code (contrib #3060, contrib #3070, #20843).
    * Alexander: Review PRs, tickets, helped to resolve issues with: contrib #3066, #3065, #3064, opencv #20809, 20471.
    * Egor: SoftNMS PR, YOLOV4x-mish new_coords CUDA PR, Sub interaction with constants PR, Sum asserts fix for ResNet101 PR merged.
    * Andrey: Fixed the build opencv-python packages on MacOS with Python 3.10 and prepared PR with Python 3.10 support on all platforms.
    * Alexander P: issue ONNX imported model fails with assertion on .forward() #20681
work on OpenCV 4.5.4 and 3.4.16, issue was closed,
    * Alexander P: issue ORB https://github.com/opencv/opencv-python/issues/537
created simpler reproducer;
added tests with required tags (CV_TEST_TAG_MEMORY_6GB, … );
checked performance test; PR was merged.
    * Julia: reviewed:  dnn: LSTM optimisation (#20658); Backport YOLOv4x-mish new_coords CUDA implementation (#20818) and 3D samples using OpenGL and GLFW (Mesh and point cloud visualization) #20371 (GSoC project)
  * In progress:
    * Egor: Exploring solutions for DNN matrix support implementation.
    * Egor: Refactoring PR adding Ceil, Floor, Round, Log, Sqrt, Exp, Not, Equal, Greater and Less layers.
    * Andrey: Including the python loader from opencv into opencv-python packages.
    * Julia: Add support for CV_16U to cv::cuda::fastNlMeansDenoising (#14296)
    * Alexander P: issue Alternative to cv2.warpPerspective #549
problematic cases in the code were considered;
to add support for large images need to fix “remap” also.
    * Alexander P: issue Remap does not support images longer than 32k pixel #4694
problematic cases in the code were considered. Implementation in progress.
    * Julia is on vacation this and next week
* Gary:
  * generic CV news: Vladlen K team has made some breakthrough in transfer learning.
  * also, there is excellent monocular stereo using transformers.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-10-06

### *__Minutes__*
* Working on more internal tests, almost done
* OpenCV customizable w different types and convert internally. Relieves user of having to convert.
* Shiqi
   * One week holiday in China
   * Will have a talk on line (ad is in Chinese, but at end in English, talk is in English):
      * https://mp.weixin.qq.com/s/cGFsWuxBNomaAU8wYy5e0g
* Intel team on release activities
   * Placeholder added to wiki 3.4, 4.5 end of this week
   * Cleanup of incomplete 18 issues 
   * Intern Anna testing DNN module. OpenVino accuracy checker from open model zoo
      * 2/3s models checked for accuracy (all fine so far)
      * Are discussing compatibility issues on the other 1/3 (size of input Tensor). Find and resolve issue next
* Would be nice to have tuning models PyTorch and TF with the model zoo
* Julia
   * 3.10 python version works except for issues on MacOS
   * Housekeeping issues -- 25
   * Cuda backend being updated

**Done:**
* Andrey: Changed environment for building opencv-python packages with Python 3.10 and successfully built it on Windows and Linux.
* Alexander: Reviewed, tested, helped to resolve issues with PRs: ## 20521, 20569, 20058, 20105, 20471, 20813
* Alexander: Recreated PRs with fixes for abandoned and incomplete ## 20770 (extra # 916), 20810.
* Alexander P: issue “Incorrect chessboard corners returned by findChessboardCornersSB #15712”:
   * feature maps has been attached to issue;
   * the ways of solving the is
   * the ways of solving the issue are suggested;
   * issue can be closed.
* Julia: reviewed blog post by GSoC student

**In progress:**
* Andrey: Trying to include LAPACK into opencv-python packages on Windows.
* Andrey: Fixing the build opencv-python packages on MacOS with Python 3.10.
* Egor: Fixed a bug in contributor’s implementation of SoftNMS, added a test, exposed the function to the public API, refactored the code and sent a PR.
* Egor: Backported CUDA implementation of YOLOV4x-mish new_coords, and sent a PR. 
* Julia Bareeva7:37 AM
* Alexander P: issue ORB https://github.com/opencv/opencv-python/issues/537
   * the problem was found: the integer overflow has occurred;
   * the problem was fixed;
   * the test case was added;
   **TO DO:** set tags test, rechecked performance test and create PR.
* Julia: fixed issue w/ data layout corruption for LSTM layer on CUDA backend
* Julia: addressed issues found on review to GSoC PR (module to save and load point cloud #20471); also added tests for Mesh' methods and refactored save\load functions, encoder finder etc.

**TF use comments**
* Keras stand alone under Google relying on stable TF deep learning, but high level pythonic API. But different APIs for embedded
* Brand new run time executor so that all the code will converted to small inner core. 
* Domain adaptation may be possible to embedded w/in separate domains such as robotic navigation, arms, etc
* PyTorch LLVM to work on common stack between network definition and low level

### *__To Dos__*
* Gary
  - [ ] GSoC Mentor payments

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-09-29


### *__Minutes__*
* Gary
   * Ordered parts for robotic rover
   * Working on early nets that would work as part of its brain
   * Fundraising
* Vincent
   * Kid is walking!
* tests for switching from <3.0 to 4 and 5.0 versions
   * Clang bug report issued <run test with thread sanitizer, crashes => found a bug, reading the same data at the same time>
       * A test needs to detect that
       * Sanitizer is finding things like this, especially when threads are high (>100)

### Done:
   * Alexander S: Reviewed, helped to resolve issues with PRs ## 20569, 20761, 20762, 20712, 20636, 20742, 
   * Alexander S: Extended C++ header parser to report file name and line number for errors #20754
   * Alexander S: Reworked community PR #20003 by PR 20770 and extra #916
   * Alexander S: Reviewed changes to OpenCV CN CI, fixed Python dependencies issue.
   * Alexander P: merged PR to add random checkerboard, issue #20735.
   * Andrey: Tested changes for extra dnn models downloading, fixed following issues and
   * Andrey: Fixed issues in including LAPACK into opencv-python packages on linux, packages were built and tested successfully (not released).
   * Julia: Prepared team scope for the current sprint

### In progress:
   * Alexander S: Review and testing of PR “Make the implementation of optimization in DNN adjustable to different vector sizes with RVV intrinsics. #20521”
   * Alexander P: issue “Incorrect chessboard corners returned by findChessboardCornersSB #15712”:
       * feature map printed, findChessboardCornersSB works correctly, need to update checkerboard.
   * Andrey: Trying to include LAPACK into opencv-python packages on Windows.
   * Andrey: Trying to build opencv-python packages using Python 3.10.
   * Julia: back to work on CUDA backend for LSTM layer:
   * Fixed issue w/ CUDNN_STATUS_BAD_PARAM; support CUDA streams at interface to avoid sync copy; fix issue w/ filter descriptor; support different runtime types
   * Egor: ArgMax/ArgMin: added NaN handling, non-continuous matrices are not being cloned(version that uses strides to iterate is too slow for some reason).
   * Egor: Implemented ArgMax/ArgMin layer for dnn module, didn’t open a PR yet since core functions aren’t merged.
   * Egor: Triaged outputBlobs reusing - every forward method except one seems to avoid copying data.
   * Egor: Reviewing ExpandDims PR.

### *__To Dos__*
* Gary
  - [ ] GSoC Mentor payments
  - [x] Video prep

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-09-15

### *__Minutes__*
* Consider putting together a 2nd build farm for thread sanitizers etc, maybe not for every build, but before releases etc
* Shiqi
   * Developing new layers for opencv dnn depth2point and a 2nd layer
   * Model zoo being expanded, maybe public at end of month
      * 4 HW models NVidia, Arm, Apple to evaluate DNN on embedded
* Julia
   * Python binding, fixed some issues, C++ types to python types
   * DNN models: min and max layers
   * Want to share a chart of what layers are ready, in development or not yet covered
   * Calibration model -- new checkerboard type, radon board generation
* Funding for viusal/deep robotics stack is (probably coming)
* GSoC payments for mentors are in

### *__To Dos__*
* Name
  - [ ] todo

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-09-08

### *__Minutes__*
* Shiqi:
  * opencv_zoo is now public; next week the first 4 models will be uploaded
  * opencv benchmark will be run first on Intel, RPi etc. (~4 configs)
* Vadim:
  * face detection functionality is nearly ready (patch by Yuantao Feng)
  * possibly we need to partly move OpenCV CI to Russia or some other place to pass by the firewall.
* Gary:
  * talking about extending robotics-related activities in OpenCV
* Anna:
  * Done:
    * Andrey: Prepared changes with the check if a list of extra dnn models changed in OpenCV Extra.
    * Egor: Fix hasDynamicShapes for batch_size and axis selection in Scale layer PR merged.
    * Egor: Fixed resize+concat optimization and got merged. Made a graph-cutting tool and found the problem in interaction   between BlobManager optimization of Concat layer and Resize layer with no work: output blob of Resize layer was changed, but the copy of input to output isn't performed.
    * Alexander P: 19 python-bindings issue checked and added to table.
    * Alexander P: fixed issue calcBackProject picks up values from the wrong cell of 3D-histogram #19001 by PR #20558
    * Alexander P: Checked and ping to close Size of control parameter issue in Kalman predict #8905
    * Alexander P: Checked and ping to close Pycharm Cannot find reference 'VideoWriter' in '__init__.py | __init__.py' #18728
  * In progress:
    * Egor: Add Normalize subgraph, support for starts<0 and axis<0 in Slice, Mul broadcasting in the middle and fix Expand's unsqueeze PR is in review.
    * Egor: The outputs of Darknet and OpenCV from YOLOv4x-mish fix branch seem to match after NMS, the current plan is to add a test, similar to YOLOv4 one.
    * Alexander P: minEnclosingTriangle Error using python3.8.3 on Windows #17585. The error was found. The fix is being prepared.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-09-03

### *__Minutes__*
* PRs & Issues:
   * python: cv.Mat wrapper over numpy.ndarray
     * AI Alexander Smorkalov: fix conflicts in [#20611](https://github.com/opencv/opencv/pull/20611) with Vadim Levin
     * Alexander Panov sort out all related issues.
   * AudioIO in VideoCapture (MSMF): [#19721](https://github.com/opencv/opencv/pull/19721) 
     * AI to All: review and comment


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-09-01

### *__Minutes__*
* GSoC 2021 has finished, we have 11 completed projects!
   * https://summerofcode.withgoogle.com/dashboard/
* Shiqi
  * Arm development board with MPU
     * meeting with maker 6 core board 5TF ops, ~$100
        * AM Logic, MPU can support many topologies
  * **Need more deep algorithms for OpenCV** -- need a list of what's missing
     * Need leader for each algorithm
     * Need to allow creates to contribute algorithms
     * Researchers to be involved who are devoted to specific areas
     * Shiqi to draft guidelines
* Vincent
   * Improving the failing tests
   * Bug for race condition filed
* Anna
   * Fixed many pull requests DNN, Stereo calibrating
   * Done:
      * Alexander P: issue #18412 “SystemError: <built-in function NMSBoxes>”: Checked the solution PR #20611. Issue is fixed.
      * Alexander P: issue #11085 “Python fisheye.stereoCalibrate: Assertion failed objectPoints.type()”: The example is reproduced. PR #20558 fixed the issue.
      * Alexander S: Reviewed PRs: 20562, 20471, 20598
      * Alexander S: Prepared the team scope for current sprint
   * In progress:
      * Andrey: Implementing a check if a list of extra dnn models changed in OpenCV Extra.
      * Egor: #18975: #19877 seems to be broken: the results of my test are diverging.
      * Egor: Made a partial c++ reproducer of #17726, the problem seems to be outside cpp-python bridge. The current plan is to cut the model into pieces until the error reveals itself.
      * Egor: #20605: tried a different approach: added initShapes function which would be called once before getMemoryShapes. Worked great in ONNX, but in TF shapes aren't present at all most of the time, so no shape propagation.
      * Egor: #20573 is approved.
      * Alexander P: Checking Python issues. A document is being prepared with a list of solutions to issue.
* Org:
   * Julia will start OpenCV Robotics area 
* Oak-D OpenCV AI Toolkit Competition:
   * Submissions for OpenCV Contest (1400 entries!) are now judged
      * **Totally awesome results**
   * 19 winners in all geographies
   * 10 will be sent for grand prize considerations
   * Will become weekly webinars (probably a year's worth)
* Aleksandr
   * New windows machine for builds
   * Maxim VPL integration added
   * GSOC all projects are fine -- one project needs additional weeks
   * Students preparing video presentations
* Gary
   * Working on OpenCV Robotics 
   * Ongoing Grant to fund
   * Talking with ME, EE guy for modifying eclectic carts
   * Ardupilot investigations
      * How to use with OAK-D
   * Plans for membership


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-27

### *__Minutes__*
* 4.5.4 release on October - community release on schedule.
* GSoC 2021 - this week -- deadline for mentors.
* Webfaction migration (deadline Sep 15):
   * Satya Mallick drives migration
* Still broken builds including precommits after #20228 merge
   * Vadim Pisarevsky will work on it on monday
* python: cv.Mat wrapper over numpy.ndarray (#20558) agree to merge.
* solveLP() infeasible results fix #19530 -- will be finished in a couple of weeks.
* Add CAP_PROP_STREAM_OPEN_TIME: #20591 
   * AI to Alexander Smorkalov to check if it works for all codecs.
* Runtime nlanes for SVE enablement #20562
   * SVE Register types cannot be stored as class/structure fields with current compiler implementation. It makes the PR useless.
   * Proposed to change SVE integration order: implement minimal SVE HAL first and proof the concept. Then change current HAL API to enable enhanced SVE optimizations. 
* Fix Octave Dependence in SIFT Descriptor Calculation #19994 -- AI to Vadim Pisarevsky to review and comment.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-25

### *__Minutes__*

* Vadim:
  * All the students evaluations are in. This week the mentors review the students' work.
  * Yuantao F from OpenCV China has prepared a draft version of opencv_zoo (the model zoo) together with an early draft of the benchmark - script that measures inference speed on a set of models and some tiny dataset on the specified hardware and reports the results.
  * My GSoC student, Jebastin Nadar, has nearly completed the project on DNN 8-bit quantization. One PR is merged, another one is pending. The final expected result is the tutorial — how to quantize ONNX networks and how to load and use the quantized networks within ONNX.
* Anna:
  * Reviewing OpenCV AI competition submissions (there are many of them: ~150). Going to give a talk with overview of the competition itself and some notable submissions.
  * **Done:**
  * Alexander P: PR “Update kalman sample”, issue #20091: merged
  * Alexander P: “cv2.stereoCalibrate behaves differently to c++ implementation”, issue #517: the reproducer is received. User error found. Right way to use the function was recommended.
  * Alexander P: “Different shape of result of the method HOUGH_GRADIENT_ALT in Python”, issue #19238:
found and fixed bug (cvMat with different dimensions were copied to OutputArray _circles)
created tests, created and merge PR #20584
  * Alexander P: cv2.HoughLinesP does not filter correctly lines according the minLineLength #10823: user error found. Right way to use the function was recommended.
  * Andrey: Changed the way how dnn models are used in OpenCV CN CI pipelines. PR with changes.
  * Alexander S: reviewed, tested, helped to resolve issues with PR #20564, 20556, 20471, 20521, 20598
  * Alexander S: Prepared team scope for the current sprint
  * Egor: Split partial sum PR merged; ONNXImporter diagnostic mode layer registration PR merged.
  * **In progress:**
  * Alexander P: issue #18412 “SystemError: <built-in function NMSBoxes>”: The reproducer is received. Python binding errors found.   Temporary way to use the function was recommended. The error fix is being prepared.
  * Alexander P: issue #11085 “Python fisheye.stereoCalibrate: Assertion failed objectPoints.type()”: The example is partially reproduced. I am trying to reproduce the whole example.
  * Lydia: talked to one of GSoC-21 students (Ricardo Antunes) about blog post, set up the publishing date 
  * Egor: waiting for review of hasDynamicShapes and axis selection in Scale layer fix
  * Egor: Added Normalize subgraph, support for starts<0 and axis<0 in Slice, Mul broadcasting in the middle and fixed Expand's unsqueeze and sent a PR
* Alexander:
   * cv.mat fix (#19091) which Aleksandr Alekhin is working on has been tested via speech recognition GSoC project. The student who is working on GSoC speech recognition project tested this patch — works well.
   * GSoC:
      * Intrinsics tutorial is considered by Vitaly as finished. PR is on review.
      * Loop closure project of Zihao Mu: should pass the final evaluation, report:    https://gist.github.com/zihaomu/4933dd1fb805cbb684e2b407e1e87e51
      * Loop Closure code is done, supports HF-Net through OpenVINO (high quality) or DeepLCD through OpenCV DNN (low/middle quality) +  ORB feature detector.
      * Things left: to find or to film an outdoor video to demonstrate better DeepLCD quality.
      * Loop closure project of Justin Wu: DBoW PR is done but no Loop Closure code itself. It could be integrated to Zihao's code. You gave him one/two weeks to finish.
      * Speech recognition project: the sample is ready. Student is preparing a video clip and a report.
* Gary:
   * continue looking for more OpenCV funding.
   * lidars are getting quite affordable, e.g.: https://www.cygbot.com/2d-3d-dual-solid-state-tof-lidar
* Shiqi:
   * GSoC project on 3D samples has been evaluated. The results are excellent.
   * Talked to one prof. There is an idea to make another "OpenCV development board" with ARM+NPU, e.g. something similar to this: https://en.t-firefly.com/product/industry/rocrk3568pc.html
* Vincent:
   * porting to the latest OpenCV (4.5.x) is in progress.
   * found some possible data races, if confirmed, a bug will be filed.
<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-20

### *__Minutes__*
* 5.0:
   * Moving RGBD parts to 3d ([#20013](https://github.com/opencv/opencv/pull/20013)/ [contrib#2936](https://github.com/opencv/opencv_contrib/pull/2936)) -- will be merged today.
* PR & issues:
   * load point cloud in 3d module ([#20471](https://github.com/opencv/opencv/pull/20471)) - should go to 3d module,but not new model
   * python: cv.Mat wrapper over numpy.ndarray ([#20558](https://github.com/opencv/opencv/pull/20558)) -- will discuss next time. AI to all review the patch and all related issues to have context for the discussion.
   * 8-bit quantization in dnn module and int8 layers ([#20228](https://github.com/opencv/opencv/pull/20228))
      * Vadim Pisarevsky will work on review issues
      * Current implementation fails tests time to time. AR to Vadim: Fix Precommits: "Linux AVX2", "Linux32", "Win32"
   * Runtime nlanes for SVE enablement #20562
      * complete results are required
      * Need to bring all technical discussions form e-mail thread to Github PR
      * Need clear technical statement in the PR: why and how it works.
      * Alexander & Alexander are against all related functions modification without actual add-value. Proposed alternative: add extra fields to the basic structures, if it’s required. Then propose RVV/SVE2/whatever backend to OpenCV. Then enable new options for functions one by one with performance control on all supported devices.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-18

### *__Minutes__*

* Vadim:
  * This week is the final GSoC evaluations: for most of the projects we have nice pull requests submitted, so there should not be any issues with them.
* Anna:
  * Done:
    * Alexander: Reviewed, tested, helped to resolve issues with PRs #20549, 20547, 20545, 20533, 20564
    * Alexander: Prepared technical proposal for OpenCV-Next architecture. Discussed internally.
    * Alexander: Prepared team scope for the current sprint.
    * Egor: gdb pretty-printer PR merged.
    * Egor: Added info about network optimizers to wiki. Created a list of all triaged networks and its diagnosis. Reviewed PPSeg model support PR: https://github.com/opencv/opencv/wiki/OpenCV-Debugging-Facilities#optimizing-the-network-to-make-it-easier-for-opencv-to-import-your-model
    * Alexander P: PR “MinAreaRect fix rotating calipers”, issue #19769: merged
    * Alexander P: PR “add note about Python's dsize to doc”, issue #19569: merged
    * Alexander P: checked and closed “Imgcodecs_Image.read_write jp2 test failure” #13818
  * In progress:
    * Egor: Fixed split partial sum issue and sent a PR; fix ONNXImporter diagnostic mode layer       registration is in review.
    * Egor: Partially triaged #20258 - a lot of unsupported layers + const propagation and ONNX model diagnostic tool segfaulted: it uses shape info during the import and if the layer is missing, it reads garbage; Didn’t come up with a solution yet.
    * Egor: Fixed hasDynamicShapes being set if only batch size is unknown for #20540, fixed Mul layer not setting the right axis for Scale layer, no PR yet.
    * Egor: Looking for a concise way to fix slice_layer.cpp not supporting axis<0 and starts<0: trivial solution works, but looks terrible.
    * Alexander P: submitted PR “Update kalman sample”, issue #20564.
    * Alexander P: checked #18412 “SystemError: <built-in function NMSBoxes>”, try to reproduce.
    * Alexander P: checked #517, “cv2.stereoCalibrate behaves differently to c++ implementation”, a reproducer was requested.
  * Org:
    * Julia is on the sick leave since last week  
* Shiqi Yu:
  * GSoC project 3D samples: the student has finished the project and prepared a nice blog post. Probably make sense to publish it at opencv.org.
  * Tested Feng Yuantao's port of libfacedetect face detector to OpenCV: https://github.com/opencv/opencv/pull/20422. It works well, new functionality is included into objdetect module, C++ & Python API is provided.
* Alexander:
  * We need to move to a new hosting for docs.opencv.org, pullrequest.opencv.org and some other OpenCV sites.
  * Alexander A is working on adding better cv::Mat wrapper to handle 1D and N-D matrices.
  * Allocated another machine to build packages for OpenCV next (5.x)
  * Maksim added 16-bit grayscale support to gstreamer backend.
  * 3D module: rgbd => 3d migration is almost complete. Most probably will be merged this or next week.
  * GSoC: Liubov's project on speech recognition is being finalized
  * GSoC: Vitaly's project on univ. intrinisic tutorial is being finalized as well.
  * GSoC: Rostislav's project is also finalized, not excellent results, but hopefully something useful.
* Gary:
  * there is friend who works on toy-like small trucks, but they can carry up to one adult or 2 children; it could be possible to play with autonomous driving, GPS tricks etc. using those trucks. It can be an attractive platform for developers/researchers.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-13

### *__Minutes__*
* PRs & Issues:
  * DNN : fix bug in extracting prior-box variances in detection output layer: [#20525](https://github.com/opencv/opencv/pull/20525) -- test required.
  * Adding option to use of single gpu in tests #20375 -- to close. AI to Alalek.
  * improve compatibility for qt 6. #20183
  * CMake may find qt6 instead of qt5. Reopen comments from Alalek (was marked as resolved by original author)
improve compatibility for qt 6. #20183
  * Al to Alexander Smorkalov: try builds with QT5 & QT6 and check if versions handled correctly.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-08-11

### *__Minutes__*

* Shiqi Yu:
  * H wants to join opencv.org, become a member.
  * It's suggested to make a short video with OpenCV 5.x highlights.
* Gary:
  * it's likely that opencv.org could secure a certain sum of money per year, which will help to have a steady development team.
  * RISC-V support is important and also very welcome.
  * There are many interesting robotic applications, e.g. cheap autonomous vehicles using differential GPS etc. (e.g. see ardupilot.org)
  * GSoC final evaluation starts next week.
* Vadim:
  * Still working on Ficus OpenCV bindings
  * Most GSoC projects should be on track; need to double-check it before the final evaluations. 

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-08-06

### *__Minutes__*

* Alexander Panov joined the team
* GSoC:
   * August 23 18:00 UTC: Deadline for Students to submit their Final Evaluation
   * August 30 18:00 UTC: Deadline for submission of Mentor's Final Evaluation of their 
* Opencv_zoo
   * Private for initial configuration
   * storage for models
   * Opencv_zoo: AR Vadim: Enable 2FA for GitHub account
* Python: unable to pass 3D matrix to C++ code [#19091](https://github.com/opencv/opencv/issues/19091) - revise from 2021-07-09
   * working on several PR, including better diagnostics in TF importer
   * [#20480](https://github.com/opencv/opencv/pull/20480) - breaking change. 
   * Workaround with fake dimension should be tested.
   * Vadim is needed for the discussion.
* Hardware acceleration in pre-built FFmpeg for Windows [(OpenCV-Python #520)](https://github.com/opencv/opencv-python/issues/520)
* Hardware acceleration is disabled by default. Need extra options to enable it. AI Alexander Smorkalov to point to C++ example how to enable it and find Python bindings for it.
* Automatically write RTSP streams to file during VideoCapture Decode with FFmpeg [#20444](https://github.com/opencv/opencv/pull/20444) -- AI to Alexander Alekhin to comment the PR and close.
* Split private.hpp for faster compilation [#20277](https://github.com/opencv/opencv/pull/20277) -- close. Does not improve build speed significantly.
* Fix Matcher Confidence Handling [#19955](https://github.com/opencv/opencv/pull/19955) -- need to make the threshold as parameter and discuss default value. AI to Alexander Alekhin to comment the PR.
* Add Quicklook for Mat on iOS and macOS [#20457](https://github.com/opencv/opencv/pull/20457)
   * AA: move code from imgcodecs to objc/core and merge
* (Draft) fix ONNXImporter diagnostic mode layer registration issue: [#20494](https://github.com/opencv/opencv/pull/20494)
   * Egor will try to hide implementation details, including layers registry pointer, mutex, etc.

 

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-07-21

### *__Minutes__*

* One of OpenCV Debian package maintainers joined in (Jochen Sprickerhof):
   * part of OpenCV is excluded because of possible licensing issues
   * PPA is one way to publish OpenCV packages, which is recommended, it's easier to do that for Ubuntu than for Debian
   * It would be nice to generate up-to-date usable pkg-config files for OpenCV during build
   * Maybe the version scheme in OpenCV needs to be revised to enforce binary compatibility between the patch releases
* Vadim:
   * GSoC: all the evaluations submitted; out of 12 projects 11 have passed mid-term evaluation.
   * GSoC student (Jebastin N) has added formal regression tests for the dynamically quantized networks and individual layers. Majority of the tests pass. After the tests are all green, the PR can be merged.
   * GSoC (DNN + RVV): convolution primitives are implemented now, the code is being tested.
   * Received Allwinner D1 dev boards with RISC-V + RVV 0.7.1, now the testing of RVV backend becomes more feasible.
* Shiqi:
   * No updates, Ricardo is on track with GSoC.
* Alexander:
   * workarounds in DNN module: 1. OpenCV did not support 1D mat, 2. the output must always to be FP32 (now solved).

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-07-16

### *__Minutes__*

* Maksim Shabunin will make announcement and OpenCV.org changes in the meantime.
* OpenCV 5.0
   * '3d' module depends on 'features2d'. That looks unusual for a common module. Will be discussed with Vadim next week.
   * Rositslav is working on 3d interface. He is on vacations this week.
* GSoC 2021
   * GSoC PR [#3006](https://github.com/opencv/opencv_contrib/pull/3006) contains LGPL code and will be rejected.
   * AI to all: add PRs and student evaluation status to GSoC tracking spreadsheet.
* PRs & Issues:
   * AArch64 semihosting: #20392 -- Alexander Alekhin will look at it next week.
   * Add read/write functions for features2d and normalize naming convention: #20367. Most of classes inherited from cv::Algorithm do not implement FileStorage operations. Decided that the PR is useful, but should be more conservative: do not change test parameters and xml/yaml.
   * Exception when destroyWindow is called on a non existing window: #20417. Alternative option - print warning.
   * Java: force using of 'Ptr<>' for OpenCV classes: #2034 - JFYI
   * Proposal: Drop Output and InputOutput arguments from Python bindings interfaces for OpenCV 5.x: #20418 -- will be discussed next time with Vadim Pisarevsky.
   * GTK vs VLFW for 3D -- need Vadim Pisarevsky for the discussion.
   * Message_lite.h support in DNN.
      * The option makes sense.
      * Need to re-generate C code from propobuf files with lite option. M.b. update protobuf.
      * Need do check compatibility with 3.4. Make sense to propose pr to master.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-07-14

### *__Minutes__*

* Vadim:
   * GSoC: many of the evaluations are not submitted yet. The reminder will be sent.
   * GSoC student (Jebastin N) has tested a few dynamically quantized object/face detection networks (FP32=>INT8) and the results are quite satisfactory. The performance is on par with the existing implementation, can be improved further. That is, more than 50% of the project is done already.
   * GSoC 3D samples project: discussed the results and plans with the mentors and the students. The results are quite good so far.
   * Together with Zihao M. started working on implementation of some missing ONNX layers (Less, Greater, NonMaxSupression), fixed a bug in Split/Slice layer. Briefly reviewed Stackblur patch from Zihao.
   * Reviewed dnn_face module from Yuantao F.; the functionality will be submitted into opencv/objdetect module.
   * Continue conversation with T-head team on the RVV optimization approaches.
   * Improved efficiency and the coverage of OpenCV Ficus bindings, still working on it.
* Shiqi:
   * GSoC student has implemented 3D point cloud & mesh visualization. In the next half of project he will add new functionality, better stability etc.
* Alexander:
   * RGBD => 3D PR has been reviewed by the core team; it's being polished now.
   * Public CI is improved, in particular, OpenCL builds.
   * Intern Maria joined OpenCV team, will be working on algorithms and visualization of audio/speech processing.
* Anna:
   * working on several PR, including better diagnostics in TF importer
   * there are some issues found when trying to import to DNN some new topologies that relate to the order of channels. The issues are being investigated.
   * working on the new releases of OpenCV-Python
   * "Group" layer in DNN is being implemented
   * 3D format import/export functionality is under review.
* Gary:
   * The GSoC project does not go all that smoothly.
   * Probably need to do some more paperwork about GSoC.
   * Talked to Kornia guys

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-07-07

### *__Minutes__*

* Vadim:
   * GSoC student (Jebastin N) continues work on OpenCV DNN 8-bit compute path. Most of the planned layers are finished. Submitted PR, which is now 'green'. Before it's merged, Jebastin is testing it now on some real object detection networks.
   * Another GSoC student, Zihao M., continues work on the loop closure algorithm (DNN-based), and also on stackblur, faster alternative to gaussian blur. The draft implementation of stackblur is ready, but it's currently a bit slower than GaussianBlur, at least on the moderate-size images & kernels.
   * Yuantao F. created draft version of DNN-based face detection module (will likely be transformed into a part of opencv_contrib/face module) and also started work on OpenCV model zoo. The face detection model, created by Shiqi Yu, is there already.
   * Investigating how to extend universal intrinsics to support variable-size vectors (which is important for RISC-V RVV and ARM's SVE2).
   * Still working on Ficus bindings for OpenCV; several functions have been manually wrapped. Plan to finish the basic version of the wrappers, including dnn + imgcodecs + highgui + videoio + parts of core & imgproc, by the end of this week.
* Shiqi:
   * GSoC student Ricardo finished the function to display pointcloud. Some features are to be added. PR will be submitted shortly.
* Alexander:
   * OpenCV community 4.5.3 has been released on Monday.
   * -openvino suffix was added to the binaries on Windows (with dldt support)
   * RGBD->3D PR is finally polished, and is ready for review.
   * the intern is working on improving Kinfu: colored version etc., GPU optimizations, documenting useful parts of the pipeline, e.g. ICP: https://docs.opencv.org/master/d7/dbe/kinfu_icp.html
   * GSoC: univ. intrinsics tutorial PR was submitted.
   * GSoC: speech recognition PR is submitted. C++ vs Python deviation was investigated, the fix is being prepared.
   * GSoC: implementation of fast bag of words for loop closure detection is in progress.
* Anna:
   * Done:
      * Andrey: Prepared the PR with building packages on Mac M1 for opencv-python repository.
      * Andrey: Prepared pull requests with changes of submodules for OpenCV Releases (4.5.3 and 3.4.15) in opencv-python repository.
   * In progress:
      * Egor: Shape + StridedSlice + Pack + Reshape is a pattern which gets simplified if there is no config file provided for the set.   But I did and hence got stuck. Reimplemented only ExpandDims using new layer parameters for Reshape, initial test suggests that everything is working.
      * Egor: Debugging net from this issue and fixing diagnostic tool along the way.
   * xperience.ai team is thinking of building a subset of OpenCV.
* Gary:
   * need to make another OpenCV board meeting.
   * some conversations with PyTorch team on possible collaboration.
   * PR with the implementation of deltile algo should be submitted soon.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-07-02

### *__Minutes__*
* The community release is being prepared. The tags will be set this weekend
* OpenCV 5 task list:
   * Rgbd to 3d patch is green and is ready for review
* GSoC-2021:
   * 8-bit DNN: [the patch](https://github.com/opencv/opencv/pull/20228) is now green. Vadim asked the student to try this approach (dynamic quantization) on some real object detection network and add the corresponding test.
   * 3d samples:
      * Patch with a new basic OpenGL functionality in core module
      * Draft version of point cloud visualization function
      * Implemented OBJ importer; the test is in progress
      * Nuget package: the scripts are in good shape. It’s suggested to integrate them into one of the build farms.
   * Speech recognition. PR is ready and submitted. Short audio samples do not work in Python.
   * Optimization tutorial: student is now working on parallel_for part. After that he will be working on universal intrinsics tutorial.
   * 3D: Zihao is implementing dnn-based loop closure detection. The other student is working on bag-of-words-based approach. PRs should be submitted by mid-term evaluation.
   * Annotated Python bindings: the project is on track. Need to submit PR by the mid-term evaluation.
* PRs & Issues
   * Scalar issue: need to be resolved by OpenCV 5. Alexander A to submit the issue to bug tracker.
   * Suggested to deprecate convertFp16() in 4.x and remove in 5.0.
   * [#19978](https://github.com/opencv/opencv/issues/19978) — Ok to close.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-30

### *__Minutes__*

* Vadim:
   * Zihao M. & Yuantao F. joined OpenCV China team. They will be working on deep learning-related topics, OpenCV model zoo in particular.
   * Still working on Ficus bindings for OpenCV
   * Started looking at various approaches to do accelerate convolution in OpenCV DNN
* Alexander:
   * OpenVINO 2021.2. OpenCV 4.5.3 for OpenCV was released. Now the community release is being prepared, including the pre-built binary package with DLDT (inference engine from Intel) included.
   * rgbd to 3d migration is in progress. Most of the remaining issues have been resolved.
* Anna:
   * Done:
      * Andrey: Created a PR with the suppression list for the Valgrind build on ARM in OpenCV repository.
      * Andrey: Changed the pipeline for the opencv-python repository on macos with M1. Fixed issues with python and dependencies on Mac Mini with M1.
      * Egor: TF Importer diagnostic mode PR merged 
   * In progress:
      * Andrey: Preparing a PR with all changes for opencv-python repository.
      * Egor: Fixed base64 encoding review remarks from alalek
      * Egor: Added ExpandDims layer in TF Importer; implemented Shape layer; added support for Const inputs in Pack. Found out that the    Reshape layer doesn't support runtime shapes and started to add const propagation. Import and inference of the net in issue is working now. Refactoring everything I implemented.
      * Julia: Working on issue: https://github.com/opencv/opencv/issues/19278 (first part: LSTM)
* Gary:
   * The GSoC student is working on Deltile. Grace is co-mentor of this project.
* Shiqi:
   * Baidu may help us to implement some missing layers in OpenCV to support more topologies.
   * GSoC student implemented draft version of point cloud visualization demo. Now the code need to polished.
* Vincent:
   * Submitted a few small patches to OpenCV, replacing "a = 0" with "a.setTo(0.)"
   * Continue working on resolving the remaining test failures
   * Suggested to consider Draco (https://github.com/google/draco) to load point cloud/meshes.
* Stefano:
   * This team packages OpenCV for Debian/Ubuntu: https://salsa.debian.org/science-team/opencv
* Satya:
   * Would be useful to have pre-built OpenCV packages for various platforms. Maybe it will be up to 10 different configurations.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-06-25

### *__Minutes__*
* Invited everyone to add the details to the ChangeLog. The release is expected at the beginning of July (1st week)
* OpenCV 5 task list:
   * Remove C API: Need to make a spreadsheet of modules that use C API and maybe distribute this task to several people, including xperience.ai team 
   * More detailed logging for users in DNN loader (TF part) — WIP; PR #20302 has been submitted.
   * Add support for quantized ONNX networks — suggested xperience.ai team to finalize and test more extensively the support for quantized ONNX nets.
* GSoC-2021:
   * 3D: one student is improving bag of words; the other one is trying deep nets, one layer is missing
   * Speech recognition: PR is submitted.
   * Vitaly’s project on the tutorial on univ. intrinsics: PR is expected soon.
   * 3D samples: the work is on track; one student will be preparing the first visualization demo based on the OpenGL callback; another one is working on OBJ importer
   * DNN 8-bit compute path: PR is mostly green; fighting with the remaining OpenCL test failures
   * Julia project is also on track;
   * Python bindings: the project is seemingly on track (need to check the report for more details)
* Opencv_zoo: Shiqi and Vadim are asked to add 2-factor authorization before Alexander A will make them admins. Otherwise, the agreement is achieved.
* PRs & Issues
   * CV_16F support in persistence: can be put even to OpenCV 4.5.3
   * Lapack support in Ubuntu (missing lapacke.h): it’s suggested to get rid of lapacke.h and add missing (Fortran-style) declarations where needed.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-23

### *__Minutes__*

* Vadim:
   * Had an online talk at RISC-V conf. about OpenCV and its progress in RISC-V optimization
   * Ported OpenCV header parser from Python to Ficus
* Alexander:
   * The team is preparing release 4.5.3; stub ChangeLog is created.
   * win32 backend of highgui has been finished.
   * All GSoC projects, mentored by Intel mentors go well; asked them to submit PRs before the evaluation
   * Rostislav is working on porting kinfu-related parts to opencv:next, 3d module; some bingings have been disabled.
* Anna:
   * Working on several PRs; highgui related PRs have been merged.
   * Made some fixes in Aruco board detector.
   * valgrid for ARM is now run; no issues is found
   * OpenCV Python for macOS ARM (M1) was built and tested;
   * Working on several PRs related to TF importer and OpenCV DNN in general.
* Shiqi:
   * Discussed progress with GSoC student on 3D samples; several options have been considered. Next week some first results are expected.
   * Model for face recognition will probably be contributed soon. Discussed it with one prof. in China.
* Gary:
   * Gave a talk yesterday at TTI event with follow-up discussion. The issue was raised that when some big datasets are used to train models, there will be often possible legal risks.
* Vincent:
   * Going through failing tests.
   * Round() behaviour changed from OpenCV 2.2 to OpenCV 4.x.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-18

### *__Minutes__*
* 4.5.3 & 3.4.15 will be released. No major patches in master will be merged till then. ChangeLog draft will be put to the wiki soon.
* Migration master=>4.x and next=>5.x or a half of it will happen after release.
* OpenCV 5 task list: no major progress
   * 3D module — some bindings are not compiling properly. 
   * Detailed diagnostics when loading TF models — WIP; PR is to be submitted.
   * ONNX model loader was extended to support quantized models — PR is submitted; need to address some issues
* GSoC 
   * 3D projects: 1 students is improving bag of words code. The other student is experimenting with networks to detect loop closure (there are some successful experiments to run those networks using OpenCV DNN).
   * Speech recognition — for now reading audio data using 3rd-party libs. After the PR with audio i/o is merged, this part will switch to OpenCV calls. OpenCV DNN already supports the models that are planned to use for speech recognition.
   * Vitaly has started working with students, no detailed updates so far (Vitaly is on vacation this week).
   * 3D samples projects: the students have started the work, designing API.
   * 8-bit DNN compute paths: PR is submitted, the student is trying to resolve the test failures
   * RISC-V: the work has just started
   * Type annotations for Python bindings: the work has just started.
* PRs & Issues
   * [#20219](https://github.com/opencv/opencv/pull/20219) — need to suggest the name of overloaded functions; suggest the mode to optimize extrinsics
   * [#20232](https://github.com/opencv/opencv/pull/20232) — merge into 3.4 as-is. In 5.x (next) replace the existing drawMatches with the new version.
   * GLFW patch:
      * General question about architecture.
      * Compatibility with the highgui backend architecture?
      * Need to polish CMake scripts (detection of GLFW etc.)
      * Could be useful to have common cross-platform visualization for Kinfu-like algorithms


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-16

### *__Minutes__*

* Vadim:
   * Finished and submitted PR to load quantized ONNX nets. Will probably be merged this week.
   * GSoC student Jebastin is working on adding 8-bit compute path to DNN. PR has been submitted (that includes 8-bit versions of popular layer + dynamic quantization), most of the tests pass.
   * Finished and submitted PR that adds GLFW support to highgui for the 2 GSoC projects on 3D visualization & samples. Will be merged this week.
   * News from Julia bindings project: there is good progress on the modern-style bindings for Julia, Linux version is working, adding support for Windows and macOS.
   * News from nuget package project: the student is preparing PR, after integration of which it would be nice to add automatic nuget package creation into OpenCV CI.
   * Started working on OpenCV bindings for Ficus. The OpenCV header parser is being converted from Python to Ficus (50% ready).
* Anna:
   * Done:
      * Andrey: Changed the Valgrind build. At this moment, tests run using the script and Valgrind plugin in Jenkins only parse reports. The PR with changes was created in the private repository (opencv-cn-pipelines).
      * Egor: Refactoring of TF importer is merged
      * Egor: findCirclesGrid() finding duplicates isn't reproducible anymore
   * In progress:
      * Andrey: Creating the pipeline for the opencv-python on macos with M1 
      * Andrey: Collected functions for Valgrind build and run few pipelines because errors (not memory  leaks) still happen, but there are only a few of them. Waiting for the results 
      * Egor: GTK wrong modifier keys being triggered fix in review; 
      * Egor: Investigated the dependency of cv2::destroyAllWindows() on libgtk2.0-dev and couldn't reproduce the issue; 
      * Egor: Proposed a PR with a fix to ids field of aruco board not being accessible from python + test
      * Egor: Tried to reproduce the leak of gaussian blur but couldn't figure out how to compile opencv with Intel's Gaussian blur optimization in 3.4.10. Latest 3.4 has -DOPENCV_IPP_GAUSSIAN_BLUR=ON which is not available on 3.4.10, so I asked the author of the issue for build flags; 
      * Egor: Link of cv::pollKey was caused by the wrong order of preprocessor directives.
* Gary:
   * deltile detector is going to be implemented during GSoC
   * OpenCV conference??
* Alexander:
   * The team is working on 4.5.3. Alex is working on merging the PRs
   * tracking API: one structure was fixed.
   * ffmpeg wrapper for Windows was updated.
   * win32 backend implementation in highgui is in progress.
   * All GSoC projects mentored by Intel team are going well.
* Shiqi:
   * Had the first meeting with GSoC student. He setup the developing environment and is working on the function API. Everything is smooth.
   * Found a student who will port the face detector to OpenCV. The model will be converted to ONNX
* Vincent:
   * Still working on migration to OpenCV 4.x
   * Found overflow in cv::norm, has submitted PR with the fix

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-06-11

### *__Minutes__*
* OpenCV 5.0
   * Odometry patch is almost ready; trying to resolve problem with Objective C bindings; maybe just exclude Linemod from the main repository for now (retain it in opencv_contrib)
   * Octree has been merged
   * ONNX quantized network support is almost ready
* GSoC 
   * Vadim’s student has prepared the first PR with partial 8-bit inference support (for now, just dynamic quantization can be applied to FP32 networks)
   * Rostislav’s students started working on loop closure algorithms; in particular, one of them will be repairing/improving bag-of-words functionality
* PRs & Issues
   * [##20190](https://github.com/opencv/opencv/pull/20190) suggested to create Layer factory each time a network is loaded from a file. It will eliminate any possible issues with singleton initialization 
   * There are two suspicious places in DNN: https://pastebin.com/KXRq7fzG .
      * In 3.x we decided to retain it as-is, since OpenCV 3.x will soon switch to low-profile maintenance mode.
      * In OpenCV 4.x, 5.0 C++11 (or newer) is used; the implementation will be checked and, if needed, we will get rid of double-checked-lock-pattern.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-09

### *__Minutes__*

* Vadim:
   * Prepared and merged PR that removes the old C-API based code from 3d and calib modules. Plan to eventually (by 5.0) remove C API from all the modules in the main repository `opencv`. Octree PR is finally merged into the `next` branch.
   * Started working on adding support for quantized nets to ONNX importer, should finish this week; the student has submitted draft PR with support of int8 compute path in DNN.
* Alexander:
   * The core team is working on preparing 4.5.3. The version has been bumped to 4.5.3-pre.
   * Working on Klockwork issues.
   * Alexander A is working on win32 backend of highgui.
   * Documentation on videoio & highgui plugins has been updated.
   * libjpeg-turbo was upgraded.
   * Rostislav continues working on 3d module; now he is fixing Python etc. bindings and other issues found by buildbot.
* Shiqi:
   * GSoC student will start work from the next week because of the final exams. 
   * Yuantao is working to build the model zoo using Github LFS.
   * The current hardware for the OpenCV benchmark prototype contains: x86 computer (i7 CPU + 1080Ti GPU), RaspberryPi

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-06-04

### *__Minutes__*
* Next week -- feature freeze for 4.5.3 and 3.4.15. Release is targeted to the beginning of July.
* There is a lot of old/dead code in Highgui found during plugin development. Alexander Alekhin will provide details, when “pluginization” has been finished.
* OpenCV 5.0
   * Old C interface is removed from calib and 3d. Vadim will file PR soon.
   * The next step: photo and other topic modules.
   * The last step: imgproc and core.
   * Proposal to organize old C interface as module in Contrib was rejected.
   * Quantized ONNX support is proposed for 5.0. Discussion [#20188](https://github.com/opencv/opencv/issues/20188). Baseline -- support the same layers and quantization type as in ONNX Runtime.
* GSoC is on track. Some students started earlier to make a pause for exams and thesis.
* PRs & Issues
   * [#20190](https://github.com/opencv/opencv/pull/20190) DNN TF importer 
   * NEON SIFT optimization [#20204](https://github.com/opencv/opencv/pull/20204) -- Vadim will comment. Pure NEON is not acceptable. Vadim will comment.
   * Add Octree to 3D module [#19684](https://github.com/opencv/opencv/pull/19684). Some internal methods are exported as public API. Vadim will work with PR author directly.
   * Samples and tutorials for the Dnn High Level API [#15240](https://github.com/opencv/opencv/pull/15240) - Close. Alexander will do and add references.
   * android image-manipulations sample improvement [#20041](https://github.com/opencv/opencv/pull/20041) - Alexander will check with latest SDK & NDK and provide update.



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-06-02

### *__Minutes__*

* Gary:
   * 
* Vadim:
   * Suggest to postpone OpenCV 5.0 till September (need more time + GSoC 2021 will be included)
   * Ficus 1.0 alpha is postponed till OpenCV bindings are ready (need ~2 weeks of work)
   * Made preliminary plan for the 2 GSoC projects about 3D samples & discussed it
   * 2 meetings on GSoC DNN quantization project. The student has suggested to implement 2 ONNX layers to support quantized networks.
   * Reviewing/working on several PRs
   * In progress: major refactoring of a part of 3D module and the calibration modules; getting rid of C API completely.
* Anna:
   * Done:
      * Andrey: Fixed the build in OpenCV-Python using Github Actions for "master" branch on windows.
      * Egor: fixed HOG copying #20131, added cuda and vulkan backend options to dnn samples #20175
   * In progress:
      * Andrey: Changing the Valgrind build in OpenCV CN CI.
      * Egor: Porting base64 encoding from 3.4 #20143 and TF importer diagnostic mode. OnMouse rounding fix #20149 and splitting up layer dispatch of Tensorflow importer #20190 are in the process of review. 
* Alexander:
   * OpenCV 4.5.3 is being prepared.
   * Maksim is working on Protex & Klockwork issues
   * Alexander A is working on reparing test failures on Windows
   * Rostislav is working on refactoring odometry to be compatible with FastICP; he met with his GSoC students.
* Shiqi:
   * From OpenCV 5.0 we need to remove some old parts (move them to contrib or remove completely): old face detector, old face recognition, old people detection.
* Vincent:
   * cv::resize() & cv::cvtColor() - would be nice to have bit-exact version.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-05-28

### *__Minutes__*
* OpenCV 5.0
   * Egor Smirnov starts work on debug option for TensorFlow loader
* GSoC 2021
   * All mentors and students are in contact
   * Blog posts for GSoC projects are very appreciated, but not required for successful evaluation
   * 3d point cloud loaders are included into GSoC scope.
* PRs & Issues
   * [Neon-optimized RGB2Lab](https://github.com/opencv/opencv/pull/19883) -- merged
   * [#19842](https://github.com/opencv/opencv/pull/19842) Need to add “normalization” to user code. Move boxes to (0,0) and then calculate intersection. Proposal: close the pr and propose alternative solution.
   * [#19684](https://github.com/opencv/opencv/pull/19684) -- all review issues have been fixed. Could be merged
   * [#19995](https://github.com/opencv/opencv/pull/19995) (Qt 6 support: tested, works well. Currently, there are merge conflicts — shall we finalize this and similar patches by ourselves?) -- fixes required. Alexander Alekhin will provide feedback.
   * [19592](https://github.com/opencv/opencv/pull/19592) (Set C++ 14 standard by default in the next branch; sooner or later we will need to do it. What to do with the patch?) -- to be closed. Alexander Alekhin will provide an alternative solution. Major concern is CentOS support (GCC 4.8.x).
   * [#19555](https://github.com/opencv/opencv/pull/19555) -- Need to fix generator and some scripts.



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-05-26

## __*Agenda*__
* 

### *__Minutes__*
* GSoC
   * Spreadsheet for projects and mentors https://docs.google.com/spreadsheets/d/194ZvbcOvGrWo3ctGKdnYW9NoCRKB6T5Udq8N_pKJ5tw/edit#gid=1036775246
* OpenCV python branch 3.4 on Ubuntu and Mac waterfall Github actions fixed all the tests
* Fixing build for master for Windows python
* Igor started processing base 64 pull requests
* Mishcans contributors for Kornia on Ransac
* OpenCV 5 waiting on release date
* Vincent works internally on revving OpenCV version
* Shiqi not much activity
* Alexander finished UI backend feature GTK, Win32 API is done in Master
* Face detection on Android on ARM plug in for OpenVino
* Release activities issues being resolved
* 3D module being worked on
   * Fixing odometry interface to support UMat, removing Ceres dependency
* Vadim Work on OpenCV 2-3 pull requests
   * Looking at 7 more pull requests
   * GSoC 
      * 3 meetings for GSoC projects
      * Python bindings Tuesday
          * Propose extra ideas
   * Pull request for Risk-V optimizations 
   * Universal intrinics extensions (low performance w/narrow registers, high performance w/wide registers)
      * 1.0 vector extensions or Risk-V 
      * Similar to ARM V-9 extensions
* Thinking about implementing Deltille grids as a fiducial for OpenCV https://openaccess.thecvf.com/content_ICCV_2017/papers/Ha_Deltille_Grids_for_ICCV_2017_paper.pdf
* Future thought on supporting event based or "neuromorphic" cameras (example: https://www.prophesee.ai/ )
   * https://www.youtube.com/watch?v=MjX3z-6n3iA&ab_channel=PROPHESEEMetavisionForMachines


### *__To Dos__*
* Name
  - [ ] todo


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-05-21

### *__Minutes__*
* G-API Python API PR has been merged. Part of Python bindings for G-API are in Python and Python package is directory with py files and .so. AI to Alexander Smorkalov: update pypi build scripts to accommodate.
* Since Python 3.8 Windows version ignores environment variable PATH. Self-built OpenCV-Python cannot load CUDA, VTK, other 3rd party libraries. Some general solution for 3rd party libraries is required: [#20050](https://github.com/opencv/opencv/pull/20050), [#16120](https://github.com/opencv/opencv/pull/16120).
* Python API static types should be targeted to master by default but could be rebased to next if dramatic changes in API are required.
* PR & Issues
   * sqrt is missing in magSpectrums() called in phaseCorrelate(): [#20100](https://github.com/opencv/opencv/issues/20100) - AI Vadim to review and comment.
   * Fundamental matrix code is fragile and thoughts for improvement [#20109](https://github.com/opencv/opencv/issues/20109) - Waiting for author response.
   * Highgui backends & plugins [#20116](https://github.com/opencv/opencv/pull/20116)


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-05-19

### *__Minutes__*

* Gary:
   * Filed all the necessary forms for GSoC (payment info etc.)
   * Separating accounts because Carla is now in a different foundation, not OSVF.
   * Big plans on expanding OpenCV foundation (robotics area is of special interest)
   * In order to increase OpenCV team, need to go to the upper level.
* Vadim:
   * The GSoC projects have been announced. Contacted a few students. Other mentors are welcome to do it as well.
   * Built and tested OpenCV on RISC-V 0.7.1 (simulator). All the core tests pass successfully. Need to acquire some real RISC-V hardware.
   * xperience.ai guys tried to use ARM server from China CI for OpenCV Python — unsuccessfully, the connection to github is very unstable.
   * The work on Ficus 1.0 alpha is finished. But maybe postpone it a bit, create bindings for OpenCV first.
* Anna:
   * Need to buy a new ARM board to test OpenCV Python on ARM Linux.
   * Got another developer into OpenCV team, Igor. He is now working on fixing issues in some pending pull requests.
   * Andrey: Split workflow according to platforms in Github Actions.
   * Alexander: Updated OpenCV-Python readme and documentation pages after migration to OpenCV organization on Github
   * Alexander: Helped to resolve issues in OpenCV-Python repo ## 486, 472, 465, 457, 455
   * Alexander: Debugged several OpenCV-Python test issues with Andrey
   In progress:
     * Andrey: Fixing running tests in Github Actions for “3.4” branch on ubuntu and macos.
* Alexander:
   * Hardware acceleration pull request was merged last week. Now the data stays on GPU without being copied to CPU (https://github.com/opencv/opencv/pull/19755)
   * Alexander is working on GTK+ backend.
   * Rostislav will mentor another 3D (loop closure project) out of GSoC.
* Shiqi:
   * Contacted GSoC student on the 3D samples project. Suggested to sync efforts, because we will have 2 projects on the same topic.
   * Yuantao is defending Master thesis this week, after that he will have more time and probably add more hardware to CI, including RISC-V.
* Vincent:
   * can co-mentor the project on improving Python bindings via type annotations.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-05-14

### *__Minutes__*
*   4.5.3:
   * "-pre" versions on June 07
   * Release 4.5.3 is targeted for the end of June, beginning of July.
   * Python code added to Python module crashes python 3.9 on finalization.
*  GSoC 2021:
   * Waiting for May 18 for official students distribution between projects. May start working with students.
   * Official development starts June 8th.
   * The first evaluation July 13th.
   * Final evaluation August 24th.
*  Opencv-python-plus: SuperAnnotate:
   * Agreed to allow pip package naming with opencv like “opencv-superannotate”
   * Agreed to create repo in OpenCV organization on Github.
   * AI to Alexander Smorkalov: prepare a document with collaboration process and agree with Superannotate team on LFS usage, Github Actions usage, access administration, etc.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-05-12

### *__Minutes__*

* Gary:
   * need to clarify the scope on fiducial tags detection project.
* Vadim:
   * the slots are allocated, waiting for May 18th for the official announcement.
   * finished work on Ficus tutorial; now making some final touches before alpha can be announced.
   * work on improving RISC-V RVV support and probably adding ARM v9's SVE2 should begin soon.
* Alexander:
   * Alexander A is back from vacation. He started working on UI backends (similar to video I/O backends that he did before)
   * Anna integrated DaSIAM into the tracking API, developed by AA.   
* Shiqi:
   * Model Zoo: would be useful to have. Maybe use github-lfs for it.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-05-07

### *__Minutes__*
*  GSoC 2021: 12 slots are available. 
   * Distribution is done in the spreadsheet.
   * AI to mentors: make a technical interview with candidates, if required.
*  ARM wants to contribute SVE2 support to OpenCV. The solution is under discussion.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-05-05

### *__Minutes__*

* Gary:
   * contract between ocv.org and ocv.org.cn need to be finalized and will hopefully be finalized soon.
* Vadim:
   * the min/max number of GSoC slots are requested, waiting while the request is processed.
   * several related to each other RISC-V RVV/SVE2 activities are going on.
* Anna:
   * OpenCV Python release was updated. Announcement is expected next week.
   * Issue with Java bindings on ARM (OpenCV China CI) is being investigated now.
   * Github actions will be used to test OpenCV Python on ARM.
   * Alexander: reviewed CI code for OpenCV-Python release 4.5.2 and 3.4.12. Tested ARM package manually.
   * Alexander: reviewed OpenCV-Python related tickets, solved to resolve issues.
   * Andrey: Created the Github Actions pipeline for building opencv-python packages on ARM.
   * Andrey: Changing running tests in Github Actions for all platforms.
   * Andrey: Fixing an issue with java tests on the ARM machine in OpenCV CN CI.
* Alexander:
   * OpenCV Intel team members reviewed GSoC proposals.
   * Alexander A is reviewing H/W acceleration of Video I/O (TLS cleanup issue on Windows is resolved).
   * Rostislav created PR that brings elements of video homography/kinfu to 3d module.
   * Artem (intern @ intel) made some improvements in kinfu pipeline (colored kinfu flavor).
* Shiqi:
   * Evaluated several GSoC proposals.
   * Finalized face detection algorithm. face detection: data file in txt 595KB, number of parameters: 85K. Suggested to make it a separate download at CMake configure stage.
* Vincent:
   * good progress on transitioning to OpenCV 4.x.
* Stefano:
   * ready to be co-mentor for some GSoC projects.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-30

### *__Minutes__*
*  4.5.2: opencv-python updates
   * OpenCV-Python package for popular platforms is planned to be ready today
   * OpenCV-Python for ARM Linux will be built with OpenCV CN infrastructure.
*  GSoC 2021:
   * AI to all: review proposals
*  PRs & Issues:
   * G-API team reworks Python package to include Python code tool. The feature will be in the next OpenCV 4.x release.
   * Different inliers convention with solvePnPRansac and USAC option: [#20008](https://github.com/opencv/opencv/issues/20008) - Vadim is looking on it (there can be problem with Python bindings)
   * Added PaddlePaddle classification model conversion case: [#19976](https://github.com/opencv/opencv/pull/19976) The PR could be merged. The next steps:
      * Need to split TF, PyTorch and PadlePadle cases.
      * Need to rework `common` folder.
   * Inconsistency in Mat::release behavior can lead to different outcomes under Debug and Release modes elsewhere: [#20000](https://github.com/opencv/opencv/issues/20000)
      * For 5.0. Debug and Release builds should do the same.
      * Vadim will take a look at it.
   * Adding functions rbegin() and rend() functions to matrix class: [#19967](https://github.com/opencv/opencv/pull/19967)
      * Test required
   * "Baremetal" patches



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-28

### *__Minutes__*

* Gary:
   * There is "tax season" in US now.
   * Calibration toolbox for OpenCV
* Vadim:
   * Gave talk on OpenCV 5 at Orbbec's organized school for students at Shenzhen University
   * Reviewed all the GSoC proposals; it looks like we have at least 8-9 good proposals.
   * Final touches to the Ficus compiler before alpha release; adding some useful functionality to the standard library
* Alexander:
   * Initial support for OneVPL (video processing library: https://github.com/oneapi-src/oneVPL) is added to OpenCV
   * Video stabilization was requested by OpenVINO team; OpenCV team proposed the solution based on opencv_contrib's videostab module
* Shiqi:
   * One of the students is now maintaining OpenCV CI China.
   * The network is now quite smooth.
* Vincent:
   * Upgrading projects to OpenCV 4.x goes on successfully.
   * Everybody whose software is used for Mars Helicopter Mission 2020 gets a badge on github.
* Stefano:
   * https://www.khronos.org/blog/an-introduction-to-vulkan-video. Cross-platform API for hardware-accelerated video encoding/decoding

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-23

### *__Minutes__*
*  KinFu patents issue:
   * Base algos not covered by patent are moving to core repo.
   * Pipeline and patented parts stay in contrib.
*  GSoC 2021:
   * All mentors should vote for candidates till May 4 and request minimal and maximal amount of slots from Google.
   * AI to all: submit votes to the spreadsheet
*  PRs & Issues:
   * [baremetal][aarch64] Build a baremetal OpenCV for AArch64 #19921. Extract CMake option to build OpenCV without threading framework:
      * Mutexes, TLS, etc are just stubs. cv::parallel_for just calls the functor.
      * The option could be tested with CI.
      * Add toolchain file and extra options on top of the first one with minimal changes in code.
   * Significantly reduced OpenCV binary size by disabling IPP in some funcs #13085
      * Alexander Alekhin will add CMake flag to manage IPP behavior externally.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-21

### *__Minutes__*

* Gary:
   * Gave keynote speech on OpenCV at "China Machine Learning Summit 2021" (via Zoom): http://ml-summit.org/; http://conference.boolan.com/Fs8oYp5wbKW6teSGD_YnDR8OWZgX. 600-800 participants.
   * Looking at fiducial tags solution by FB. Claimed to be much more accurate for calibration.
   * Working with Ethan R, who has created very advanced camera calibration framework (using Ceres internally). In addition to this framework there is sophisticated web infrastructure.
* Anna:
   * Julia B has joined OpenCV team. She will be working on OBJ & PLY importers for 3D module.
   * Looking for another OpenCV team member (may take ~1 month).
   * 2 GSoC 2020 students agreed to write a blog post.
   * OpenCV Python package goes through the final testing. Will be released quite soon. The versioning matches OpenCV version numbers.
* Vadim:
   * GSoC proposals: composed spreadsheet, sent the link and request for review to the mentors.
   * ficus compiler: incremental compilation mode is in progress. Should make the compiler much more convenient for big-scale projects.
* Alexander:
   * Alexander A is reviewing H/W acceleration PR for video I/O. He also merged 1D barcode PR.
   * Ubuntu 16.04 upgraded to 20.04 in CI.
   * PR on rgbd port to next branch, 3D module, will be submitted this week.
* Shiqi:
   * May hire one of the students to do part-time work for OpenCV (e.g. maintain CI system).
   * Maybe launch OpenCV hardware evaluation program: run certain set deep learning topologies on a variety of hardware and produce some numbers.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-16

### *__Minutes__*
*  Opencv-python -- plan to finish packages preparation on Monday-Tuesday and push release to Pypi
*  GSoC 2021:
   * Vadim is reviewing proposals and will create the summary spreadsheet with proposals this weekend. AI to all: review applications and provide feedback.
   * On May 4th we should ask Google for a certain number of slots (min-max).
   * RISC-V DNN optimization will be done inplace. There is an option to extract optimizations as “dnn_hal”. It could be done later, as refactoring. AVX512 optimizations are done inplace and dispatched in run-time.
   * 1D Barcode support: [#2757](https://github.com/opencv/opencv_contrib/pull/2757) -  in progress. Alexander Alekhin will fix minor issues by himself and merge the patch.
  * ML: "format" bug in exported models (e.g, "text" module)
      * Deprecate old part of “text” module in contrib
      * OpenCV 3.0..OpenCV 3.2 did not add field “format” that is used to determine xml file version: 2.4x-style and 3.x+ style. Alexander Alekhin added check to code to print warning. Also Alexander Alekhinfixed issues with old code for text detection in contrib.
  * cv::UMat output/input in VideoCapture/VideoWriter (data stays in GPU memory): [#19755](https://github.com/opencv/opencv/pull/19755) 
      * Works on Windows and Linux (properly configured environment is required).
      * It is not supported by plugins in videoio yet (TBD).
      * There is issue with multi-gpu configuration Intel + NVIDIA on laptops.
      * The feature is disabled by default.



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-04-14

### *__Minutes__*

* Gary:
   * Need to review the proposals.
* Anna:
   * Had meeting with SA. Probably will have some additional Python module that will be compatible with OpenCV Python. It will provide cloud-based training solution (very high-level, user-friendly API).
   * OpenCV China CI project is complete.
   * Continue working on OpenCV 5.
* Vadim:
   * GSoC application period is over, 61 proposals submitted (~40% less than in 2020). We need to select the projects by May 18th, but request the slots on May 4th.
   * the latest touches to the ficus compiler, the last big feature before release is added (efficient vector data type based on RRB trees).
   * starting working on the tutorial
* Alexander:
   * Alexander A: 400+ PRs are being ported from OpenCV 4.x to OpenCV 5.x.
   * OpenVINO-based ARM CPU plugin - instructions on how to use it are published at opencv.org: https://opencv.org/how-to-run-yolov4-using-openvino-and-opencv-on-arm/
   * Colored KinFu algorithm has been merged to OpenCV 4.x
   * Rostislav continues to work on porting RGBD parts to OpenCV 5.x
   * Dosya RPM demos (object tracking) are refined.
* Vladimir:
   * DPC++ backend (async calls) (G-API?)
   * MediaSDK is to be replaced with OneVPL (video processing library): similar API, different name.
* Shiqi:
   * OpenCV China CI: working with admins to provide more stable connection
   * Continue working on face detector. Reduced 88K (face + 5 landmarks).
* Vincent:
   * All the code has been ported to C++ (OpenCV 4.x).
   * Started working on a small compatibility library.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>


## 2021-04-09

### *__Minutes__*
*  Release:
   * Opencv-python. Packages build is on track. All available configurations are migrated to Github Actions.
   * Xperience AI team tests packages now.
   * Grirgory will send notification when packages are available.
*  5.0 Tasks:
   * New text rendering affects videoio tests (frames with text are used). A lot of tests fails with low PSNR. Alexander Alekhin looks how to fix the issue with minimal test data changes
   * RGBD work from Rostislav is merged to contrib and should be forwarded to OpenCV next.
   * No progress with Python for now.
   * Python packages renaming:
      * Need to check import priorities: pure binary, archive, folder with pys
      * Need to check Pypi rules about it.
   * Probably need to rename opencv2/*.hpp to opencv/*.hpp. At once, contrib’s headers should be renamed to opencv_contrib/*.hpp.


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-07

### *__Minutes__*

* Gary:
   * we are now in the application period
* Anna:
   * cut down team for various reasons:
      * OpenCV Python support (Windows version is being prepared, Mac is in progress)
      * The goal is to have complete OpenCV Python by OpenCV 5
      * Andrey is working on CI (polishing the remaining parts; fixing problems with ccache, found several tests that failed on RISC-V, edited instructions on how to add the new pipeline)
* Vadim:
   * ficus compiler is almost complete: all major features have been implemented. Now polishing the code, fixing bugs and writing the tutorial
* Alexander:
   * OpenCV 4.5.2, 3.4.14 have been finally released, the announcement was published.
   * Pose graph w/o Ceres dependency was merged to opencv_contrib; now should be ported to 3d module

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-04-02

### *__Minutes__*
*  Release:
   * Release tag ETA 12:00 UTC. Release binaries ETA - EOW.
   * Python release will be done next week. ETA: next Friday.
   * Final reminder: changelog on Wiki

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-31

### *__Minutes__*
* Vincent:
   * all the internal projects build successfully with the latest OpenCV. Now the task is to make the unit tests pass
   * heads up: ARM v9 was released.
* Gary:
   * Need to find mentors for GSoC projects and not only, a few more students have contacted us to do summer internship beyond GSoC.
* Anna:
   * ONNX diagnostic tool is finally integrated into OpenCV. Provides detailed diagnostic about the network.
   * Published announcement about GSoC 2021
   * Working with OpenCV China, polishing remaining bits
   * Discussing extensions to OpenCV python regarding training deep nets in a cloud
* Shiqi:
   * Working on optimizing the new face detector for AVX2 (8-bit compute path)
* Vadim:
   * still working on ficus, slowly switching back to opencv
   * added Ningxin Hu's idea on OpenCV.js DNN acceleration using WebNN
* Alexander:
   * OpenCV 4.5.2, 3.4.14 will be released within 1-2 days (April 1st-2nd).
   * Announcement about Intel Inference Engine ARM support was published at opencv.org: https://opencv.org/deep-learning-inference-in-openvino-on-arm/
   * opencv_contrib new functionality:
      * Edge drawing (edge & circle detection) was added
      * 1D barcode support
      * Python bindings for viz module
   * wide universal intrinsics documentation was added to docs.opencv.org.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-26

### *__Minutes__*
*  GSoC 2021:
   * Alexander Smorkalov will post blog on habr.com
   * Lydia will ask the remaining GSoC 2020 authors about blog post

*  PR & Issues:
   * Contrib - merge
   * Python bindings: Alexander Alekhin will file bug on Github. Alexander Smorkalov will involve Vadim Levin to resolve the issue.
   * Add reading of specific images from multipage tiff [#19780](https://github.com/opencv/opencv/pull/19780) - Commented in PR.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-24

### *__Minutes__*
* Vincent:
   * finished transition to the new OpenCV. A minor compile bug with Clang 13 (on VSX).
   * another interesting implementation of universal intrinsics: https://github.com/google/highway
   * draco, 3D compression library by Google: https://github.com/google/draco
* Gary:
   * we are in the middle of GSoC 2021 project discussion.
   * need to invite more mentors.
* Shiqi:
   * contacted to 2 students from GSoC: 3D visualization and universal intrinsics.
* Vadim:
   * Ficus compiler was rewritten in Ficus. Now it's being debugged. After it's done, a few more features will be added, tutorial is written and the standard library extended a bit. When Ficus 1.0 (alpha) can be released.
   * Now slowly getting back to work on OpenCV 5
* Alexander:
   * Luibov is communicating with potential candidates for GSoC project on speech recognition
   * Rostislav is talking about 3D projects
   * Vitaly Tuzov is talking about intrinsics' project
   * OpenVINO 2021.3 has been released
   * Updated OpenCV page to inform that ARM backend of OpenVINO backend is ready (CPU & Movidius plugins).
   * Working on OpenCV 4.5.2, cleaning up issues
   * Vitaly is updating documentation on wide univ. intrinsics.
   * Rostislav finished 3D pose graph code and is now trying to make it compile on various platforms.
* Anna:
   * on sick leave

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-19

### *__Minutes__*
*  1. OpenCV Wiki: Lydia Kravchenko will add old GSoC and meeting minutes pages to Archive, remove years on archive page
*  2. Legal Issues:
   * a. Proposal: add Ci check for “stop” words to search for “GPL”, “non-commercial”,  etc.
*  3. GSoC
   * a. GSoC 2020 mentors: ping students and check if students are ready to prepare a blog post
   * b. GSoC 2021: Lydia Kravchenko will prepare post announcement about GSoC 2021
   * c. Point cloud format parsers -- a topic for GSoC 2021

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-17

### *__Minutes__*
* Shiqi:
   * trained very efficient face detection model. 1/10 of the size of the previous model (from libfacedetect). Can probably embed it into OpenCV.
* Alexander:
   * release of OpenCV 4.5.2 is being prepared.
   * several changes to OpenCV DNN to be compatible with the latest Intel's IE.
   * Rostislav is rewrote internal optimization of visual odometry from Ceres to custom function.
   * Audio support PR is submitted (Windows part, Linux part to follow).
   * At least 3 people from Intel OpenCV team can be GSoC mentors.
* Vincent:
   * Suggested to use Clang TIDY: https://clang.llvm.org/extra/clang-tidy/checks/performance-unnecessary-value-param.html to enforce better coding style.
   * Migration to the new OpenCV in the internal projects is going on.
* Vadim:
   * working on ficus compiler. it's approaching the first alpha release

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-12

### *__Minutes__*
*  1. GSoC 2021 Google Group was created 
*  2. Master RISC-V: [#18394](https://github.com/opencv/opencv/pull/18394) -- Alternative universal intrinsics implementation for RISC-V with RVV 0.7 from THead for their hardware. Will be adjusted and merged later.
*  3. ONNX diagnostic tool: PR [#19693](https://github.com/opencv/opencv/pull/19693) 
   * a. Document changes in public API.
   * b. Check if we need std::map<String, int> in public API.
   * c. Reduce global variables. There is a global std::set in PR. “Wrap” with a function call to not initialize if DNN is not used.
*  4. Steps support in DNN Slice layer: PR [#19546](https://github.com/opencv/opencv/pull/19546)
  * a. Agreed that optimization could be done as the next step with another PR.
  * b. Need to implement proper fallback from OpenCL to CPU code.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>
## 2021-03-10

### *__Minutes__*
* Gary, Vadim:
  * We are accepted into GSoC 2021! Now need to add mentors and create GSoC google group.
  * A demo application for Android that reads camera and runs a deep learning net on it (+ some efforts to make it compact) + tutorial on how to make such app — a great GsoC idea.
  * on-cloud training, code sharing infrastructure (python etc.)
* Anna:
  * 2-3 people from xperience.ai could be mentors.
  * Anastasia: finalized/corrected ONNX diagnostic tool in accordance with provided issues from @sl-sergei ((1) onnx_graph_simplifier stage correction, (2) mixing of diagnostics and assertion/error logs), prepared MVP
  * Anastasia: finalized PR #19641 (added corrections in accordance with comments), backported PR #19546
  * Alexander: Finalized PRs #19619, 19675.
  * Alexander: Updated test suppression list in Jenkins CI, reported hardware accelerated video encoding failures on Windows with NVIDIA cards.
  * Alexander: Investigated ccache usage issue on Windows, no ready to use solution for now.
  * Andrey: Split tests on Windows for nightly pipelines in OpenCV CN CI. I am going to implement it into precommit pipelines.
  * Andrey: Added the "pylint" stage for nightly pipelines in OpenCV CN CI. I am going to implement it into precommit pipelines.
  * Andrey: Added warning handling for nightly pipelines in OpenCV CN CI. I am going to implement it into precommit pipelines.
* Shiqi:
  * continued work on the face detection model. Several models have been trained. Still not satisfied with the results, could further improve accuracy and maybe reduce the size (quantize the model)
  * several students are considered as OpenCV interns.
  * need to have a guide on how to build compact OpenCV-based apps for Android
* Alexander:
  * Alexander A has prepared the guide on how to use h/w accelerating video i/o in OpenCV; fixed a few bugs in the code
  * Linux machines in OpenCV CI are upgraded. More RAM is added.
  * Rostislav continues to work on porting functionality from contrib to 3D module; KinFu etc.
* Vincent:
  * less and less compile etc. issues when porting to the new API
  * grid adapter for SURF (trying to find more or less equal number of features in each tile) was removed but may be useful
  * sandbox API (already in GSoC ideas)


## 2021-03-05

### *__Minutes__*
* 1. Feature freeze happened. The official release is targeted at the end of the month.
* 2. OpenCV team will change the branching strategy for the 5.0 release. Rationale: major branches rename breaks a lot of links, including documentation. The goal is to create new major branches and not rename existing ones.
   * a. Master will be renamed to 4.x
   * b. Next will be renamed to 5.x
   * c. No master branch
   * d. Default branch - 5.x
   * e. 6.x will be created for the next major version.
* 3. Proposals for GSoC 2021 are partly approval 
* 4. Jenkins: Xperience AI switched to new networking solution. PRs statuses will be stabilized in a couple of days.
* 5. PRs & Issues:
   * a. Bayer issues: #19629 #18619 #4857
      * i. Deprecate current constants and create new one in 4.x and next
      * ii. AI to Vadim Pisarevsky to work on it.
   * b. Android Camera through NDK ( #19597 )
      * i. Requires minimal supported Android version upgrade.
      * ii. OpenCV team will continue to release OpenCV for Android SDK with conservative strategy with minimal Android version. Native Camera support will not be there. Advanced users can build OpenCV with higher API level and Camera support by their own.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-03-04

### *__Minutes__*
* Gary:
   * 11 GSoC ideas submitted. Maybe need more.
   * Contract is being prepared.
   * Individual membership? (patreon?)
* Vadim:
   * no major updates
* Anna:
   * Lydia: OpenCV.org site: articles on RISC-V optimization and image retrieval have been published.
   * Anastasia: finalized TF reshape appropriate support #19489 (PRs: #857, #19641)
   * Anastasia: corrected PRs in accordance with comments: #19546, #19477
   * Andrey: Fixed ccache on ubuntu-20.04-arm build.
   * Andrey: Added robust timeouts for stages in OpenCV CN CI. 
   * Andrey: Fixed a network problem with git commands in OpenCV CN C
   * Alexander:
      * Finished abandoned PRs #19539, #19668.
      * Scoped work for popular point cloud format support (OBJ, PLY, STL)
      * Reviewed, helped to resolve issues with #19554, #19566, #19619.
      * Helped Andrey with Pylint, build timeouts on CI
   * General activity: OpenCV 5 release is being prepared.
* Shiqi:
   * network configuration of CI system in China. Now it should be fine.
   * purchased mac mini with M1, can now test macOS and iOS.
   * negotiations with some big companies is going on.
* Alexander:
   * OpenCV 4.5.3;
   * hardware video decoding backend has been merged.
   * several image codecs have been upgraded (libtiff, libjpeg, etc.)
   * several video i/o issues & klocwork issues.
   * calib3d crash was fixed.
   * Rostislav is working on rgbd module port. Ceres-based parts are now rewritten in Eigen.
   * ARM target is being added to OpenCV based on Inference Engine backend.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-02-24

### *__Minutes__*
* Gary:
   * opencv.org.cn & opencv.org contract is in progress.
   * GSoC ideas list should be further expanded & more mentors should be added.
* Vadim:
   * Conversion of ficus compiler from ocaml to ficus is still in progress. Ocaml sources have been converted to Ficus.
   * Performance regression testing for OpenCV? Funding from opencv.org?
* Vincent:
   * Migration to OpenCV 4.x is still in progress; less and less problems with compiling OpenCV-based projects.
   * One of critical security issues has been fixed.
* Anna:
   * xperience.ai will concentrate on preparing OpenCV 5.0
   * Andrey: Integrated extended PR testing with OpenCV Contrib and OpenCV Extra into the main pipeline. Reproduced DNN testing locally.
   * Anastasia: finalized #17364 (PR: #849, #19477), completed #19366 analysis.
   * Alexander S: Reviewed Ci failures and test hangs. Tuned suppression lists, fixed yet another non-free handling issue (PR #19488).
   * Alexander S: Reviewed issues filed against OpenCV-Python repository. Tested and closed some bugs. Introduced the same milestones as in core OpenCV. Start looking into current CI setup for the repo and weak points.
   * Alexander S: Prepared slides for HSE course for Courcera. Work on home tasks for the course is in progress.
   * Alexander S: Reviewed, tested, helped to resolve issues with ##19126, 19448, 19439, 19309, 19392
   * Amir: tried to fullfill requirement of preserving compatibility in PR Subdiv2D, unsuccessfully. Hoped to use preprocessor macros  as a flexible approach to relay between new and old logic, but it was more difficult than expected.
* Shiqi:
   * worked on face detection for OpenCV. Trying to reduce the model size even further, make it even more efficient.
* Alexander V:
   * Dual quaternion patch has been merged.
   * GPU implementation of HashedSDF has been merged.
   * The team has started working on colored KinFu.
   * QR detector testing. The report has been sent to WeChat team.
   * Documentation on the universal intrinsics has been updated.
* Stefano:
   * working with TF team during the next months.
   * it may be interesting to support LambdaNetworks in OpenCV (can be a GSoC project): https://openreview.net/forum?id=xTJEN-ggl1b
   * ICLR 2021

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-02-19


### *__Minutes__*
* GSoC 2021:
   * Alexander Smorkalov and Julia Bareeva are ready to participate as mentors;
   * March 9th - decision from Google id OpenCV participates or not
   * April 13th - deadline for students submissions
   * May 17th - Google decision on the amount of participants
   * Ideas: Computational geometry in 3d.
   * Vladimir Dudnik: (https://github.com/YadiraF/PRNet could be a good choice for GSoC 2021) (GPL).



<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-02-17

### *__Minutes__*
* Gary:
   * Registered for GSoC 2021. Need more ideas.
   * Some observable progress on the fiducial tags projects. Now detects the tags robustly, including accurate 3D pose estimation.
   * The project on fiducial tags may be useful for some possible bigger projects.
   * Communicated with a guy with medical background who does research on making neural nets more "human-like".
* Vadim:
   * Conversion of ficus compiler from ocaml to ficus is in progress. The parser is 50% complete.
* Vincent:
   * no major updates
* Anna:
   * Anastasia, Alexander, Amir: working on a number of PRs and issues: #19366 (PR: #19546, #854), #19536, #19539, 19540
     ## 19498, 19543, 19532, 19515, 19503, 19499, 19525, 19392, 19392, 19532.
   * Lydia, Alexander: published announcement about OpenCV Python distro: https://opencv.org/opencv-python-is-now-an-official-opencv-project/
   * Andrey: created a pipeline to download DNN models and implemented the sync of them into current pipelines. Prepared changes for main pipelines to use extended DNN testing.
   * Andrey: Going to add OpenCV pre-built binaries cache to OpenCV CN CI, and implement PR's testing in OpenCV Contrib repository.
   * Lydia: preparing RISC-V article for opencv.org blog.
   * Amir: working on issue #17036 cvtColorTwoPlane(...) with two color planes having different alignments.
* Alexander:
   * dual quaternions PR: several issues have been fixed in order to speedup PR integration process.
   * "parallel_for plugins" PR has been integrated: openmp, tbb and "one tbb".
   * Rostislav is working on 3D module, moving KinFu there.
   * the new ARM target was added to OpenCV DNN (using IE plugin).
   * compared results of OpenCV QR code detector from main repository and Tencent's contribution from opencv_contrib. The results will be reported back.
* Vladimir:
   * IE now supports ARM. Information on how to build OpenCV with ARM support will be put to wiki.
* Shiqi:
   * celebrating Chinese New Year. Next week will continue working on face detection.
* Stefano:
   * benchmark comparing different implementation of matrix product: https://mmperf.org
   * state-of-art performance from deep net w/o batch norm: https://arxiv.org/abs/2102.06171. Helps to significantly accelerate deep network training and avoid the problem with possibly varying statistics between batches.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-02-10

### *__Minutes__*
* Gary:
   * fiducial tags detection project is slowly evolving
* Vadim:
   * SVE2 support is probably coming to OpenCV; will currently use simulator
   * the conversion of ficus compiler from ocaml to ficus has started
* Vincent:
   * https://developers.google.com/sandboxed-api/. Can be a GSoC 2021 project and add safe imread using sandboxed API.
* Alexander:
   * parallel_for plugin is in progress. OpenMP, TBB will be completed soon.
   * the team is working on H/W encoding/decoding in ffmpeg backend.
   * Luba Batanina has reviewed several speed recognition models. Jasper model could probably be easily converted to ONNX.
   * pollkey() function is added to highgui (when no GUI is provided).
   * GPU MatND compilation issue is solved.
   * RGBD issues when running on arm have been fixed.
* Anna:
   * Andrey: Integrated extended PR testing with OpenCV Contrib and OpenCV Extra into the main pipeline. Reproduced DNN testing locally.
   * Anastasia: finalized #17364 (PR: #849, #19477), completed #19366 analysis.
   * Alexander:
      * Reviewed CI failures and test hangs. Tuned suppression lists, fixed yet another non-free handling issue (PR #19488).
      * Reviewed issues filed against OpenCV-Python repository. Tested and closed some bugs. Introduced the same milestones as in core OpenCV. Start looking into current CI setup for the repo and weak points.
      * Reviewed, tested, helped to resolve issues with ##19126, 19448, 19439, 19309, 19392
      * Amir: tried to fulfill requirement of preserving compatibility in PR Subdiv2D, unsuccessfully. Hoped to use preprocessor macros as a flexible approach to relay between new and old logic, but it was more difficult than expected.
   * (WIP) Andrey: Going to embed extended DNN testing into the main pipeline.
   * (WIP) Sergei: Fixing problems with diagnostic tools for ONNX DNN loaders, testing it on examples from issue #19366
   * (WIP) Sergei: Preparing description for extended LSTM support in DNN module
   * (WIP) Anastasia: working on #18920, #19366
   * (WIP) Amir: amendments to PR19392 as requested in comments.
* Shiqi:
   * Working on face detection model. Trained 2 models: 1. face + 5 landmarks, 2. face + 68 landmarks, very efficient and very compact. Size ~100Kb and 250Kb, respectively. Can possibly embed those models into OpenCV.
* Stefano:
   * GTK4 apps can now run in a browser (https://developer.gnome.org/gtk4/unstable/gtk-broadway.html)
   * Vulkan-based API for video decoding.
   * PyTorch started to support Vulkan shaders.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-02-03

### *__Minutes__*
* Gary:
   * GSoC 2021: almost applied. 6 or 7 students still stay in touch with OpenCV.org.
   * What about getting involved into movie industry? Tracking & 3D vision Maybe contact to E.V.
* Vadim:
   * Ficus compiler is in progress; ~60 unit tests are added, many bug have been fixed
* Alexander:
   * Intel team has ARM CPU plugin for Inference Engine; relies on ARM compute library:  https://github.com/openvinotoolkit/openvino_contrib/tree/master/modules/arm_plugin
   * Added 2 ideas to GSoC page:
     * speech recognition using OpenCV DNN
     * bridge to Open3D
   * Support for OneAPI TBB: PR is submitted (includes support for user-provided backends of parallel_for_).
   * L. Batanina improved subgraph handling in OpenCV DNN.
* Anna:
   * looking at various PRs
   * improving deep learning module, in particular ONNX importer (more detailed and comprehensive report in the case of failure).
   * opencv python: moving away from travis to our own CI
   * OpenCV China CI: better opencv_extra + opencv_contrib support
* Shiqi:
   * Installed proxy for OpenCV China CI. It made the connection to github much smoother.
   * The nearest plans is to improve libfacedetect, possibly integrate it into OpenCV.
* Vincent:
   * Adding custom InputArray/OutputArray as possible GSoC project. Can possibly mentor or co-mentor.
   * Possible issues with latest versions of OpenCV: 1. inline namespaces, 2. protobuffers (will possibly submit pull request).

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-01-27

### *__Minutes__*
* Gary:
   * GSoC ideas list is being composed
   * Maybe parts of Tencent code can be reused for fiducial tags detection
* Vadim:
   * Ficus compiler is in progress
   * Gave talk on OpenCV 4.5/5.0 (DNN-centered)
* Alexander
   * C++ sample for DaSiamRPN was merged. Tracking API is being polished
   * The work on parallel_for() backend on-fly switching is in progress.
   * CI Infrastructure improvements. More unified linux selection from docker registry
   * Continue integration of OpenCV China CI.
* Anna
   * Alexander: Organized OpenCV-Python repository transfer to OpenCV organization on Github: github/opencv/opencv/python (pip; later some versions for Ubuntu)
   * Alexander: Extended OpenCV CN CI: added Java and Python bindings test on Windows and TEngine testing on ARM; filed related bug #19399.
   * Alexander: Prepared plan for the second stage of OpenCV CN CI contract.
   * Reviewed, tested, helped to resolve issues with PRs ## 17604, 19388, 19078, 19364, 19259 contrib ## 2827 and 2805. Continued work on incoming issues.
   * Andrey: Run the build of OpenCV and OpenCV Contrib locally. Also run tests from OpenCV Extra. Created the Jenkins pipeline to test fixes there.
   * Igor: Finished ccache enabling for Mac OS python packages build in Travis CI. 
   * Amir: restored API / ABI in PR 19126, checks passing. Was involved in Identifying problems in PR17836.
* Shiqi:
   * concated H for CI system. They will unlikely install proxy. But some other alternatives can be considered for smoother network experience.
<pre>
--
</pre>
* Some GSoC ideas to add:
   * Data augmentation module for deep learning training
   * Audio I/O + speech recognition example
   * Higher-level image operations (inspired by pyimagesearch?)
   * Fingerprint recognition sample (?), iris recognition sample (?)

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-01-20

### *__Minutes__*
* Gary:
   * GSoC 2021 Ideas Page set up (in progress)
   * AprilTag detector is still in progress (probably, a part of the new QR code detector can be re-used)
   * some web framework (with web version of imshow etc.) is being developed by some friendly company, and maybe useful for OpenCV.
* Vadim:
   * Tencent has submitted QR code detector into opencv_contrib (under OpenCV/Apache 2 license). Reviewed it (together with Alexander A. from Intel). It works very well. Updated the example to do live detection.
   * good progress on the Ficus compiler
   * reviewed the article for OpenCV.org blog on the places recognition.
* Alexander
   * C++ sample DaSIAM PRN tracker was reviewed and merged.
   * OpenCV CN CI is added into OpenCV CI.
   * Issue with GCC v10 is investigated (wrong support for dispatching)
   * macOS, iOS builds now use ccache.
* Anna
   * Working on several PRs (Python bindings etc.)
   * Voronoi diagram calculation algorithm has been fixed.
   * Provided guide how to download and use network in a Python sample.
   * OpenCV DNN module loader is extended to provide extended diagnostic (as many problems as possible).
   * Finalizing the work on the "official" OpenCV Python package.
   * Good features to track.
* Shiqi:
   * OpenCV CI system is almost ready; Network is unstable. The company who is responsible for the network part (H company) will look into it.
   * Mac mini M1 is ordered and will arrive this month or beginning of the next month.
* Stefano:
   * Visual transformer survey.
   * Looking for the coverage of compiler stack, in particular, sparse kernels.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2021-01-13

## __*Agenda*__
* Welcome Back
* GSoC 2021
* OpenCV 5.0

### *__Minutes__*
* GSoC -- fiducial detection finish for calibration
   * Calibration toolbox ...
   * All scale fiducial pattern
   * Jan 30 Org registration starts
* Alexander
   * Euler angle support reviewed and merged
   * [Answers.opencv.org](https://answers.opencv.org/questions/) has been made read-only and activity has been moved to much more interactive  [forum.opencv.org](https://forum.opencv.org/)
   * 3D module RGBD parts to 3D module in progress
* OpenCV 5.0
   * Q1 early release
* Anna
* Transfer of Python build to our site
   * PyPI (mac has some issues being resolved)
      * Going to discuss with original author
   * build server for ARM testing continuous integration server in China is up and running
      * Status of ARM builds being linked show up on main server site
   * Working on issues with DNN modules/layers for extending to some specific network architectures and layers (LSTM)
      * 3 people now working
* Vadim
   * Tried Orbbec's Astra 3D camera — works great in Parallels running Linux (Ubuntu 20.04) on Mac. Found one little problem, will submit patch soon. Kinect fusion sample was fixed to run on Astra camera; submitted PR.
   * Gave talk at the weekly seminar organized by Orbbec. Presented OpenCV plans on 3D. Slides will be uploaded to the shared drive.
   * Discussed the progress on OpenCV China CI with Alexander from xperience.ai. It's basically ready; just need to finish integration with OpenCV's PR pages at github and also add opencv_contrib build step (to make sure that the API changes in the main OpenCV modules do not break opencv_contrib).
   * Interviewed one guy for OpenCV China team.
   * There is some noticeable progress on Ficus compiler in the past several days, 1 major feature and 2 smaller features have been implemented.

### *__To Dos__*
* Name
  - [ ] Gary to set up Ideas page



***
# _**From end of 2020:**_
***

## 2020-12-23

## __*Agenda*__
* Last progress before 2-week end-of-year break

### *__Minutes__*
* Intel team
   * OpenCV 4.5.1 and 3.4.13 have been released.
   * [answers.opencv.org](https://answers.opencv.org/questions/) is read-only now. Activity on [forum.opencv.org](https://forum.opencv.org/) is where Q&A happens now.
   * The team has reviewed Euler Angles PR, left some comments ([https://github.com/opencv/opencv/pull/19098](https://github.com/opencv/opencv/pull/19098))
   * Putting RGBD parts to 3D module is in progress
* **Org: Done:**
   * Anastasia: fixed issue #18878
   * Amir: worked on amendments to Voronoi diagram construction with respect to new topology (i.e. Delaunay triangulation) defined by the new predicates. PR #19126 is being reviewed.
   * Alexander: Implemented full RISC-V testing pipeline for OpenCV CN CI with QEMU emulator. Prepared test suppression list for major modules. 
      * Work on multi-core & multi-theading solution for RISC-V is in progress.
      * Implemented pre-commit pipeline for PR testing on Ubuntu 18.04. Work on ARM analogue is in progress.
      * Resolved several networking and security issues and exposed CI server to the Internet. CI master is available at https://build.opencv.org.cn/
      * Analyzed failed tests on CI, filed relevant bugs to Github. All issues are tracked in spreadsheet.
* **In progress:**
   * Anastasia: working on #19183
   * Amir: started with issue #4775
   * Igor: Working on opencv-python packages build speed up
   * Alexander: CI job for PR testing on ARM
      * Read-only access for subset of jobs on CI: pre-commit, nightly.
      * General infrastructure-related tasks for China CI: notifications, backup, etc
* Vadim in Shenzhen 

_In case we skip the meeting next week: Merry Christmas and Happy New Year everyone! Hope 2021 will be a beautiful and uneventful year unlike 2020_  😄 

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2020-12-18

## __*Agenda*__
* OpenCV 4.5.1 / 3.4.13 release.
   * target release date: Dec 20-25
   * wiki: changelog
* GSOC blogposts
* OpenCV fails tests on ARM64, module : GAPI. Issues ## 19117..19124.
* ARM tests tolerance check adjustment (put under #if condition)
* China CI integration


### *__Minutes__*
* Release expected on time. AI to all: add notes to changelog.
* AI to all GSoC 2020 maintainers: ping students. Blog post about GSoC project is required. Lydia will contact to RISC-V case author and Depth Fusion
* G-API tests fail on ARM64. Alexander Alekhin reproduced a significant part of tests. The issue is treated as a non-accurate test implementation, but not a library issue. Alexander Smorkalov disables G-API on ARM64.
* Alexander Smorkalov works on OpenCV China CI and stabilizes base builds. A soon as they are stable, Alexander will work on





<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2020-12-16
### *__Minutes__*

* Vadim:
   * got back to China successfully. On the quarantine currently.
   * working on OE34 (named parameters), since it may affect a lot of OpenCV 5.x API. Stub solution for Python, Java, JS is ready. Now working on a good solution for Python.
   * Prepared PR 19082 with RISC-V copyright info, but it causes some confusion. It's now being resolved and the updated patch will be prepared shortly.
* Anna:
   * new person (Amir) joined the team. Working on fixing Delaunay triangulation in one corner case (#19126)
   * Alexander is working on a number of PRs. ARM64 issue has been filed.
   * He is also working on OpenCV China CI.
   * Nearest-neighbor resize alignment is another topic.
   * Python bindings is in progress.
   * RISC-V build preparation is in progress.
* Gary:
   * AprilTag: did not have meeting past week. Sent a bunch of datasets to the student for proper testing.
   * Want to take a look at color calibration, contributed by H inc.
   * OpenCV.org is unrolling; OpenCV trademark etc.
   * Negotiating possibility to "hire" expert to implement state-of-art bundle adjustment for OpenCV; self-calibration is another possible topic.
   * OpenCV board meetings need to be resumed. The nearest one is planned at the end of 2020.
* Alexander:
   * A. Alekhin is working on adding versioning to videoio plugings (ffmpeg etc.)
   * Closed 300 invalid/obsolete issues.
   * Finished documentation refactoring. Better look'n'feel: https://pullrequest.opencv.org/buildbot/export/pr/18712/docs/d9/df8/tutorial_root.html
   * Rostislav is moving some functionality from rgbd to 3d; reviewing PR with dual quaternions. 
   * Text recognition GSoC project results have been merged
* Shiqi:
   * helped to resolve issue with RISC-V related copyrights
   * installed fresh NVidia drivers on OpenCV China CI build nodes
   * SSL certificates uploaded
   * network has been tested
* Vincent:
   * filed several issues in the bug tracker about problems found in 4.5.0 and 3.4.12.
* Stefano:
   * participating in TF project; SiFive does excellent job on RISC-V backend


***


[[Meeting_notes]]