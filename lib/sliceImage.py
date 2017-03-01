from PIL import Image
def sliceImage(im):
    width,height = im.size
    bound = 175#decide if this pixel is black or white
    xStartFlag,xEndFlag,yStartFlag,yEndFlag = False,False,False,False
    xStart,xEnd,yStart,yEnd = 0,0,0,0
    result = []

    for i in range(width):
        if(xStartFlag==False):
            #find the start x
            for j in range(height):
                if(im.getpixel((i,j))<bound):
                    xStartFlag = True
                    xStart = i
                    break
        elif(xEndFlag==False):
            #find the end x
            xEndFlag = True
            for j in range(height):
                if(im.getpixel((i,j))<bound):
                    xEndFlag = False
            if(i==width-1):xEndFlag = True


            #when we've done finding x's boundary,find the y's,too.
            if(xEndFlag==True):
                xEnd = i

                for jj in range(height):
                    if(yStartFlag==False):
                        #find the start y
                        for ii in range(xStart,xEnd+1):
                            if(im.getpixel((ii,jj))<bound):
                                yStartFlag = True
                                yStart = jj
                                break
                    elif(yEndFlag==False):
                        #find the end y
                        if(jj-yStart<4):continue#assure that 'i' and 'j' can be recognized
                        yEndFlag = True
                        for ii in range(xStart,xEnd+1):
                            if(im.getpixel((ii,jj))<bound):
                                yEndFlag = False
                        if(jj==height-1):yEndFlag = True


                        #when we've done finding two boundary,add the sub image to result and find the next
                        if(yEndFlag == True):
                            yEnd = jj
                            xStartFlag,xEndFlag,yStartFlag,yEndFlag = False,False,False,False
                            if(xEnd-xStart>=2 and yEnd-yStart>=5):
                                result.append((xStart,yStart,xEnd,yEnd))
    return result
