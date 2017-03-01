import os
import glob
import re 
import shutil


desktop = "/Users/danielbillmann/Desktop"

os.chdir(desktop)

# move all screenshots to their own folder
if not os.path.exists("Screenshots"):
	os.makedirs("Screenshots")
 
if not os.path.exists("misc_img"):
	os.makedirs("misc_img")

screenShotsDir = "/Users/danielbillmann/Desktop/Screenshots"
misc_img_dir = "/Users/danielbillmann/Desktop/misc_img"

screenShot = glob.glob("*.png")
for i in screenShot: 
	i = str(i)
	if re.match("^Screen Shot", i):
		os.rename(desktop + "/" + i, screenShotsDir + "/" + i)
  
img = glob.glob("*.png") 
jpeg = glob.glob("*.jpeg") 
jpg = glob.glob("*.jpg")
gif = glob.glob("*.gif")

for i in img: 
	if img:
		os.rename(desktop + "/" + i, misc_img_dir + "/" + i)
for i in jpeg:
	if jpeg:
		os.rename(desktop + "/" + i, misc_img_dir + "/" + i)
for i in jpg:
	if jpg:
		os.rename(desktop + "/" + i, misc_img_dir + "/" + i)
for i in gif:
    if gif: 
        os.rename(desktop + "/" + i, misc_img_dir + "/" + i)
        