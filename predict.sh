mkdir test_data
mkdir test_data_sobel
mkdir test_data_laplace
numK = 17
echo "preprocessing of test_data started..."
./preprocess.sh "$1"
echo "preprocessing of test data done..."
echo "knn with sobel features started..."
python knn.py train_data_sobel/ test_data_sobel/ nameorder_sobel $numK > sobelout
echo "knn with sobel features done..."
echo "knn with laplace features started..."
python knn.py train_data_laplace/ test_data_laplace/ nameorder_laplace $numK > laplaceout
echo "knn with laplace features done..."
echo "finalizing predictions"
numTest=$(cat nameorder_sobel | wc -l)
g++ finalize.cpp -o pred
./pred sobelout laplaceout nameorder_laplace $numTest $numK > predictedout
echo "predictions finalized..."
rm -r test_data
rm -r test_data_sobel
rm -r test_data_laplace
rm sobelout
rm laplaceout
rm pred
rm nameorder_laplace
rm nameorder_sobel