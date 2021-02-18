import math
import random
import zlib

def readFile():
    file = open('exempeltextMac.txt', 'r')
    txt = file.read()
    return bytearray(str(txt),'utf-8')

def makeHisto(byteArr):
    hist = {}
    #Get The ASCII Code For Each Element in 'byteArr'
    for i in byteArr:
        hist[i] = hist.get(i , 0) + 1
    #hist: --> Contains value for each characters is repeated.
    return hist

def makeProb(histo):
    histSum = 0
    probSum = 0     
    #Get Sum of all the content    
    for key in histo.keys(): 
        histSum += histo[key]
    #Add the content into a histProb List
    for key in histo.keys():
        histo[key] = histo[key] / histSum 
        # print('ProbKey: --> {:.5f}'.format(hist[key]))

    for key in histo.keys():    
        probSum += histo[key]

    print("Sum of hist: {} ".format(histSum))
    
    print("Sum of Prob: {} ".format(probSum))
    return histo

def entropi(prob):
    ent = 0
    for key in prob.keys():
        if prob[key] > 0:
            ent += prob[key] * math.log2(1/prob[key])
    print("Entropi: {}".format(ent))
    return ent

def copyByteArr(byteArr):
    return byteArr.copy()

def shuffledByteArray(byteArr): 
    copiedArr = copyByteArr(byteArr)
    decodedCopiedArr = copiedArr.decode('utf-8')
    copiedList = list(decodedCopiedArr)
    random.shuffle(copiedList)
    return copiedList

def compress(byteArr):
    copy = copyByteArr(byteArr) 
    code = list(zlib.compress(copy))
    return code

fileContent = readFile()
histogram = makeHisto(fileContent)
prob = makeProb(histogram)
ent = entropi(prob)
Shuffle = shuffledByteArray(fileContent)
print("⇓⇓⇓⇓ Shuffled ⇓⇓⇓⇓ ")
histo = makeHisto(Shuffle)
prob1 = makeProb(histo)
entropi = entropi(prob1)


# print('Shuffle: {}'.format(Shuffle))
# t1 = #66 Bites After It Has Been Compressed
# t10 = 10 * t1 #76 Bites After It Has Been Compressed
# byteArr = bytearray(str(t1), "utf-8")

# comp = compress(byteArr)
# print("{} \n".format(len(comp)))
# print(comp)

 