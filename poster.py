from instabot import Bot 
import datetime
import os
import time

date = datetime.datetime.now()


bot = Bot() 

bot.login(username = "michael.albert.io", 
		password = "****") 



photopath = str(date.year) + "_" + str(date.month) + "_" + str(date.day) + ".jpg"
if os.path.exists(photopath):
    print("no post today")
else:
    os.system('python postcreator.py')
    time.sleep(5)
    bot.upload_photo(photopath, 
                    caption ="#EveryVoiceCounts") 


# create last run time
f = open("lastdate.txt", "w")
f.write(str(date.year) + "/" + str(date.month) + "/" + str(date.day) + " - " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second))
f.close()
