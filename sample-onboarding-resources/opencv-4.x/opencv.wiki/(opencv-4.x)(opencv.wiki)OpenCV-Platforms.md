# Running OpenCV on Various Platforms

OpenCV is a cross-platform library and is optimized to run efficiently on various platforms. In order to do that, we use the following:

* OpenCV HAL, which includes so-called Wide Universal Intrinsics with different backends: https://docs.opencv.org/master/df/d91/group__core__hal__intrin.html
* Cross-platform implementation of cv::parallel_for_() and cv::Mutex: https://docs.opencv.org/master/d7/dff/tutorial_how_to_use_OpenCV_parallel_for_.html
* A wrapper on top of dynamically loaded OpenCL runtime, so-called Transparent API (T-API): https://learnopencv.com/opencv-transparent-api/
* Optimized cross-platform and platform-specific low-level libraries, such as Intel IPP, open-source or vendor-supplied BLAS & LAPACK implementations, Eigen etc.
* A runtime dispatcher to choose the optimal branches out of several available options: https://github.com/opencv/opencv/wiki/CPU-optimizations-build-options
* Various backends for our Deep Learning Module, see https://github.com/opencv/opencv/wiki/Deep-Learning-in-OpenCV

In the subsections you can also find information about running OpenCV on some specific platforms.
