coefficients = open('./data/result.csv','r').readlines()
for i in range(len(coefficients)):
    coefficients[i] = coefficients[i].split(',')
    for j in range(len(coefficients[i])):
        coefficients[i][j] = float(coefficients[i][j])

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import sys
from PIL import Image
from lib.sliceImage import sliceImage

def letterIdentify(im):
    attr = [1]
    for i in range(10):
        for j in range(10):
            attr.append(im.getpixel((i,j)))
    score = [0]*26
    for i in range(len(coefficients)):
        for j in range(len(coefficients[0])):
                score[j] += attr[i]*coefficients[i][j]
    maxScore = -9999999
    result = '?'
    for i in range(len(score)):
        if(score[i]>maxScore):
            maxScore = score[i]
            result = letters[i]
    return result

def predict(im):
    bound = 200
    result = ""
    subImagePos = sliceImage(im)
    for pos in subImagePos:
        subIm = im.crop(pos).resize((10,10))
        result += letterIdentify(subIm)
    return result
def main():
    #letterIdentify(Image.open("./slicedImages/1000.jpg"))
    im = Image.open(sys.argv[1]).convert("L")
    print(predict(im))
if __name__=="__main__":
    main()
