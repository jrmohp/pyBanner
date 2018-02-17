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

for row in rows:
    teamfont = ImageFont.truetype("arialbold.ttf", 180)
    ifont = ImageFont.truetype("arialbold.ttf", 130)
    numfont = ImageFont.truetype("arialbold.ttf", 1000)
    idfont = ImageFont.truetype("wl.ttf", 130)

    # Opening the file gg.png
    imageFile = "banner.jpg"
    img = Image.open(imageFile)
    image_width = img.size[0]
    # Drawing the iicture
    draw = ImageDraw.Draw(img)
    teamfont_size = draw.textsize(row[0], font=teamfont)
    teamfont_x = (image_width / 2) - 80 - (teamfont_size[0] / 2)
    tname=row[0]
    tname = tname.upper()

    inames =row[2]
    pixelwidth=3696

    lines,tmp,h = IntelliDraw(draw,inames,ifont,pixelwidth)

    j=0
    count=1


    for i in lines:
        count=count+1
        print(count)
    if row[4]<10:
        cnum="0"+str(row[4])
    else:
        cnum = str(row[4])


    draw.text((teamfont_x, 690),tname, (0, 0, 0), font=teamfont)
    draw.text((135,195),cnum , (0, 0, 0), font=numfont)
    draw.text((6825, 945), row[3], (255, 255, 255), font=idfont)

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

    addw = draw.textsize(row[1],font=ifont)
    diff2 = 3696-addw[0]
    div2 = diff2/2
    addx = 2481+div2
    addy = (j * h)+50
    addy2 = (j * h)
    if count == 2:
        draw.text((addx, 870 + addy), row[1], font=ifont, fill='black')
    else:
        draw.text((addx, 870 +addy2), row[1], font=ifont, fill='black')


    imgname=cnum+"_"+row[0]+"_"+row[3]

    # Save the image with a new name
    img.save(imgname + ".png")

print("Operation done successfully")
conn.close()