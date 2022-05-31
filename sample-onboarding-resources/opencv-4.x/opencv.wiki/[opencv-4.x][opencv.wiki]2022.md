# 2022  OpenCV Technical Committee

* [Markdown Syntax](https://guides.github.com/features/mastering-markdown/)
* OpenCV
   * [OpenCV Home Page](https://opencv.org/)
   * [OpenCV Developer Site](https://github.com/opencv/opencv/wiki)
   * [OpenCV Meeting Notes Home](https://github.com/opencv/opencv/wiki/Meeting_notes)
   * [OpenCV Google Summer of Code (GSoC) ideas page 2022](https://github.com/opencv/opencv/wiki/GSoC_2022)

[[Meeting_notes]]

# Template

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-mm-dd

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

## 2022-04-13

* Gary:
  * has added 2 more ideas to GSoC 2022, would really like to bring in a decent camera calibration, have got a very good mentor for this project.
  * 2 more mentors from US can help with GSoC 2022
* Vadim:
  * big thanks to OpenCV team who partially repaired OpenCV CI, we can now test and merge PRs
  * DNN: experimental implementation of element-wise operations is ready and sent to Egor from x.ai
  * DNN: experimental implementation of convolution (including depth-wise convolution), fully-connected layer and max pooling is prepared and sent it to OpenCV China. It will also be used in Ficus inference engine.
* Shiqi:
  * Had meeting with Orbbec, who is going to bring in support for their new depth camera to OpenCV. This camera does not need OpenNI to work.
* Alexander S (x.ai):
  * Done:
    * Egor: reviewed #21831, triaged #21839.
    * Alexandr P: merged PR fix search for one contour in _filterTooCloseCandidates() #3201
    * Alexandr P: checked and closed issues #3111, #2811
    * Andrey: Prepared Windows ARM environment and tested OpenCV python packages building for #644
    * Alexander S: Reviewed, tested, helped to resolve issues with  opencv #21841, 21834,  21845, 21857,   21833, opencv-python #654, 644, 652, opencv contrib #3224, 3220
  * In progress:
    * Egor: Broadcasting draft is working, need to fix performance issues. Benchmarks: 2 times slower than the Eltwise(binary, equal shapes) layer. 
    * Alexandr P: issue Aruco python problem: “Can't find dictionary->identify #2655”
fixed, PR is being prepared
    * Alexandr P: issue "Probably a bug in aruco::getBoardObjectAndImagePoints #2921"
Issue was reproduced, fix is being prepared
  * Org:
    * Andrey will join the team fulltime to work on CI with Github Actions.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-04-06

### *__Minutes__*

### Done:

* Vadim:
  * another 2 possibly perspective projects in GSoC: adding G-API to OpenCV.js and RISC-V acceleration.
  * continue working on OpenCV DNN refactoring proposal
* Alexander V (Intel):
  * 4.6.0 community release date could be changed due to Intel business suspension in Russia.
  * OpenCV Intel team have no access to Intel CI infrastructure used for OpenCV validation.
  * Right now Aleksandr Alekhin and Maksim Shabunin are working to migrate CI infrastructure to cloud-based solution.
  * FFmpeg 5.0 support has been merged: https://github.com/opencv/opencv/pull/21754
  * One ffmpeg memory leak has been fixed: https://github.com/opencv/opencv/pull/21819
* Alexander S (x.ai):
  * Done:
    * Egor: Fixed submatrix indexation in pretty printer and sent a PR.
    * Egor: Sent a registration issue fix PR.
    * Alexander S: reviewed, tested opencv #21827, opencv-contrib #3220, #3219, opencv-python #647, #648.
  * In progress:
    * Andrey: Preparing Windows ARM environment to test OpenCV python packages building.
    * Andrey: Moving download_models.py script to OpenCV python package (5.0 scope).
    * Egor: Memory-efficient broadcasting: sped up the initial attempt, but still 5 times slower than Vadim’s solution. Looking at numpy for inspiration.
    * Kataev Victor: Put in order pinhole and fisheye undistortPoints() function with tests and issues. Create internal documentation for cmake, macros. Create proposal for new calibration utility and camera model refactor  
* Gary:
  * someone internally passed big thank to Vincent for helping with Google Street.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-03-30

### *__Minutes__*

### Done:

* Vadim:
  * Continue working on DL inference engine in Ficus. Hopefully, some simple classification models could be run by the next week.
  * Also working on extending standard library of Ficus and fixing the compiler.
  * Some updates on GSoC, see details in the separate e-mail.
* Alexander S (x.ai):
  * Done:
    * Alexander S: Reviewed, teststed, helped to resolve issues with core #21351, opencv-python #642, #641, #646,  opencv-contrib #3200, #3213.
    * Egor: Fixed initial states support in  Add CUDA backend for LSTM layer #20938.
    * Andrey: Updated builds of OpenCV python packages according to latest commits in all OpenCV repositories (release preparations). #640
    * Andrey: Prepared a fix for building OpenCV python package from source with limited network. #642
  * In progress:
    * Andrey: Moving download_models.py script to OpenCV python package (5.0 scope).
  * Org:
    * Alexander Panov is on vacation
    * Victor Kataev joined the Xperience AI team and will work on classic CV part: camera calibration, 3d reconstruction, RANSAC, et al.
* Alexander V:
  * Fixed order of python types registration (base class must go first): https://github.com/opencv/opencv/pull/21785
  * OpenVINO plugin support is in progress: https://github.com/opencv/opencv/pull/21745
  * FFmpeg 5.0 support is in progress (compilation fixes up to 3.0, tests fixes for 5.0): https://github.com/opencv/opencv/pull/21754
  * Volume python support is in progress: https://github.com/opencv/opencv/pull/21559
* [GSoC eligibility](https://developers.google.com/open-source/gsoc/faq#are_participants_from_ukraine_russia_or_belarus_allowed_to_participate_in_gsoc_2022)
* Experience . ai has experience in calibration
  * Plan to work on adding more calibration
* Team
  * Igor LSTM
  * CUDA support
  * Transformers => DNN
     * Float support 32 64
  * Alexander on vacation
     * After ARUCO improvements all into contrib module
        * Then migrate everything to main repository (opencv)
        * Wrappers for backwards compatibility
  * Python fixes ... mid April for 5.0
     * Some APIs were missing ... windows ARM support (not official binary package, but avoiding issues)
* Open Vino Plugin support FFMPEG 5.0, python package registrations
* Shiqi 
   * RockChips MPU chips for NN will help
      * Might continue 
* Vincent ... ready for OpenCV 5.0
* Gary, Prasanna
   * Developing a PixHawk platform
      * GSoC project: 
         * Document, film how to make build
         * Put in human detection/following and obstacle avoidance 
       
     


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-03-09

### *__Minutes__*

### Done:
* Vadim:
  * Continue to explore Mindspore. It's being updated really frequently, hard to follow the latest updates.
  * OpenCV China: working on OpenCV DNN acceleration, adding block layout.
* Alexander V:
  * DNN refactoring is in progress. Dnn.cpp split PR is created: https://github.com/opencv/opencv/pull/21662
  * Some additional tasks have been done:
    * establishing "Net::Impl" inheritance for isolating OpenVINO backend logic
    * inherited calls for layers creation, reset layers instances on backend switching
    * DNN OpenVINO plugin build script
    * DNN plugin API / loader / backend factory implementation is in progress 
  * DNN speech recognition sample on C++ is added: https://github.com/opencv/opencv/pull/21458
  * HashTSDF AVX fix is delivered: https://github.com/opencv/opencv/pull/21652 
  * Volume python support is in progress: https://github.com/opencv/opencv/pull/21559
* Alexander S:
  * Done:
    * Andrey: Fixed issues in builds of OpenCV python packages in Github Actions for new releases. #632
    * Andrey: Created releases of OpenCV python packages (3.4.17.63, 4.5.5.64).
    * Alexandr P: PR fix CORNER REFINE CONTOUR #3186; fixed issues, awaiting next review step; PR Fix objPoints order in GridBoard and CharucoBoard; fixed issues, awaiting next review step
    * Egor: reviewed dnn: split dnn.cpp code #21662
    * Alexander S: Reviewed, helped to resolve issues with opencv_contrib #3174, #3186, opencv python #632, #628.
    * Alexander S: Extended CUDA meanStdDev implementation with masks and CV_32F type (PR #3191).
  * In progress:
    * Alexandr P: Prepare Aruco/Charuco/Diamond bord recommendations page
    * Python script for evaluating dictionary metrics has been prepared
    * Python script is being prepared to create rotation invariant markers (non-symmetric, safe to 90*, 180* rotation and mirroring).
    * Egor: N-dimensional transpose for core is working, PR.
    * Egor: Fix LSTM support in ONNX(cpu) #21522 addressed review comments
* Shiqi:
  * two students are working on point cloud segmentation algorithms: one uses deep nets and the other uses region growing.
* Stefano:
  * ML_program dialect of MLIR: https://discourse.llvm.org/t/rfc-introduce-ml-program-dialect/60376

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-03-02

### *__Minutes__*

* Alexander S (x.ai):
  * Done:
    * Alexandr P: cv::aruco::detectMarkers consumes all available memory when CORNER_REFINE_CONTOUR #2738 add new fix without merge conflict. prepared PR fix CORNER REFINE CONTOUR #3186, awaiting review
    * Aleksandr P: Charuco seems inaccurate. #3175 checked a nd closed
    * Alexander S: Reviewed, checked, helped to resolve issues with python #627, contrib #3186, contrib#3185, #21522, #21630, #21634,
    * Egor: Split and add no-op Expand for consts #21542, merged.
    * Egor: Fix LSTM support in ONNX(cpu) #21522 backported cuda-related fixes.
  * In progress:
    * Andrey: Fixing issues in builds of OpenCV python packages in Github Action for new releases.
    * Aleksandr P: CharucoBoard_create wrong internal marker position #2623 axis orders were checked and fixed a new issue with diamond markers was found. Now it's getting fixed new tests are being prepared for new issues.
    * Egor: ONNX LSTM CUDA implementation #20938 rebased onto fixes for cpu.
* Alexander V (intel):
  * One GSoC idea has been added by Rostislav: https://github.com/opencv/opencv/wiki/GSoC_2022#idea-simple-triangle-rendering
  * Legacy IE NN builder API has been removed:  https://github.com/opencv/opencv/pull/21591
  * ONNX conformance tests are skipped for OpenVINO 2022.1: https://github.com/opencv/opencv/pull/21609 
  * Workaround has been prepared to build OCV with GCC12 on 64-bit PowerPC: https://github.com/opencv/opencv/pull/21614
  * Runtime checks were added to imgcodecs to validate input: https://github.com/opencv/opencv/pull/21620
* Shiqi:
   * Two students this semester -- 3D cloud segmentation
   * Hardware toolkit for Universities [ARM khadas](https://www.khadas.com/) [vim3 board](https://www.khadas.com/vim3)
   * possible collaboration with RPi (?)
* Vadim
   * Looking at different inference engines Mindspore Lite (Apache 2)
   * Lightweight Jit compiler to generate vector instructions on the fly
      * generate kernels on the fly that are optimal for general HW
         * Just started [github.com/vpisarev/loops](https://github.com/vpisarev/loops)
            * Inspired from [XBYAK](https://github.com/herumi/xbyak)    

### *__To Dos__*
* Gary
  - [ ] Make contact with Raspberry Pi camera project

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-02-16

### *__Minutes__*

* Vadim:
  * OpenCV China: exploration of the existing inference engines continues, below is the table with various properties (oneDNN is to be replaced with OpenVINO): ![](images/inf_engines_2022_02.png)
  * GSoC 2022: there are 14 ideas already in https://github.com/opencv/opencv/wiki/GSoC_2022. Potential mentors and contributors are welcome to join to https://groups.google.com/g/opencv-gsoc-2022.
  * Just started implementation of light-weight "Loops" JIT engine to accelerate OpenCV and Ficus: https://github.com/vpisarev/loops
* Vincent:
  * almost got rid of C API in the internal projects.
  * right shift of negative numbers (https://github.com/opencv/opencv/pull/21588) - will likely reject, because OpenCV heavily relies on 2-complement representation of negative numbers and how right shifts are implemented.
  * custom InputArrays in OpenCV 5 (https://github.com/opencv/opencv/issues/20869).
  * resolving int64 definition ambiguity in OpenCV 5 (https://github.com/opencv/opencv/issues/7573)
  * Interesting project from NVidia: https://nvlabs.github.io/instant-ngp/
* Shiqi:
  * Trying to find more resources to support OpenCV China.
  * Contacted one big chip company to possibly support OpenCV.
  * Probably should resume communication with T-head on OpenCV+RISC-V.
* Gary:
  * Could add some more ideas. It would be nice to have some robotics projects (multi-camera calibration, apriltags, SLAM etc.)

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-02-16

### *__Minutes__*

* Vadim:
  * DL engine refactoring: briefly studied Tencent's NCNN, Alibaba MNN, started to study Huawei's Mindspore Lite. Lot's of excellent code to borrow ;)
  * OpenCV China: PRs with gitcode support & tim-vm backend are ready for review; both needs to be tested independently
  * GSoC 2022: 10 ideas are there, need more
* Alexander S:
  * Done:
    * Egor: reviewed #21601, #21608.
    * Aleksandr P: CharucoBoard_create wrong internal marker position #2623. PR has been prepared and is awaiting review
    * PR fix #2623 and #2604
    * Alexandr P: checked, commented and closed aruco: Error building calibrate_camera.cpp #624 и Documentation Error Aruco     CharucoBoard.draw() (Python) #2170
    * Alexander S: Reviewed PRs #21606, Contrib #3174.
    * Alexander S: Made backlog grooming for aruco module.
  * In progress:
    * Alexandr P: start issue - cv::aruco::detectMarkers consumes all available memory when CORNER_REFINE_CONTOUR #2738
    * Egor: ONNX specific options for LSTM (PR #21522)
* Alexander V:
  * One GSoC idea has been added by Rostislav: https://github.com/opencv/opencv/wiki/GSoC_2022#idea-simple-triangle-rendering
  * Legacy IE NN builder API has been removed:  https://github.com/opencv/opencv/pull/21591
  * ONNX conformance tests are skipped for OpenVINO 2022.1: https://github.com/opencv/opencv/pull/21609 
  * Workaround has been prepared to build OCV with GCC12 on 64-bit PowerPC:  https://github.com/opencv/opencv/pull/21614 
  * Runtime checks were added to imgcodecs to validate input: https://github.com/opencv/opencv/pull/21620
* Vincent:
  * Several sanitizer bugs have been found and fixed, including GCC 12.
  * Logging level should be controllable at compile time: https://github.com/opencv/opencv/issues/21623
* Shiqi:
  * will discuss plans with students what to do on OpenCV
* Stefano:
  * there are interesting recent advances in MLIR related to efficient sparse inference
  * Google implements light-weight IREE compiler that uses MLIR technology and promises to have very low footprint: https://github.com/google/iree/
  * there is promising "lottery tickets" approach to significantly reduce the size of networks, e.g. https://analyticsindiamag.com/the-lottery-ticket-hypothesis-that-shocked-the-world/

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-02-09

### *__Minutes__*

* Vadim:
  * Ficus: DL engine is in progress, shape inference part was finished
  * OpenCV China: PRs with gitcode support & tim-vm backend are ready for review; both needs to be tested independently
  * GSoC 2022: 
* Alexander S:
  * Done:
    * Aleksandr P: Feature/aruco speedup (rebased with 4.x) #3151 was merged (after several fixes).
    * Aleksandr P: CharucoBoard_create wrong internal marker position #2623. The bug and several tests have been fixed.
  * In progress:
    * Aleksandr P: new API (like in QRCodeDetector) + PIMPL interface for ArUco module.
  * Egor is on sick leave.
* Alexander V:
  * Odometry Python support is merged into 5.x: https://github.com/opencv/opencv/pull/21439
  * Outputs handling with OpenVINO backend is fixed: https://github.com/opencv/opencv/pull/21564
  * Intel team has prepared OpenCV drop for OpenVINO 2022.1 pre-release package 
  * CVAT is using OpenCV MIL tracker (feature merged): https://github.com/openvinotoolkit/cvat/pull/4200

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-02-02

### *__Minutes__*

* Vadim:
  * Ficus: implementation of experimental DL engine is still in progress.
  * OpenCV China team started to compare various inference engines w.r.t. performance on ARM.
  * OpenCV GSoC 2022 page with possible project is started: 
* Alexander V:
  * FP denormals has been supported: https://github.com/opencv/opencv/issues/21046
  * Output registration with new names has been supported: https://github.com/opencv/opencv/pull/21540. It’s useful for ONNX, since layers names and outputs are different things there.
  * Option to enable/disable plugin linking with OpenCV has been added: https://github.com/opencv/opencv/pull/21547. It can help with cases when OpenCV is used via another library (e.g. gstreamer plugin) which shares dependencies with OpenCV plugin (e.g. tbb plugin).
  * Rostislav and Artem continue working on large-scale pipeline for large-scale dense 3D reconstruction pipeline, volume pipeline etc. (no activities on SLAM yet)
  * Continue working on adding mp3 and aac formats as audio inputs.
* Alexander S:
  * Done:
    * Aleksandr P: Feature/aruco speedup (rebased with 4.x) #3151. PR is being reviewed. Fixed several reviewer notes such as wrong usage of parameters for old tests or missing CV_Asserts.
    * Aleksandr P: checked, commented and closed several ArUco issues:
       * run python MarkerPrinter.py , get the wrong result! #3125
       * cv::aruco::detectMarkers crashes on AMD processors. #2736
    * Aleksandr P: fixed bad shape of markers (1x4) in several cases and added tests #3105. Added a new clear way to fix  the bug. Fixed PR descriptions. PR awaits the next review step.
  * In progress:
    * Aleksandr P: CharucoBoard_create wrong internal marker position #2623. The bug has been reproduced and localized.
    * Aleksandr P: new API (like in QRCodeDetector) + PIMPL interface for ArUco module.
    * Egor: fixed negative starts for Slice and opened a PR 
* Vincent:
  * fixed bugs found by some sanitizers, e.g. regarding initializing some global objects/tables etc.
  * parallel_for sometimes uses too many cores; need to look at possible solutions.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-01-26

### *__Minutes__*

* Vadim:
  * Ficus: implementation of experimental DL engine is in progress; ONNX parser and converter to DL Ast is finished (supports subgraphs and dynamic shapes), shape inference & memory allocation is in progress.
* Alexander V:
  * The latest upgrade of MSVS 2019 breaks compilation of OV in winpack_dldt package
  * The fix has been prepared: https://github.com/opencv/opencv/issues/21469
  * CVAT is going to integrate OpenCV MIL tracker: https://github.com/openvinotoolkit/cvat/pull/4200
  * FP denormals support is in progress (the initial ticket: https://github.com/opencv/opencv/issues/21046):
  * Changes in core module are merged: https://github.com/opencv/opencv/pull/21506
  * DNN changes are on review: https://github.com/opencv/opencv/pull/21521
  * NULL pointer dereference issue is fixed: https://github.com/opencv/opencv/pull/21467
  * Odometry Python support is in progress: https://github.com/opencv/opencv/pull/21439
* Alexander S:
  * Andrey: Updated docker images and dockerfiles for OpenCV python packaging building. #617
  * Alexander S: Reviewed PRs contrib #3151, Python #617, core #21506, 21454.
  * Alexander S: Made experiments with NVIDIA VPI, prepared proposal.
  * Egor: Fixed optional output support in ONNX and sent a PR.
  * Egor: Fixed ONNX’s LSTM Y, Yh, Yc outputs, enabled peephole support and set a draft PR with runtime constant enabled for now. (+3 passing conformance tests, but needs redesigning)
  * Aleksandr P: Added “tile configurator” for ArUco markers testing (allows to add any number of rotated markers to image).
  * Aleksandr P: Added FHD performance test (15 test options). New algorithm gives ~4x speed-up.
  * Aleksandr P: Found and fixed several bugs - pyramid image use errors, bad parameters. Errors were found thanks to new tests.
  * (In progress) Aleksandr P: PIMPL interface for ArUco  (it will be like QRDetector).
* Vincent:
  * bug with connected components was fixed in 4.x branch, picked this patch.
  * some issues have been found by fuzzer and memory sanitiser, will provide patch soon.
* Gary:
  * working on a prototype of self-driving car, using a toy car of moderate size that can speedup up to 70 miles/h.
  * the total cost of the current prototype (components only) is ~$4000, but it can be greatly reduced.

<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-01-19

### *__Minutes__*

* Vadim:
  * Ficus: started implementation of DL inference engine in Ficus. So far the draft design is created (data structures, basic functions). The actual operation implementation is not started yet.
  * Prepared draft proposal about OpenCV 5.x DNN, it's now reviewed by the team.
* Alexander V:
  * The crash with unaligned memory access in DNN convolution has been fixed (the issue is caused by weights from DaSiamRPN): https://github.com/opencv/opencv/pull/21426 (by Alexander A)
  * Some DNN API enhancements (explicit ctors, const methods) are proposed by the team: https://github.com/opencv/opencv/pull/21437 (Alexander A.)
  * Speech recognition sample has been ported to C++: https://github.com/opencv/opencv/pull/21458 (by the intern)
  * Modern OpenVINO package interface is supported (new DNN cmake options): https://github.com/opencv/opencv/pull/21452. By Maksim S.
  * Outdated or invalid issues has been closed on GitHub (by Alexander A)
* Alexander S:
  * Done:
    * Alexander S:
      * Reviewed, tested, helped to resolve issues with ## 21454, 21467, 21429, 21379, OpenCV-Python ## 609, 610
      * Investigated NVIDIA VPI and prepared proposal for OpenCV integration (priority 1, priority 2)
    * Egor:
      * Finished universal broadcasting with CPU, OpenCL, CUDA (#21449)
    * Vadim
      * Added possible PyModule_AddObject failure handling (PR #21468)
      * Added several fixes in Python submodules initialization (PR #21478)
      * Prepared Issue #14730 resolution (PR will be opened after PR #21478 is merged to reduce number of changes and avoid conflicts)
  * In progress:
    * Andrey: Updating docker images for OpenCV python packages building.
    * Alexander P:
      * Feature/aruco speedup PR #3151 (was created to avoid regression in original user PR) and #2790: successfully done rebase ArUco speedup to 4.x
      * looked at Aruco3 article to check PR code
      * fixed several issues (refactoring and merging) from original PR (#2790)
      * created new performance tests
    * Vadim:
      * Finalizing Python types annotation generation (PR #20370) (was blocked by Issue #14730 due to cyclic dependencies between submodules and top level module).
      * Started work on LSTM layer fixes: 
        * constant/dynamic inputs issue (#21118)
        * Abandoned implementation with CuDNN #20938
* Vincent:
  * almost everything is fine, except for a few minor issues:
    * crash in connected components (fixed)
    * building opencv dnn for mobile
  * started conversation with Rostislav about possible Draco integration


<pre>
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
</pre>

## 2022-01-12

### *__Minutes__*

* Vadim:
  * Ficus: started working on a tiny deep learning inference engine. The goals are:
    * test ficus in another close-to-real-world scenario
    * prototype the next-gen inference engine for OpenCV
    * experiment with some novel features
  * OpenCV China:
    * PR with Tim-VX support is being debugged to make sure it runs smoothly in our CI.
    * The preliminary performance table for the model zoo was composed (https://github.com/opencv/opencv_zoo). For Intel platform we currently use the default backend, plan to make use of OpenVINO soon.
* Alexander V:
  * New Levenberg-Marquadt algorithm implementation has been merged: https://github.com/opencv/opencv/pull/21018
  * Audio functionality has been integrated into speech recognition sample: https://github.com/opencv/opencv/pull/21197
  * Aruco module has been scanned by Protex, no license issues were observed. Aruco code is treated by Protex as OpenCV code managed by OpenCV license. So it can be moved from opencv_contrib to the main opencv repository.
* Alexander S:
  * Done:
    * Alexander S: Prepared CI proposal.
    * Alexander S: Reviewed, tested, helped to resolve issues with #21386, #21351, #609, 
    * Egor:  Added domain support to model diagnostic tool and sent a PR.
    * Egor: Reviewed:
       * #21384: proposed to reuse the existing code and pointed to a way to achieve it.
       * #21415: explained that I'm already working on this and my last working version should outperform the proposed solution.
    * Egor: implemented ONNX Backend API in my branch: opencv side, onnx backend-scoreboard side: Dockerfile(for now I build opencv inside the container, in the future we can install opencv-python from pip); which allows backend-scoreboard to generate the report(index_dev.html). We can probably merge this upstream - backend-scoreboard uses Azure jobs to periodically rerun tests. The resulting support percentage differ from the cpp one because:
        * For cpp I used tests from onnx-master, which aren’t in sync with pip version yet. Python version has a few pytorch-converted tests. OpenCV doesn’t support 1-d mats and resulting shapes differ(e.g. (3,) vs (3,1)).
    * Alexander P: Vacations.
  * In progress:
    * Andrey: Unifying factory method wrapper for classes inherited from cv::Algorithm. #21406
    * Egor: WIP on general broadcasting: offset calculations seem to be correct now.
* Shiqi:
  * The PR by my students has been merged: Add support for 3D point cloud segmentation, using the USAC framework. #21276
* Gary:
  * We've built an autonomous robot that works with Ardupilot but we're having some motor control problems (circles on "straight" command) that hopefully will get resolved. 
  * Futurewei renewed their Gold Membership! The funds are unrestricted but our intent is to use it to further robotics capability in OpenCV 
  * We need to start thinking about Google Summer of Code projects. 
     * Easier, faster load of image of data to something that works with tensors for the major deep learning libraries is one. 
     * Robotics platform stuff is another.
==
during the meeting it was a lengthy conversation with Alexander S on 1) camera calibration and 2) ONNX coverage in OpenCV DNN

1. Camera Calibration:
  * There is obvious need (multiple user requests and reports, direct or indirect) that camera calibration in OpenCV needs to be revised; indeed, it was build around 20-years old technology, so it's time to upgrade it.
  * Alexander S will start composing evolution proposal to improve camera calibration
  * Much more extensive testing/benchmarking of camera calibration functionality is needed; currently we use very few test cases.
  * Better documentation is needed, in particular, the discussion of the proper use of different calibration rigs
  * Better solver is needed. Probably, the recently added Bundle Adjustment engine can be re-used for camera calibration.
  * The building blocks of camera calibration/stereo camera calibration pipelines that employ RANSAC can be replaced with the corresponding functions from the new USAC framework
  * There are approaches to calibrate camera using an arbitrary textured planar calibration rig (that may include significantly more feature points, compared to the traditional chessboards/circles patterns), e.g. https://www.epfl.ch/labs/cvlab/software/descriptors-and-keypoints/bazar/bazar-calib/. We should consider it.
  * Elements from https://github.com/opencv/opencv/tree/4.x/apps/interactive-calibration could be moved to calib module and/or the app could be better advertised, maybe improved.
  * Aruco module from opencv_contrib could be moved to opencv.
  * There could be helper functions created that would retrieve the name/model of the camera attached to computer (or embedded into smartphone) and the corresponding camera matrix/distortion coefficients can be retrieved from a database.
  * There could be helper functions to conveniently save/restore the calibrated camera information
  * Multi-sensor registration (e.g. TOF camera + RGB camera) could be added as well

2. Deep learning:
  * OpenCV currently covers ~24% of ONNX (according to the following test: http://onnx.ai/backend-scoreboard/onnxruntime_details_stable.html), which is quite low of course (even though we can handle many useful CV models (for classification, detection, tracking, pose estimation, segmentation etc.) and even some speech recognition models). We need to support more.
  * Let's state that by OpenCV 5 we should reach at least 50% in the above-mentioned scoreboard; 70%+ will be a very good result.
  * For that and also for easier integration of various NPU-specific DNN backends we will likely need to revise our graph engine in OpenCV DNN. The inference engine in Ficus (WIP) could probably be used to prototype such advanced graph engine.
  * If by GSoC 2022 we will revise OpenCV DNN design, we could use students to implement some of operations
