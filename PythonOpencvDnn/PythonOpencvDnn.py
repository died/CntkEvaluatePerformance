import numpy as np
import cv2
import time
from cv2 import dnn

def get_class_list():
    with open(loc+'synset_words.txt', 'rt') as f:
        return [x[x.find(" ") + 1:] for x in f]

loc = "..\\CntkEvaluatePerformance\\Common\\"
image = cv2.imread(loc+'space_shuttle.jpg')

blob = dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123), False)
net = dnn.readNetFromCaffe(loc+'ResNet-50-deploy.prototxt', loc+'ResNet-50-model.caffemodel')
net.setInput(blob)
t = time.time()
prob = net.forward()
print("Evaluate with OpenCv+DNN python cost {} ms".format(round((time.time()-t)*1000)))
idxs = np.argsort(prob[0])[::-1][:3]

classes = get_class_list()
for (i, idx) in enumerate(idxs):
    print("#{0} {1:.6f} Label:{2} ".format(i + 1, prob[0][idx] , classes[idx].replace("\n","")))