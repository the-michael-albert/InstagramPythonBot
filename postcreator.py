from PIL import Image, ImageDraw, ImageFont
import datetime



date = datetime.datetime.now()

curday = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1)).days

contents = 0

days_since_start = 0


def createImg(days):
    img = Image.new('RGB', (1080, 1080), color = (240, 240, 240))

    fnt = ImageFont.truetype(r"C:\Users\****** ******\.fonts\Proxima\ProximaNova-Regular.otf", 200)
    d = ImageDraw.Draw(img)
    d.text((50,10), "Day " + str(curday - int(contents)), font=fnt, fill=(200, 0, 150))



    fnt = ImageFont.truetype(r"C:\Users\****** ******\.fonts\Proxima\ProximaNova-Regular.otf", 50)
    d.text((50,300), "of waiting for justice.", font=fnt, fill=(49, 49, 49))
    d.text((50,400), "of waiting for difference.", font=fnt, fill=(49, 49, 49))
    d.text((50,500), "of waiting for equality.", font=fnt, fill=(49, 49, 49))

    fnt = ImageFont.truetype(r"C:\Users\****** ******\.fonts\Proxima\ProximaNova-Regular.otf", 75)
    d.text((50,650), "of waiting for change.", font=fnt, fill=(49, 49, 49))

    fnt = ImageFont.truetype(r"C:\Users\****** ******\.fonts\Proxima\ProximaNova-Regular.otf", 30)
    d.text((50,1000), "Posted by a robot made by Michael Albert", font=fnt, fill=(49, 49, 49))


    date = datetime.datetime.now()

    img.save(str(date.year) + "_" + str(date.month) + "_" + str(date.day) + ".jpg")


f=open("date.txt", "r")
if f.mode == 'r':
    contents = f.read()
    if contents != curday:
        print(contents)
        createImg(int(contents))
    else:
        print("Already Created Content for Today ")

