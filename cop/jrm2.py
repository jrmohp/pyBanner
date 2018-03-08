import sqlite3
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap
import os
import sys


conn = sqlite3.connect('certfinal2.db')


print("Opened database successfully")

cursor = conn.cursor()
cursor.execute("SELECT tid,tname,mname,cid,cname FROM public_members")
rows = cursor.fetchall()

ifont = ImageFont.truetype("arial.ttf", 80)
bfont = ImageFont.truetype("arialbold.ttf", 80)
cfont = ImageFont.truetype("arialbold.ttf", 50)
for row in rows:
    inames = "This is to certify that? "+row[2]+ " ^of team '"+row[1]+" :representing |"+row[4]+" /has participated* in the Mega ATV Championship Session-3 held from 24th Feb - 26 Feb 2018 at Nashik, Maharashtra."
    cid = row[3]
    imageFile = "final4.jpg"
    img = Image.open(imageFile)
    image_width = img.size[0]
    # Drawing the iicture
    draw = ImageDraw.Draw(img)

    x=101
    y=909
    c1 = 0
    remwidth = 3000
    sum1=0
    line1 = ""
    draw.text((2792, 1), cid, fill=0, font=cfont)
    space = inames.split(" ")
    print(space)
    ac = 0
    bc = 0
    cc = 0
    dc = 0
    ec = 0
    fc = 0
    p1=0
    p2=0
    p3=0
    p4=0
    p5=0
    p6=0
    p7=0
    comma=0

    for i in space:
        isize = draw.textsize(i,font=ifont)
        if remwidth - isize[0] > 0:
            x = x + isize[0]+10
            if remwidth > 0 and x< 3404:
                remwidth = remwidth - isize[0] - 10
                line1 = line1+" "+i
                c1 = c1+1
                sum1 = sum1 + isize[0]
        else:
            break
    space = space[c1:]
    c1=0
    remwidth2 = 3000
    sum2 = 0
    line2 = ""
    x=101
    for i in space:
        isize = draw.textsize(i,font=ifont)
        if remwidth2 - isize[0] > 0:
            remwidth2 = remwidth2 - isize[0]-20
            x = x + isize[0]+20
            if remwidth2 > 0 and x< 3404:
                line2 = line2+" "+i
                c1 = c1+1
                sum2 = sum2 + isize[0]
        else:
            break


    space = space[c1:]
    c1 = 0
    sum3=0
    remwidth3 = 3000
    line3 = ""
    x = 101
    for i in space:
        isize = draw.textsize(i, font=ifont)
        if remwidth3 - isize[0] > 0:
            remwidth3 = remwidth3 - isize[0]
            x = x + isize[0] + 20
            if remwidth3 > 0 and x < 3385:
                line3 = line3 + " " + i
                c1 = c1 + 1
                sum3 = sum3 + isize[0]
        else:
            break

    space = space[c1:]
    c1 = 0
    sum4 = 0
    remwidth4 = 3000
    line4 = ""
    x = 101
    for i in space:
        isize = draw.textsize(i, font=ifont)
        if remwidth4 - isize[0] > 0:
            remwidth4 = remwidth4 - isize[0]
            x = x + isize[0] + 20
            if remwidth4 > 0 and x < 3404:
                line4 = line4 + " " + i
                c1 = c1 + 1
                sum4 = sum4 + isize[0]
        else:
            break




    print(line1)
    print(sum1)
    print(line2)
    print(sum2)
    print(line3)
    print(sum3)
    f = 3000-sum1
    x1 = 101 + (f/2)
    y1 = 1010
    last = line1

    if '?' in line1:
        ac = ac + 1
        (split1, split2) = last.split("?")
        size = draw.textsize(split1, font=ifont)
        draw.text((x1, y1), split1, font=ifont,fill='black')
        print("split1="+split1)
        p1=1
        last = split2
        x1 = x1 + size[0] + 20
    if '^' in line1:
        bc = bc + 1
        (split1, split2) = last.split("^")
        size = draw.textsize(split1, font=bfont)
        draw.text((x1, y1), split1, font=bfont)
        print("split1="+split1)
        p2=1
        last = split2
        x1 = x1 + size[0] + 20
    if "'" in line1:
        cc = cc + 1
        (split1, split2) = last.split("'")
        size = draw.textsize(split1, font=ifont)
        draw.text((x1, y1), split1, font=ifont)
        print("split1="+split1)
        p3=1
        last = split2
        x1 = x1 + size[0] + 20
        if ":" not in line1:
            draw.text((x1, y1), last, font=bfont)
            print("last="+last)
            x1 = x1 + size[0] + 20
            myc=1


    else:
        if p3 == 0:
            draw.text((x1, y1), last, font=bfont)


    if ":" in line1:
        dc = dc + 1
        (split1, split2) = last.split(":")
        size = draw.textsize(split1, font=bfont)
        draw.text((x1, y1), split1, font=bfont)
        print("split1="+split1)
        p4=1
        last = split2
        x1 = x1 + size[0] + 20
        if "|" not in line1:
            draw.text((x1, y1), last, font=ifont)
            print("last="+last)
            x1 = x1 + size[0] + 20
            myc2 = 1

    else:
        if p3== 0:
            draw.text((x1, y1), last, font=bfont)
            print("last="+last)
    if "|" in line1:
        ec = ec + 1
        (split1, split2) = last.split("|")
        size = draw.textsize(split1, font=ifont)
        draw.text((x1, y1), split1, font=ifont)
        print("split1="+split1)
        p5=1
        last = split2
        x1 = x1 + size[0] + 20
        if "/" not in line1:
            draw.text((x1, y1), last, font=bfont)
            print("last="+last)
            x1 = x1 + size[0] + 20
            myc3=1

    else:
        if p4 == 0 and p3 == 0:
            draw.text((x1, y1), last, font=ifont)
            print(last)




    f = 3000-sum2
    x1 = 101 + (f / 2)
    y1 = 1115
    last = line2

    if dc == 0:
        if ":" in line2:
            dc = dc + 1
            (split1, split2) = last.split(":")
            size = draw.textsize(split1, font=bfont)
            draw.text((x1, y1), split1, font=bfont)
            p4=1
            last = split2
            x1 = x1 + size[0] + 20
            if "|" not in line2:
                draw.text((x1, y1), last, font=ifont)
                x1 = x1 + size[0] + 20

        else:
            draw.text((x1, y1), last, font=bfont)


        if "|" in line2:
            ec = ec + 1
            (split1, split2) = last.split("|")
            size = draw.textsize(split1, font=ifont)
            draw.text((x1, y1), split1, font=ifont)
            p5=1
            last = split2
            x1 = x1 + size[0] + 20
            if "/" not in line2:
                draw.text((x1, y1), last, font=bfont)
                x1 = x1 + size[0] + 20

        else:
            if p4 == 0:
                draw.text((x1, y1), last, font=ifont)

        if "/" in line2:
            dc = dc + 1
            (split1, split2) = last.split("/")
            size = draw.textsize(split1, font=bfont)
            draw.text((x1, y1), split1, font=bfont)
            last = split2
            x1 = x1 + size[0] + 20
            draw.text((x1, y1), last, font=ifont)
            x1 = x1 + size[0] + 20

        else:
            if p5 == 0:
                draw.text((x1, y1), last, font=bfont)
    elif ec == 0:
        if "|" in line2:
            ec = ec + 1
            (split1, split2) = last.split("|")
            size = draw.textsize(split1, font=ifont)
            draw.text((x1, y1), split1, font=ifont)
            p5=1
            last = split2
            x1 = x1 + size[0] + 20
            if "/" not in line2:
                draw.text((x1, y1), last, font=bfont)
                x1 = x1 + size[0] + 20

        else:
            if p4 == 0:
                draw.text((x1, y1), last, font=ifont)

        if "/" in line2:
            fc = fc + 1
            (split1, split2) = last.split("/")
            size = draw.textsize(split1, font=bfont)
            draw.text((x1, y1), split1, font=bfont)
            p6=1
            last = split2
            x1 = x1 + size[0] + 20
            draw.text((x1, y1), last, font=ifont)
            x1 = x1 + size[0] + 20

        else:
            if p5 == 0:
                draw.text((x1, y1), last, font=bfont)
    elif fc == 0:
        if "/" in line2:
            fc = fc + 1
            (split1, split2) = last.split("/")
            size = draw.textsize(split1, font=bfont)
            draw.text((x1, y1), split1, font=bfont)
            last = split2
            x1 = x1 + size[0] + 20
            draw.text((x1, y1), last, font=ifont)
            x1 = x1 + size[0] + 20

        else:
            draw.text((x1, y1), last, font=bfont)


    f = 3000 - sum3
    x1 = 101 + (f / 2)
    print("x1=" + str(x1))
    y1 = 1220
    last = line3
    if "/" in line3:
        fc = fc + 1
        (split1, split2) = last.split("/")
        size = draw.textsize(split1, font=bfont)
        draw.text((x1, y1), split1, font=bfont)
        last = split2
        if remwidth4<3000:
            x1 = x1 + size[0] + 20
            draw.text((x1, y1), last, font=ifont)

        x1 = x1 + size[0] + 20

    else:
        draw.text((x1, y1), last, font=ifont)

    f = 3000 - sum4
    x1 = 101 + (f / 2)
    print("x1=" + str(x1))
    y1 = 1325
    last = line4
    draw.text((x1, y1), last, font=ifont)


    print(line1)
    print(sum1)
    print(line2)
    print(sum2)
    print(line3)
    print(sum3)

    print(remwidth)
    print(sum1)
    fname = row[0] + "_" + row[2] + "_" + row[3]
    # Save the image with a new name

    if not os.path.exists(row[0]):
        os.makedirs(row[0])
        name2=row[0]+"/.htaccess"
        file=open(name2,'a')
        file.write('AuthType Basic\nAuthName "Restricted Content"\nAuthUserFile /etc/apache2/.htpasswd\nRequire valid-user')
        file.close()

    try:
        img.save(row[0]+"/"+fname + ".jpeg")
    except:
        img.save(row[0]+"/"+row[0] + ".jpeg")
