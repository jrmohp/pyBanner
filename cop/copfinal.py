import sqlite3
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap


def IntelliDraw(drawer,text,font,containerWidth):
    words = text.split()
    lines = []
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

conn = sqlite3.connect('certfinal2.db')


print("Opened database successfully")

cursor = conn.cursor()
cursor.execute("SELECT tid,tname,mname,cid,cname FROM public_members")
rows = cursor.fetchall()

ifont = ImageFont.truetype("arial.ttf", 80)
bfont = ImageFont.truetype("arialbold.ttf", 80)
cfont = ImageFont.truetype("arialbold.ttf", 50)
for row in rows:
    inames = "This is to certify that?"+row[2]+ ",of team'"+row[1]+":"+row[4]+" /has participated in the Mega ATV Championship Session-3 held from 23rd Feb - 26 Feb 2018"
    cid = row[3]
    imageFile = "cop.jpg"
    img = Image.open(imageFile)
    image_width = img.size[0]
    # Drawing the iicture
    draw = ImageDraw.Draw(img)

    draw.text((2792, 1), cid, fill=0, font=cfont)

    pixelwidth = 3281
    remwidth = 0

    (split1, split2) = inames.split("?")
    inamew = draw.textsize(split1, font=ifont)
    remwidth = pixelwidth - inamew[0]
    draw.text((101, 905), split1, font=ifont, fill='black')

    newx = 101 + inamew[0] + 30
    (split2, split3) = split2.split(",")
    inamew2 = draw.textsize(split2, font=bfont)
    remwidth = remwidth - inamew2[0]
    draw.text((newx, 905), split2, font=bfont, fill='black')
    newx = newx + inamew2[0] + 30
    (split3, split4) = split3.split("'")
    inamew3 = draw.textsize(split3, font=ifont)
    remwidth = remwidth - inamew3[0]
    draw.text((newx, 905), split3, font=ifont, fill='black')
    newx = newx + inamew3[0] + 30

    (split4, split5) = split4.split(":")
    inamew4 = draw.textsize(split4, font=bfont)
    remwidth = remwidth - inamew4[0]
    if remwidth>20:
        draw.text((newx, 905), split4, font=bfont, fill='black')
        newx = newx + inamew4[0] + 30
    inamew5 = draw.textsize("representing", font=ifont)
    remwidth = remwidth - inamew5[0]

    if remwidth >= 5:
        line = 1
    else:
        line=2

    if line == 2:
        newx = 101
        newy = 905 + 105
        remwidth = 3050
    if remwidth > 5:
        draw.text((newx, 905), "representing", font=ifont, fill='black')
    else:
        line=2

    (split5, split6) = split5.split("/")
    instn = split5.split(" ")
    newx = newx + inamew5[0] + 30
    c1 = 0
    for i in instn:

        isw = draw.textsize(i, font=bfont)
        remwidth = remwidth - isw[0]
        if remwidth > 90:
            draw.text((newx, 905), i, font=bfont)
            newx = newx + isw[0] + 20
            c1 = c1 + 1
        else:
            line = 2
            break

    if line == 2:
        newx = 101
        newy = 905 + 105
        remwidth = 3050
    if line == 3:
        newx = 101
        newy = 905 + 105 + 105
        remwidth = 3050
    print(remwidth)

    while c1 < len(instn):
        print(instn[c1])
        isw = draw.textsize(instn[c1], font=bfont)
        remwidth = remwidth - isw[0]
        if remwidth > 60:
            draw.text((newx, newy), instn[c1], font=bfont)
            newx = newx + isw[0] + 20
            c1 = c1 + 1
        else:
            line = line + 1
            break

    if line == 3:
        newx = 101
        newy = 905 + 105 + 105
        remwidth = 3050
    print(remwidth)

    while c1 < len(instn):
        print(instn[c1])
        isw = draw.textsize(instn[c1], font=bfont)
        remwidth = remwidth - isw[0]
        if remwidth > 60:
            draw.text((newx, newy), instn[c1], font=bfont)
            newx = newx + isw[0] + 20
            c1 = c1 + 1
        else:
            line = line + 1
            break

    print(remwidth)
    rema = split6.split(" ")
    c2 = 0
    for i in rema:
        isw = draw.textsize(i, font=ifont)
        remwidth = remwidth - isw[0]
        print(i)
        print(remwidth)
        if remwidth > 30:
            draw.text((newx, newy), i, font=ifont)
            newx = newx + isw[0] + 20
            c2 = c2 + 1
        else:
            line = line + 1
            break

    if line == 3:
        newx = 101
        newy = 905 + 105 + 105
        remwidth = 3050
    print(remwidth)
    print(line)
    if line == 4:
        newx = 101
        newy = 905 + 105 + 105 + 105
        remwidth = 3050

    while c2 < len(rema):

        isw = draw.textsize(rema[c2], font=ifont)
        remwidth = remwidth - isw[0]
        if remwidth > 30:
            draw.text((newx, newy), rema[c2], font=ifont)
            newx = newx + isw[0] + 20
            c2 = c2 + 1
        else:
            line = line + 1
            break
    # draw.text((newx, 905), split4, font=bfont, fill='black')
    # newx = newx + inamew4[0] + 30

    print(remwidth)
    fname = row[0]+"_"+row[2]+"_"+row[3]
    # Save the image with a new name
    try:
        img.save(fname+".jpeg")
    except:
        img.save(row[3]+".jpeg")