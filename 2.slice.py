from PIL import Image
from lib.sliceImage import sliceImage
def main():
    bound = 200
    letterNum = 1000
    for i in range(100,350):
        openFile = "./images/"+str(i)+".jpg"
        im = Image.open(openFile).convert("L")
        subImage = sliceImage(im)
        for subIm in subImage:
            saveFile = "./slicedImages/"+str(letterNum)+".jpg"
            letterNum += 1
            tmp = im.crop(subIm).resize((10,10))
            tmp.save(saveFile)
if __name__ == "__main__":
    main()
