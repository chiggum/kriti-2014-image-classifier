import sys
import os
import os.path as op
import cv2
import numpy as np

pngFolder = sys.argv[1]
testFolder = sys.argv[2]
namefile = open(sys.argv[3], "w")
numK = int(sys.argv[4])

numTrainEx=0
numTestEx=0
trainData = []
responses = []
testData = []
responses2 = []

includedExtenstions=['png']
fileNames=[fn for fn in os.listdir(pngFolder) if any([fn.endswith(ext) for ext in includedExtenstions])]
fileNames2=[fn for fn in os.listdir(testFolder) if any([fn.endswith(ext) for ext in includedExtenstions])]

fileNames = sorted(fileNames)
fileNames2 = sorted(fileNames2)

for pngFile in fileNames:
	baseName = op.splitext(pngFile)[0]
	if -1 != baseName.find('art'):
		responses.append(0)
	else:
		responses.append(1)
	inputFile = op.join(pngFolder,pngFile)
	img=cv2.imread(inputFile)
	temp=[]
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			temp.append(float(img[i][j][0] + 256*img[i][j][1] +256*256*img[i][j][2])/256*256*256.0)
	trainData.append(temp)
	numTrainEx=numTrainEx+1

for pngFile in fileNames2:
	baseName = op.splitext(pngFile)[0]
	namefile.write(baseName+'\n')
	if -1 != baseName.find('art'):
		responses2.append(0)
	else:
		responses2.append(1)
	inputFile = op.join(testFolder,pngFile)
	img=cv2.imread(inputFile)
	temp=[]
	for i in range(0, img.shape[0]):
		for j in range(0, img.shape[1]):
			temp.append(float(img[i][j][0] + 256*img[i][j][1] +256*256*img[i][j][2])/256*256*256.0)
	testData.append(temp)
	numTestEx=numTestEx+1

namefile.close()

trainData=np.matrix(trainData, dtype=float).astype(np.float32)
responses=np.array(responses, dtype=float).astype(np.float32)
testData=np.matrix(testData, dtype=float).astype(np.float32)
responses2=np.array(responses2, dtype=float).astype(np.float32)

knn = cv2.KNearest()
knn.train(trainData,responses)

cnt=0
for k in range(0, numTestEx):
	newcomer = testData[k]
	ret, results, neighbours ,dist = knn.find_nearest(newcomer, numK)
	print int(results), int(responses2[k]), int(neighbours.sum())
	if int(results) != int(responses2[k]):
		cnt=cnt+1
print "Count:", numK, cnt