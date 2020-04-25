import sqlite3
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap


def IntelliDraw(drawer,text,font,containerWidth):
    words = text.split()
    lines = [] # prepare a return argument
    lines.append(words)
    finished = False
    line = 0
    while not finished:
        thistext = lines[line]
        newline = []
        innerFinished = False
        while not innerFinished:
            #print 'thistext: '+str(thistext)
            if drawer.textsize(' '.join(thistext),font)[0] > containerWidth:
                newline.insert(0,thistext.pop(-1))
            else:
                innerFinished = True
        if len(newline) > 0:
            lines.append(newline)
            line = line + 1
        else:
            finished = True
    tmp = []
    for i in lines:
        tmp.append( ' '.join(i) )
    lines = tmp
    (width,height) = drawer.textsize(lines[0],font)
    return (lines,width,height)

conn = sqlite3.connect('kart3.db')


print("Opened database successfully")

cursor = conn.cursor()
cursor.execute("SELECT A,B,C,D,E FROM public_treg")
rows = cursor.fetchall()

def printban():
    teamfont = ImageFont.truetype("fonts/arialbold.ttf", 180)
    ifont = ImageFont.truetype("fonts/arialbold.ttf", 130)
    numfont = ImageFont.truetype("fonts/arialbold.ttf", 1000)
    idfont = ImageFont.truetype("fonts/wl.ttf", 130)

    tname ="Invader"
    cnum ="35"
    address = "Pune, Maharashtra "
    tid = "MAC0216"
    inames ="Marathwada Mitra Mandals Institute Of Technology"
    tname = tname.upper()
    # Opening the file gg.png
    imageFile = "banner.jpg"
    img = Image.open(imageFile)
    image_width = img.size[0]
    # Drawing the iicture
    draw = ImageDraw.Draw(img)
    teamfont_size = draw.textsize(tname, font=teamfont)
    teamfont_x = (image_width / 2) - 80 - (teamfont_size[0] / 2)



    pixelwidth=3696

    lines,tmp,h = IntelliDraw(draw,inames,ifont,pixelwidth)

    j=0
    count=1


    for i in lines:
        count=count+1
        print(count)



    draw.text((teamfont_x, 690),tname, (0, 0, 0), font=teamfont)
    draw.text((135,195),cnum , (0, 0, 0), font=numfont)
    draw.text((6825, 945),tid, (255, 255, 255), font=idfont)

    for i in lines:
        linew=draw.textsize(i,font=ifont)
        diff = 3696-linew[0]
        print(diff)
        div = diff/2
        print(div)
        myx=2481+div
        print(myx)
        if count==2:
            draw.text((myx, 900 + j * h), i, font=ifont, fill='black')
        else:
            draw.text((myx, 870 + j * h), i, font=ifont, fill='black')
        j = j + 1

    addw = draw.textsize(address,font=ifont)
    diff2 = 3696-addw[0]
    div2 = diff2/2
    addx = 2481+div2
    addy = (j * h)+50
    addy2 = (j * h)
    if count == 2:
        draw.text((addx, 870 + addy), address, font=ifont, fill='black')
    else:
        draw.text((addx, 870 +addy2), address, font=ifont, fill='black')


    imgname=cnum+"_"+tname+"_"+tid

    # Save the image with a new name
    img.save(imgname + ".png")

printban()

print("Operation done successfully")
conn.close()