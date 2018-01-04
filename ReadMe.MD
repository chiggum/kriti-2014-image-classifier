# kriti-2014-image-classifier
- Manas Hostel

### Task
Build a model to classify images into - photographic (taken by a camera) and artistic (hand-painted).

### Approach
- K-Nearest Neighbour with `K=17` trained separately over sobel and laplacian features extracted from train data.
- For a test case,
    - sobel and laplacian features extracted.
    - if KNN-sobel says photograph then predict so
    - else if KNN-laplacian say art then predict so
    - else
        - if no. of art neighb. with KNN-sobel >= no. of photo neigh. with KNN-laplacian then predict art
        - else predict photograph

### Requirements
- Linux (preferrably Ubuntu 12.10)
- openCV python module (sudo apt-get install python-opencv)
- python 2.7
- g++

**Extract** content of `data.zip` to root directory.

NOTE: We **ASSUME** that the test images are in JPG format.

### Steps to predict
Steps to predict the category of test images:
1. Put all test images in `test` directory
2. `cd "to/the/dir/which/contains/this/Readme"`
2. `chmod +x kriti.sh`
3. `./kriti.sh`

The final predictions will be in "predictedout" file with one line for each test image name and corresponding category predicted.

NOTE: The whole process will take 15-20 minutes, so please be patient and don't interrupt the running processes. Also, it is recommended to turn off other processes.

### Update
- Obtained second prize with 91% accuracy on test set. [Certificate Link](https://1drv.ms/i/s!AsWdE6fYJr8igqpDcrLW9QLo9BRreA)
