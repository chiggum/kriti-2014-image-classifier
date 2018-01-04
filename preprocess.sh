for filename in $1/*.*; do
	name=${filename##*/}
	base=${name%.jpg}
	echo $filename
	python resize.py "$1/$base.jpg" "test_data/$base.png"
 	python sobel.py "test_data/$base.png" "test_data_sobel/$base.png"
 	python laplacian.py "test_data/$base.png" "test_data_laplace/$base.png"
done